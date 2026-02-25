import sys
import platform
from unicodedata import name
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import * 
from matplotlib.pyplot import plot
import mysql
import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from mysql import connector
from PySide6.QtWidgets import QLabel
# GUI FILE
from app_modules import *
import numpy as np
from scipy.interpolate import make_interp_spline
from login import Ui_Form
from cadastro import Ui_Form as Ui_Cadastro
from esqueci_senha import Ui_Form as Ui_Esqueci
from ui_styles import DARK_THEME, LIGHT_THEME
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale



# FORÇA idioma pt_BR e evita erro de localization
QLocale.setDefault(QLocale(QLocale.Portuguese, QLocale.Brazil))


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Login - Bem Cuidar")
        self.setFixedSize(883, 677)

        # Conexões
        self.ui.botao_login.clicked.connect(self.login)
        self.ui.botao_cadastrar.clicked.connect(self.cadastrar)
        self.ui.botao_esquecisenha.clicked.connect(self.esqueci_senha)

        from PySide6.QtGui import QIcon

        self.setWindowIcon(QIcon("assets/icon.ico"))

    def login(self):
        usuario = self.ui.campo_usuario.text().strip()
        senha = self.ui.campo_senha.text().strip()

        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha usuário e senha")
            return

        conexao = None
        cursor = None
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            # Check if user exists
            sql_check = "SELECT nome_usuario FROM usuario WHERE nome_usuario = %s"
            cursor.execute(sql_check, (usuario,))
            resultado = cursor.fetchone()

            if not resultado:
                msg = QMessageBox(self)
                msg.setWindowTitle("Usuário não encontrado")
                msg.setText("Este usuário não existe. Realize um cadastro.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("QLabel { color: black; }" \
                "QMessageBox QPushButton { background-color: #38bdf8; color: white; border-radius: 5px; padding: 5px 15px; }" \
                "QMessageBox QPushButton:hover { background-color: #0ea5e9; }")
                msg.exec()
                return

            # Check if cpf matches
            sql_login = "SELECT nome_usuario FROM usuario WHERE nome_usuario = %s AND cpf = %s"
            cursor.execute(sql_login, (usuario, senha))
            resultado_login = cursor.fetchone()

            if resultado_login:
                # Buscar o RA do usuário logado
                sql_ra = "SELECT registro FROM usuario WHERE nome_usuario = %s"
                cursor.execute(sql_ra, (usuario,))
                resultado_ra = cursor.fetchone()
                ra_usuario = resultado_ra[0] if resultado_ra else ""
                
                self.abrir_principal(usuario, ra_usuario)
            else:
                msg = QMessageBox(self)
                msg.setWindowTitle("Erro")
                msg.setText("Senha incorreta. Tente novamente.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setStyleSheet("QLabel { color: black; }")
                msg.exec()

        except Exception as e:
            print("Erro ao fazer login:", e)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def cadastrar(self):
        self.cadastro_window = TelaCadastro()
        self.cadastro_window.show()
        self.close()

    def esqueci_senha(self):
        self.esqueci_window = EsqueciSenha()
        self.esqueci_window.show()
        self.close()

    # ---------- ABRIR MAIN ----------
    def abrir_principal(self, usuario, ra=""):
        self.main_window = MainWindow(usuario, ra)
        self.main_window.show()
        self.close()


class TelaCadastro(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # UI
        loader = QUiLoader()
        arquivo_ui = QFile("cadastro.ui")
        arquivo_ui.open(QFile.ReadOnly)

        self.ui = loader.load(arquivo_ui, self)
        arquivo_ui.close()

        self.setWindowTitle("Cadastro - Bem Cuidar")
        self.setFixedSize(883, 677)

        # Conexões
        self.ui.botao_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.ui.botao_voltar.clicked.connect(self.voltar_login)


    def cadastrar_usuario(self):
        nome_usuario = self.ui.campo_usuario_cad.text().strip()
        registro = self.ui.campo_reg_cad.text().strip()
        senha = self.ui.campo_senha_cad.text().strip()

        if not nome_usuario or not registro or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos")
            return

        conexao = None
        cursor = None
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            # Check if registro already exists
            sql_check = "SELECT registro FROM usuario WHERE registro = %s"
            cursor.execute(sql_check, (registro,))
            resultado = cursor.fetchone()

            if resultado:
                QMessageBox.warning(self, "Erro", "Este RA já existe")
                return

            # Insert new user
            sql_insert = "INSERT INTO usuario (nome_usuario, registro, cpf) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (nome_usuario, registro, senha))
            conexao.commit()

            QMessageBox.information(self, "Sucesso", "Cadastrado com sucesso!")

            # Return to login
            self.voltar_login()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet("QLabel { color: black; }")
            msg.exec()

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def voltar_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class EsqueciSenha(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # UI
        loader = QUiLoader()
        arquivo_ui = QFile("esqueci_senha.ui")
        arquivo_ui.open(QFile.ReadOnly)

        self.ui = loader.load(arquivo_ui, self)
        arquivo_ui.close()

        self.setWindowTitle("Esqueci Senha - Bem Cuidar")
        self.setFixedSize(883, 677)

        # Conexões
        self.ui.botao_redefinir.clicked.connect(self.esqueci_senha)
        self.ui.botao_voltar.clicked.connect(self.voltar_login)


    def esqueci_senha(self):
        registro = self.ui.campo_reg_red.text().strip()
        nova_senha = self.ui.campo_cpf_red.text().strip()
        confirmar_senha = self.ui.campo_conf_cpf.text().strip()

        if not registro or not nova_senha or not confirmar_senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos")
            return

        if nova_senha != confirmar_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem")
            return

        conexao = None
        cursor = None
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            # Check if registro exists
            sql_check = "SELECT registro FROM usuario WHERE registro = %s"
            cursor.execute(sql_check, (registro,))
            resultado = cursor.fetchone()

            if not resultado:
                QMessageBox.warning(self, "Erro", "Este RA não existe")
                return

            # Update password
            sql_update = "UPDATE usuario SET cpf = %s WHERE registro = %s"
            cursor.execute(sql_update, (nova_senha, registro))
            conexao.commit()

            QMessageBox.information(self, "Sucesso", "Senha redefinida com sucesso!")

            # Return to login
            self.voltar_login()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("Erro")
            msg.setText(str(e))
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet("QLabel { color: black; }")
            msg.exec()

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def voltar_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class MainWindow(QMainWindow):
    def __init__(self, usuario, ra=""):
        super().__init__()
        self.usuario = usuario
        self.ra = ra

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(Style.style_main_window)

        # Set the welcome message with the logged-in user's name
        self.ui.label_usuario.setText(f"Olá, {self.usuario}")

        self.modo_escuro = False
        self.aplicar_tema()
        self.ui.btn_tema.clicked.connect(self.toggle_tema)

        # Conexões dos botões de navegação do TabWidget
        self.ui.botao_proximo.clicked.connect(self.proximo_tab)
        self.ui.botao_anterior.clicked.connect(self.anterior_tab)
        self.ui.botao_limpar.clicked.connect(self.limpar_campos)
        
        # Botão para gerar PDF
        self.ui.btn_imprimir_pdf.clicked.connect(self.gerar_pdf)

        # Botão para buscar paciente no dashboard
        self.ui.botao_buscar_paciente.clicked.connect(self.buscar_paciente)
        
        # Botão para limpar dados do dashboard
        self.ui.botao_limpar_dashboard.clicked.connect(self.limpar_dashboard)

        # Conecta botão finalizar para salvar dados
        if hasattr(self.ui, 'botao_finalizar'):
            self.ui.botao_finalizar.clicked.connect(self.salvar_prontuario)

        # Conexões da página dados_paciente
        if hasattr(self.ui, 'btn_pesquisar'):
            self.ui.btn_pesquisar.clicked.connect(self.pesquisar_paciente_dados)
        
        if hasattr(self.ui, 'btn_limpar_campos'):
            self.ui.btn_limpar_campos.clicked.connect(self.limpar_campos_dados)
        
        if hasattr(self.ui, 'btn_excluir'):
            self.ui.btn_excluir.clicked.connect(self.excluir_paciente)

            # Conexões da página adicionar_usuario (Consulta de Técnicos)
        if hasattr(self.ui, 'btn_pesquisar_tec'):
            self.ui.btn_pesquisar_tec.clicked.connect(self.pesquisar_usuario_tec)
        
        if hasattr(self.ui, 'btn_limpar_campos_tec'):
            self.ui.btn_limpar_campos_tec.clicked.connect(self.limpar_campos_tec)
        
        if hasattr(self.ui, 'btn_excluir_tec'):
            self.ui.btn_excluir_tec.clicked.connect(self.excluir_usuario_tec)
        
        print('Version: ' + platform.release())

        self.criar_grafico_atividade()

    def aplicar_tema(self):
        if self.modo_escuro:
            self.ui.frame_main.setStyleSheet(DARK_THEME)
            self.ui.stackedWidget.setStyleSheet(DARK_THEME)
        else:
            self.ui.frame_main.setStyleSheet(LIGHT_THEME)
            self.ui.stackedWidget.setStyleSheet(LIGHT_THEME)


    def toggle_tema(self):
        self.modo_escuro = not self.modo_escuro
        
        self.aplicar_tema()

    # ---------- NAVEGAÇÃO DAS TABS ----------
    def proximo_tab(self):
        """Move para a próxima tab do tabWidget_2"""
        current_index = self.ui.tabWidget_2.currentIndex()
        total_tabs = self.ui.tabWidget_2.count()
        if current_index < total_tabs - 1:
            self.ui.tabWidget_2.setCurrentIndex(current_index + 1)

    def anterior_tab(self):
        """Move para a tab anterior do tabWidget_2"""
        current_index = self.ui.tabWidget_2.currentIndex()
        if current_index > 0:
            self.ui.tabWidget_2.setCurrentIndex(current_index - 1)

    def limpar_campos(self):
        """Limpa todos os campos das tabs do tabWidget_2"""
        # Percorre todas as tabs
        for tab_index in range(self.ui.tabWidget_2.count()):
            tab = self.ui.tabWidget_2.widget(tab_index)
            
            # Encontra todos os QLineEdit na tab atual
            line_edits = tab.findChildren(QtWidgets.QLineEdit)
            for line_edit in line_edits:
                line_edit.clear()
            
            # Encontra todos os QRadioButton na tab atual e desmarca
            radio_buttons = tab.findChildren(QtWidgets.QRadioButton)
            for radio in radio_buttons:
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
            
            # Encontra todos os QComboBox na tab atual e reseta
            combo_boxes = tab.findChildren(QtWidgets.QComboBox)
            for combo in combo_boxes:
                combo.setCurrentIndex(0)
            
            # Encontra todos os QSpinBox na tab atual e reseta
            spin_boxes = tab.findChildren(QtWidgets.QSpinBox)
            for spin_box in spin_boxes:
                spin_box.setValue(0)
            
            # Encontra todos os QDateEdit na tab atual e reseta
            date_edits = tab.findChildren(QtWidgets.QDateEdit)
            for date_edit in date_edits:
                date_edit.setDate(QtCore.QDate.currentDate())
        
        # Mostra mensagem de confirmação
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Campos Limpos")
        msg.setText("Todos os campos foram limpos com sucesso!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setStyleSheet("QLabel { color: black; }" \
            "QMessageBox QPushButton { background-color: #38bdf8; color: white; border-radius: 5px; padding: 5px 15px; }" \
            "QMessageBox QPushButton:hover { background-color: #0ea5e9; }" \
            "QMessageBox { background-color: #f8fafc; }")
        msg.exec()

    def salvar_prontuario(self):
        dados = {}



        
        # percorre as abas
        for i in range(self.ui.tabWidget_2.count()):
            tab = self.ui.tabWidget_2.widget(i)

            for widget in tab.findChildren(QtWidgets.QWidget):

                name = widget.objectName()
                if not name:
                    continue

                # -------- CAMPOS SIMPLES --------
                if isinstance(widget, QtWidgets.QLineEdit):
                    valor = widget.text()
                    if valor:
                        dados[name] = valor

                elif isinstance(widget, QtWidgets.QComboBox):
                    valor = widget.currentText()
                    if valor:
                        dados[name] = valor

                elif isinstance(widget, QtWidgets.QSpinBox):
                    dados[name] = widget.value()

                elif isinstance(widget, QtWidgets.QDateEdit):
                    dados[name] = widget.date().toString("yyyy-MM-dd")

                # -------- RADIO BUTTONS --------
                elif isinstance(widget, QtWidgets.QRadioButton) and widget.isChecked():

                    parent = widget.parent()
                    while parent and not parent.objectName():
                        parent = parent.parent()

                    if parent:
                        dados[parent.objectName()] = widget.text()



        if not dados:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Aviso")
            msg.setText("Nenhum dado encontrado para salvar!")
            msg.exec()
            return


        # ---------------- MAPEAR CAMPOS DA UI -> BANCO ----------------
        
        dados_paciente = {
            "numero_de_prontuario": dados.get("numero_de_prontuario"),
            "nome_completo": dados.get("nome_completo"),
            "data_de_nascimento": dados.get("data_de_nascimento"),
            "idade": dados.get("idade"),
            "sexo": dados.get("sexo"),
            "estado_civil": dados.get("estado_civil"),
            "profissao": dados.get("profissao"),
            "endereco": dados.get("endereco"),
            "telefone": dados.get("telefone"),
            "responsavel": dados.get("responsavel"),
            "data_de_emissao_consulta": dados.get("data_de_emissao_consulta"),
        }

        dados_internacao = {
            "motivo_da_internacao": dados.get("motivo_da_internacao"),
            "como_ele_chegou": dados.get("como_ele_chegou"),
            "inicio_dos_sintomas": dados.get("inicio_dos_sintomas"),
            "data": dados.get("data"),
            "duracao_dos_sintomas": dados.get("duracao_dos_sintomas"),
            "localizacao": dados.get("localizacao"),
            "irradiacao": dados.get("irradiacao"),
            "sintomas_associados": dados.get("sintomas_associados"),
            "tratamentos_ja_realizados": dados.get("tratamentos_ja_realizados"),
            "localizacao_da_dor": dados.get("localizacao_da_dor"),
            "tipo_de_dor": dados.get("tipo_de_dor"),
            "avaliacao_de_dor": dados.get("avaliacao_de_dor"),
        }

        sinais_vitais = {
            "escala_da_dor": dados.get("escala_da_dor"),
            "pressao_arterial": dados.get("pressao_arterial"),
            "frequencia_cardiaca_pulso": dados.get("frequencia_cardiaca_pulso"),
            "frequencia_respiratoria": dados.get("frequencia_respiratoria"),
            "temperatura": dados.get("temperatura"),
            "saturacao_de_O2": dados.get("saturacao_de_O2"),
            "classificacao_pressao": dados.get("classificacao_pressao"),
            "ritmo": dados.get("ritmo"),
            "classificacao_temperatura": dados.get("classificacao_temperatura"),
            "tipo": dados.get("tipo"),
        }

        avaliacao_geral = {
            "estado_geral": dados.get("estado_geral"),
            "nivel_de_consciencia": dados.get("nivel_de_consciencia"),
            "hidratacao": dados.get("hidratacao"),
            "nutricao": dados.get("nutricao"),
            "locomocao": dados.get("locomocao"),
            "orientacao": dados.get("orientacao"),
            "quanto_ao": dados.get("quanto_ao"),
            "comunicacao": dados.get("comunicacao"),
            "causa": dados.get("causa"),
            "atencao": dados.get("atencao"),
            "memoria": dados.get("memoria"),
            "expressao_facial": dados.get("expressao_facial"),
            "atitude": dados.get("atitude"),
            "postura": dados.get("postura"),
            "movimentacao": dados.get("movimentacao"),
            "movimenta_se_com_ajuda": dados.get("movimenta_se_com_ajuda"),
            "de": dados.get("de"),
        }

        dados_neurologico = {
            "pupilas": dados.get("pupilas"),
            "reagentes_a_luz": dados.get("reagentes_a_luz"),
            "forca_muscular": dados.get("forca_muscular"),
            "reflexos": dados.get("reflexos"),
            "sensibilidade": dados.get("sensibilidade"),
            "escala_de_coma_de_Glasgow": dados.get("escala_de_coma_de_Glasgow"),
            "abertura_ocular": dados.get("abertura_ocular"),
            "resposta_verbal": dados.get("resposta_verbal"),
            "resposta_motora": dados.get("resposta_motora"),
            "resposta_pupilar": dados.get("resposta_pupilar"),
        }

        dados_tecidos_cutaneo_e_mucosas = {
            "turgor_cutaneo": dados.get("turgor_cutaneo"),
            "icterica": dados.get("icterica"),
            "cianose": dados.get("cianose"),
            "cianose_local": dados.get("cianose_local"),
            "coloracao_da_pele": dados.get("coloracao_da_pele"),
            "outras_coloracao_da_pele": dados.get("outras_coloracao_da_pele"),
            "presenca_de_sudorese": dados.get("presenca_de_sudorese"),
            "ps_local": dados.get("ps_local"),
            "textura": dados.get("textura"),
            "espessura": dados.get("espessura"),
            "elasticidade": dados.get("elasticidade"),
            "mobilidade": dados.get("mobilidade"),
            "edma": dados.get("edma"),
            "edma_local": dados.get("edma_local"),
            "cacifo": dados.get("cacifo"),
            "sensibilidade_dolorosa": dados.get("sensibilidade_dolorosa"),
            "sensabilidade_tatil": dados.get("sensabilidade_tatil"),
            "sensibilidade_termica": dados.get("sensibilidade_termica"),
            "presenca_de_dispositivo": dados.get("presenca_de_dispositivo"),
            "pd_tipo": dados.get("pd_tipo"),
            "dispositivo_membro": dados.get("dispositivo_membro"),
            "outro_local": dados.get("outro_local"),
            "alteracoes_na_integridade_da_pele": dados.get("alteracoes_na_integridade_da_pele"),
        }

        dados_lesoes_planas = {
            "lesoes_planas": dados.get("lesoes_planas"),
            "manchas": dados.get("manchas"),
            "tipo_das_manchas": dados.get("tipo_das_manchas"),
            "local_das_manchas": dados.get("local_das_manchas"),
            "m_tamanho": dados.get("m_tamanho"),
            "m_quantidade": dados.get("m_quantidade"),
            "m_formato": dados.get("m_formato"),
            "m_distribuicao": dados.get("m_distribuicao"),
            "lesoes_hemorragicas": dados.get("lesoes_hemorragicas"),
            "lh_tipo": dados.get("lh_tipo"),
            "lh_local": dados.get("lh_local"),
            "lh_tamanho": dados.get("lh_tamanho"),
            "lh_quantidade": dados.get("lh_quantidade"),

            "lesoes_vasculares": dados.get("lesoes_vasculares"),
            "lv_tipo": dados.get("lv_tipo"),
            "lv_local": dados.get("lv_local"),
            "lv_tamanho": dados.get("lv_tamanho"),
            "lv_quantidade": dados.get("lv_quantidade"),
            "lv_formato": dados.get("lv_formato"),
            "lv_distribuicao": dados.get("lv_distribuicao"),


            "lesoes_solidas": dados.get("lesoes_solidas"),
            "ls_tipos": dados.get("ls_tipos"),
            "ls_local": dados.get("ls_local"),
            "ls_tamanho": dados.get("ls_tamanho"),
            "ls_quantidade": dados.get("ls_quantidade"),
            "ls_formato": dados.get("ls_formato"),
            "ls_contorno": dados.get("ls_contorno"),
            "ls_distribuicao": dados.get("ls_distribuicao"),
            "ls_odor": dados.get("ls_odor"),

    
            "lesoes_com_conteudo_liquido": dados.get("lesoes_com_conteudo_liquido"),
            "lcl_tipo": dados.get("lcl_tipo"),
            "lcl_local": dados.get("lcl_local"),
            "lcl_tamanho": dados.get("lcl_tamanho"),
            "lcl_formato": dados.get("lcl_formato"),
            "lcl_quantidade": dados.get("lcl_quantidade"),
            "lcl_distribuicao": dados.get("lcl_distribuicao"),
            "lcl_odor": dados.get("lcl_odor"),
            "lcl_secrecao": dados.get("lcl_secrecao"),
            "lcl_secrecao_tipo": dados.get("lcl_secrecao_tipo"),

 
            "solucoes_de_continuidade": dados.get("solucoes_de_continuidade"),
            "sc_tipo": dados.get("sc_tipo"),
            "sc_local": dados.get("sc_local"),
            "sc_tamanho": dados.get("sc_tamanho"),
            "sc_odor": dados.get("sc_odor"),
            "sc_contorno": dados.get("sc_contorno"),
            "sc_secrecao": dados.get("sc_secrecao"),
            "sc_secrecao_tipo": dados.get("sc_secrecao_tipo"),

        
            "lesoes_escamativas": dados.get("lesoes_escamativas"),
            "le_tipo": dados.get("le_tipo"),
            "le_local": dados.get("le_local"),
            "le_quantidade": dados.get("le_quantidade"),
            "le_prurido": dados.get("le_prurido"),
            "le_atrofia": dados.get("le_atrofia"),
            "le_especificar": dados.get("le_especificar"),
            "le_cicatriz": dados.get("le_cicatriz"),
            "le_c_local": dados.get("le_c_local"),
            "le_c_outras": dados.get("le_c_outras"),

        }

        dados_integridade_dos_membros_superiores_e_inferiores = {
            "simetria_im": dados.get("simetria_im"),
            "musculatura_im": dados.get("musculatura_im"),
            "local_im": dados.get("local_im"),
            "mobilidade_im": dados.get("mobilidade_im"),
            "coordenacao_im": dados.get("coordenacao_im"),
            "sensibilidade_im": dados.get("sensibilidade_im"),
            "forca_im": dados.get("forca_im"),
            "rigidez_articular_im": dados.get("rigidez_articular_im"),
            "derformidade_im": dados.get("derformidade_im"), 
            "limitacoes_de_movimento_im": dados.get("limitacoes_de_movimento_im"),
            "alteracoes_vasculares_im": dados.get("alteracoes_vasculares_im"),
            "qual_im": dados.get("qual_im"),
            "perfusao_tissular_im": dados.get("perfusao_tissular_im"),
            "condicoes_locomotora_im": dados.get("condicoes_locomotora_im"),
            "formas_de_locomocao_im": dados.get("formas_de_locomocao_im"),
            "outras_im": dados.get("outras_im"),
        }

        dados_membros_superiores = {
            "sensibilidade_ms": dados.get("sensibilidade_ms"),
            "forca_motora_ms": dados.get("forca_motora_ms"),
            "edema_ms": dados.get("edema_ms"),
            "pulsos_perifericos_ms": dados.get("pulsos_perifericos_ms"),
            "paresia_ms": dados.get("paresia_ms"),
            "plegia_ms": dados.get("plegia_ms"),
            "amputacoes_ms": dados.get("amputacoes_ms"),
            "local_amputacoes_ms": dados.get("local_amputacoes_ms"),
            "gesso_ms": dados.get("gesso_ms"),
            "tala_gessado_ms": dados.get("tala_gessado_ms"),
            "dispositivo_venoso_ms": dados.get("dispositivo_venoso_ms"),
            "local_dispositivo_venoso_ms": dados.get("local_dispositivo_venoso_ms"),
            "lesoes_ms": dados.get("lesoes_ms"),
            "local_lesoes_ms": dados.get("local_lesoes_ms"),
        }

        dados_membros_inferiores = {
                "sensibilidade_mi": dados.get("sensibilidade_mi"),
                "forca_motora_mi": dados.get("forca_motora_mi"),
                "edema_mi": dados.get("edema_mi"),
                "pulsos_perifericos_mi": dados.get("pulsos_perifericos_mi"),
                "paresia_mi": dados.get("paresia_mi"),
                "plegia_mi": dados.get("plegia_mi"),
                "amputacoes_mi": dados.get("amputacoes_mi"),
                "local_amputacoes_mi": dados.get("local_amputacoes_mi"),
                "gesso_mi": dados.get("gesso_mi"),
                "tala_gessado_mi": dados.get("tala_gessado_mi"),
                "dispositivo_venoso_mi": dados.get("dispositivo_venoso_mi"),
                "local_dispositivo_venoso_mi": dados.get("local_dispositivo_venoso_mi"),
                "lesoes_mi": dados.get("lesoes_mi"),
                "local_lesoes_mi": dados.get("local_lesoes_mi"),
        }

        dados_unhas = {
            "unha": dados.get("unha"),
            "implantacao": dados.get("implantacao"),
            "coloracao": dados.get("coloracao"),
            "u_outra": dados.get("u_outra"),
            "espessura_olhos": dados.get("espessura_olhos"),
            "e_outra": dados.get("e_outra"),
            "superficie": dados.get("superficie"),
            "s_outra": dados.get("s_outra"),
            "brilho": dados.get("brilho"),
            "consistencia": dados.get("consistencia"),
            "leuconiquia": dados.get("leuconiquia"),
            "l_qual": dados.get("l_qual"),
            "onicofagia": dados.get("onicofagia"),
            "condicoes_de_higiene": dados.get("condicoes_de_higiene"),
            "c_outra": dados.get("c_outra"),
        }

        dados_cranio = {
            "forma_cranio": dados.get("forma_cranio"),
            "outro_cranio": dados.get("outro_cranio"),
            "simetria_cranio": dados.get("simetria_cranio"),
            "massas": dados.get("massas"),
            "abaulamento": dados.get("abaulamento"),
            "contorno": dados.get("contorno"),
            "escamas": dados.get("escamas"),
            "lesoes": dados.get("lesoes"),
            "cc_tipo": dados.get("cc_tipo"),
            "cc_local": dados.get("cc_local"),
            "cabelos_cor": dados.get("cabelos_cor"),
            "quantidade": dados.get("quantidade"),
            "tipo_alteracao_cabelo": dados.get("tipo_alteracao_cabelo"),
            "localizacao_das_anormalidades": dados.get("localizacao_das_anormalidades"),
            "la_outra": dados.get("la_outra"),
            "prurido": dados.get("prurido"),
            "parasitas": dados.get("parasitas"),
            "condicoes_de_higiene_cranio": dados.get("condicoes_de_higiene_cranio"),
            "chs_outra": dados.get("chs_outra"),
        }

        dados_face = {
            "formato": dados.get("formato"),
            "f_outro": dados.get("f_outro"),
            "simetria_face": dados.get("simetria_face"),
            "edema_palpebral": dados.get("edema_palpebral"),
            "dor_seios_frontais": dados.get("dor_seios_frontais"),
            "dor_seios_paranasais": dados.get("dor_seios_paranasais"),
            "dor_seios_maxilares": dados.get("dor_seios_maxilares"),
            "outras": dados.get("outras"),
        }

        dados_olhos = {
            "simetricos": dados.get("simetricos"),
            "distancia": dados.get("distancia"),
            "acuidade_visual": dados.get("acuidade_visual"),

            "tamanho": dados.get("tamanho"),
            "fotorreativas": dados.get("fotorreativas"),

            "halo_senil": dados.get("halo_senil"),
            "presenca_de_secrecoes": dados.get("presenca_de_secrecoes"),
            "conjuntiva": dados.get("conjuntiva"),
            "coloracao_olhos": dados.get("coloracao_olhos"),
            "preservada": dados.get("preservada"),

            "movimentos_oculares": dados.get("movimentos_oculares"),
            "descricao_movimento_ocular": dados.get("descricao_movimento_ocular"),
            "forumen_lacrimal": dados.get("forumen_lacrimal"),
            "descricao_forumen": dados.get("descricao_forumen"),
            "outras_obs_olhos": dados.get("outras_obs_olhos"),
        }

        dados_narinas = {
            "simetria_narinas": dados.get("simetria_narinas"),
            "integridade_preservada_narinas": dados.get("integridade_preservada_narinas"),
            "lesoes_narinas": dados.get("lesoes_narinas"),
            "edemas_simetria": dados.get("edemas_simetria"),
            "coloracao_externa": dados.get("coloracao_externa"),

            "cavidade_nasal": dados.get("cavidade_nasal"),
            "integridade_preserva": dados.get("integridade_preserva"),
            "coloracao_interna": dados.get("coloracao_interna"),
            "secrecoes": dados.get("secrecoes"),
            "tipo_secrecao_nasal": dados.get("tipo_secrecao_nasal"),
            "tamanho_narinas": dados.get("tamanho_narinas"),
            "desvio_de_septo": dados.get("desvio_de_septo"),
            "olfato": dados.get("olfato"),
            "outras_narinas": dados.get("outras_narinas"),
        }

        dados_pavilhao_auditivo_externo = {
            "integridade_preservada_pa": dados.get("integridade_preservada_pa"),
            "presenca_de_cerumen": dados.get("presenca_de_cerumen"),
            "condicoes_de_higiene_pa": dados.get("condicoes_de_higiene_pa"),
            "queixa_de_odor": dados.get("queixa_de_odor"),
            "presenca_de_secrecoes_pa": dados.get("presenca_de_secrecoes_pa"),
            "queixa_de_zumbido": dados.get("queixa_de_zumbido"),
            "acuidade_auditiva_pa": dados.get("acuidade_auditiva_pa"),
            "uso_de_aparelho_auditivo": dados.get("uso_de_aparelho_auditivo"),
            "implantacao_pa": dados.get("implantacao_pa"),
            "outra_implantacao_pa": dados.get("outra_implantacao_pa"),
        }

        dados_regiao_cervical = {
            "simetrica_rc": dados.get("simetrica_rc"),
            "central_rc": dados.get("central_rc"),
            "presenca_de_massas_rc": dados.get("presenca_de_massas_rc"),
            "cicratizes": dados.get("cicratizes"),
            "local_rc": dados.get("local_rc"),
            "movimentacao_rc": dados.get("movimentacao_rc"),
            "rigidez_de_nuca": dados.get("rigidez_de_nuca"),
            "pulso_carotideo_rc": dados.get("pulso_carotideo_rc"),
            "ingurgimento_jugular_rc": dados.get("ingurgimento_jugular_rc"),
            "fremio_tatil": dados.get("fremio_tatil"),
            "linfonodos": dados.get("linfonodos"),
            "tireoide_rc": dados.get("tireoide_rc"),
            "outras_rc": dados.get("outras_rc"),
        }

        dados_torax = {
            "forma_torax": dados.get("forma_torax"),
            "deformidades": dados.get("deformidades"),
            "tipo_deformidades": dados.get("tipo_deformidades"),
            "integridade_cutanea": dados.get("integridade_cutanea"),
            "expansibilidade": dados.get("expansibilidade"),
            "respiracao_torax": dados.get("respiracao_torax"),
            "alteracoes": dados.get("alteracoes"),
            "tipo_de_alteracao": dados.get("tipo_de_alteracao"),
            "local_torax": dados.get("local_torax"),
            "bulhas_cardiacas": dados.get("bulhas_cardiacas"),
            "bulhas_dois_tempos": dados.get("bulhas_dois_tempos"),
            "fonese": dados.get("fonese"),
            "especificar": dados.get("especificar"),
            "oxigenacao": dados.get("oxigenacao"),
        }

        dados_boca_e_faringe = {
            "ml_integridade_preservada_bf": dados.get("ml_integridade_preservada_bf"),
            "ml_edema_bf": dados.get("ml_edema_bf"),
            "ml_rima_labial": dados.get("ml_rima_labial"),
            "ml_especificar_bf": dados.get("ml_especificar_bf"),
            "g_integridade_reservada_bf": dados.get("g_integridade_reservada_bf"),
            "g_sangramento_bf": dados.get("g_sangramento_bf"),
            "g_edema_bf": dados.get("g_edema_bf"),
            "g_lesoes_bf": dados.get("g_lesoes_bf"),
            "g_especificar_bf": dados.get("g_especificar_bf"),
            "denticao_natural": dados.get("denticao_natural"),
            "uso_de_protese": dados.get("uso_de_protese"),
            "d_conservacao_bf": dados.get("d_conservacao_bf"),
            "p_coloracao_bf": dados.get("p_coloracao_bf"),
            "p_lesoes_palato": dados.get("p_lesoes_palato"),
            "l_coloracao_bf": dados.get("l_coloracao_bf"),
            "l_lesoes_lingua": dados.get("l_lesoes_lingua"),
            "l_ulceracoes_bf": dados.get("l_ulceracoes_bf"),
            "n_acpectos_bf": dados.get("n_acpectos_bf"),
            "n_faringe_bf": dados.get("n_faringe_bf"),
            "n_coloracao_faringe": dados.get("n_coloracao_faringe"),
            "n_edema_faringe": dados.get("n_edema_faringe"),
            "a_integra_bf": dados.get("a_integra_bf"),
            "a_alteracoes_bf": dados.get("a_alteracoes_bf"),
            "a_uvula_bf": dados.get("a_uvula_bf"),
            "a_outras_bf": dados.get("a_outras_bf"),

        }

        dados_mamas = {
            "simetria_mamas": dados.get("simetria_mamas"),
            "forma_mamas": dados.get("forma_mamas"),
            "mastectomia_mamas": dados.get("mastectomia_mamas"),
            "planicie_dos_mamilos": dados.get("planicie_dos_mamilos"),
            "palpacao_de_massas": dados.get("palpacao_de_massas"),
            "localizacao_mamas": dados.get("localizacao_mamas"),
            "consistencia_mamas": dados.get("consistencia_mamas"),
            "mobilidade_mamas": dados.get("mobilidade_mamas"),
            "tamanho_mamas": dados.get("tamanho_mamas"),
            "sensibilidade_mamas": dados.get("sensibilidade_mamas"),
            "expressao_mamilar_mamas": dados.get("expressao_mamilar_mamas"),
            "presenca_de_secrecao": dados.get("presenca_de_secrecao"),
            "campo_presenca_secrecoes": dados.get("campo_presenca_secrecoes"),
        }

        dados_pulmoes = {
            "murmurios_vesiculares": dados.get("murmurios_vesiculares"),
            "tipos_de_ruidos": dados.get("tipos_de_ruidos"),
            "tosse": dados.get("tosse"),
            "expectoracao": dados.get("expectoracao"),
        }

        dados_abdomen = {
            "formato_abdomen": dados.get("formato_abdomen"),
            "simetria": dados.get("simetria"),
            "marcas_de_estiramento": dados.get("marcas_de_estiramento"),
            "integridade_abdomen": dados.get("integridade_abdomen"),
            "ausculta_abdominal": dados.get("ausculta_abdominal"),
            "sensibilidade_palpacao": dados.get("sensibilidade_palpacao"),
            "outros": dados.get("outros"),
        }

        dados_geniturinario = {
            "condicao": dados.get("condicao"),
            "integridade_geniturinario": dados.get("integridade_geniturinario"),
            "edemas": dados.get("edemas"),
            "lesoes_geniturinario": dados.get("lesoes_geniturinario"),
            "secrecoes_geniturinario": dados.get("secrecoes_geniturinario"),
            "aspecto": dados.get("aspecto"),
            "outras_geniturinario": dados.get("outras_geniturinario"),
        }

        dados_inspecao_anal = {
            "integridade_anal": dados.get("integridade_anal"),
            "tipo_alteracao_anal": dados.get("tipo_alteracao_anal"),
            "informacoes_adicionais_anal": dados.get("informacoes_adicionais_anal"),
        }

        # FIM DAS TELAS INTEGRADAS



        # Remove campos vazios
        dados_paciente = {k: v for k, v in dados_paciente.items() if v not in ("", None)}
        dados_internacao = {k: v for k, v in dados_internacao.items() if v not in ("", None)}
        dados_sinais_vitais = {k: v for k, v in sinais_vitais.items() if v not in ("", None)}
        dados_avaliacao_geral = {k: v for k, v in avaliacao_geral.items() if v not in ("", None)}
        dados_neurologico = {k: v for k, v in dados_neurologico.items() if v not in ("", None)}
        dados_tecidos_cutaneo_e_mucosas = {k: v for k, v in dados_tecidos_cutaneo_e_mucosas.items() if v not in ("", None)}
        dados_lesoes_planas = {k: v for k, v in dados_lesoes_planas.items() if v not in ("", None)}
        dados_integridade_dos_membros_superiores_e_inferiores = {k: v for k, v in dados_integridade_dos_membros_superiores_e_inferiores.items() if v not in ("", None)}
        dados_membros_superiores = {k: v for k, v in dados_membros_superiores.items() if v not in ("", None)}
        dados_membros_inferiores = {k: v for k, v in dados_membros_inferiores.items() if v not in ("", None)}
        dados_unhas = {k: v for k, v in dados_unhas.items() if v not in ("", None)}
        dados_cranio = {k: v for k, v in dados_cranio.items() if v not in ("", None)}
        dados_face = {k: v for k, v in dados_face.items() if v not in ("", None)}
        dados_olhos = {k: v for k, v in dados_olhos.items() if v not in ("", None)}
        dados_narinas = {k: v for k, v in dados_narinas.items() if v not in ("", None)}
        dados_pavilhao_auditivo_externo = {k: v for k, v in dados_pavilhao_auditivo_externo.items() if v not in ("", None)}
        dados_regiao_cervical = {k: v for k, v in dados_regiao_cervical.items() if v not in ("", None)}
        dados_torax = {k: v for k, v in dados_torax.items() if v not in ("", None)}
        dados_boca_e_faringe = {k: v for k, v in dados_boca_e_faringe.items() if v not in ("", None)}
        dados_mamas = {k: v for k, v in dados_mamas.items() if v not in ("", None)}
        dados_pulmoes = {k: v for k, v in dados_pulmoes.items() if v not in ("", None)}
        dados_abdomen = {k: v for k, v in dados_abdomen.items() if v not in ("", None)}
        dados_geniturinario = {k: v for k, v in dados_geniturinario.items() if v not in ("", None)}
        dados_inspecao_anal = {k: v for k, v in dados_inspecao_anal.items() if v not in ("", None)}





        # ---------------- BANCO DE DADOS ----------------
        conexao = None
        cursor = None

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            if dados_paciente:
                colunas = ", ".join(dados_paciente.keys())
                placeholders = ", ".join(["%s"] * len(dados_paciente))

                sql_paciente = f"""
                    INSERT INTO paciente ({colunas})
                    VALUES ({placeholders})
                """
                cursor.execute(sql_paciente, list(dados_paciente.values()))

                # ---------- INSERT INTERNAÇÃO ----------
            if dados_internacao:
                colunas_int = ", ".join(dados_internacao.keys())
                placeholders_int = ", ".join(["%s"] * len(dados_internacao))

                sql_internacao = f"""
                    INSERT INTO internacao ({colunas_int})
                    VALUES ({placeholders_int})
                """
                cursor.execute(sql_internacao, list(dados_internacao.values()))

            conexao.commit()  

                # ---------- INSERT SINAIS VITAIS ----------
            if dados_sinais_vitais:
                colunas_sinais = ", ".join(dados_sinais_vitais.keys())
                placeholders_sinais = ", ".join(["%s"] * len(dados_sinais_vitais))

                sql_sinais = f"""
                    INSERT INTO sinais_vitais ({colunas_sinais})
                    VALUES ({placeholders_sinais})
                """
                cursor.execute(sql_sinais, list(dados_sinais_vitais.values()))

            conexao.commit()  

                # ---------- INSERT AVALIACAO GERAL ----------
            if dados_avaliacao_geral:
                colunas_avaliacao = ", ".join(dados_avaliacao_geral.keys())
                placeholders_avaliacao = ", ".join(["%s"] * len(dados_avaliacao_geral))

                sql_avaliacao = f"""
                    INSERT INTO avaliacao_geral ({colunas_avaliacao})
                    VALUES ({placeholders_avaliacao})
                """
                cursor.execute(sql_avaliacao, list(dados_avaliacao_geral.values()))

            conexao.commit()  

                # ---------- INSERT NEUROLOGICO ----------
            if dados_neurologico:
                colunas_neurologico = ", ".join(dados_neurologico.keys())
                placeholders_neurologico = ", ".join(["%s"] * len(dados_neurologico))

                sql_neurologico = f"""
                    INSERT INTO neurologico ({colunas_neurologico})
                    VALUES ({placeholders_neurologico})
                """
                cursor.execute(sql_neurologico, list(dados_neurologico.values()))

            conexao.commit()  

                # ---------- INSERT TECIDOS CUTANEOS E MUCOSAS ----------
            if dados_tecidos_cutaneo_e_mucosas:
                colunas_tecidos = ", ".join(dados_tecidos_cutaneo_e_mucosas.keys())
                placeholders_tecidos = ", ".join(["%s"] * len(dados_tecidos_cutaneo_e_mucosas))

                sql_tecidos = f"""
                    INSERT INTO tecidos_cutaneo_e_mucosas ({colunas_tecidos})
                    VALUES ({placeholders_tecidos})
                """
                cursor.execute(sql_tecidos, list(dados_tecidos_cutaneo_e_mucosas.values()))

            conexao.commit()  

                # ---------- INSERT LESOES PLANAS ----------
            if dados_lesoes_planas:
                colunas_lesoes = ", ".join(dados_lesoes_planas.keys())
                placeholders_lesoes = ", ".join(["%s"] * len(dados_lesoes_planas))

                sql_lesoes = f"""
                    INSERT INTO lesoes_planas ({colunas_lesoes})
                    VALUES ({placeholders_lesoes})
                """
                cursor.execute(sql_lesoes, list(dados_lesoes_planas.values()))

            conexao.commit()

                # ---------- INSERT IM ----------
            if dados_integridade_dos_membros_superiores_e_inferiores:
                colunas_im = ", ".join(dados_integridade_dos_membros_superiores_e_inferiores.keys())
                placeholders_im = ", ".join(["%s"] * len(dados_integridade_dos_membros_superiores_e_inferiores))

                sql_im = f"""
                    INSERT INTO integridade_dos_membros_superiores_e_inferiores ({colunas_im})
                    VALUES ({placeholders_im})
                """
                cursor.execute(sql_im, list(dados_integridade_dos_membros_superiores_e_inferiores.values()))
            conexao.commit()

                    # ---------- INSERT MEMBROS SUPERIORES ----------
            if dados_membros_superiores:
                colunas_ms = ", ".join(dados_membros_superiores.keys())
                placeholders_ms = ", ".join(["%s"] * len(dados_membros_superiores))

                sql_ms = f"""
                    INSERT INTO membros_superiores ({colunas_ms})
                    VALUES ({placeholders_ms})
                """
                cursor.execute(sql_ms, list(dados_membros_superiores.values()))
            conexao.commit()

                    # ---------- INSERT MEMBROS INFERIORES ----------
            if dados_membros_inferiores:
                colunas_mi = ", ".join(dados_membros_inferiores.keys())
                placeholders_mi = ", ".join(["%s"] * len(dados_membros_inferiores))

                sql_mi = f"""
                    INSERT INTO membros_inferiores ({colunas_mi})
                    VALUES ({placeholders_mi})
                """
                cursor.execute(sql_mi, list(dados_membros_inferiores.values()))
            conexao.commit()

                    # ---------- INSERT UNHAS ----------
            if dados_unhas:
                colunas_unhas = ", ".join(dados_unhas.keys())
                placeholders_unhas = ", ".join(["%s"] * len(dados_unhas))

                sql_unhas = f"""
                    INSERT INTO unhas ({colunas_unhas})
                    VALUES ({placeholders_unhas})
                """
                cursor.execute(sql_unhas, list(dados_unhas.values()))
            conexao.commit()

                    # ---------- INSERT CRANIO ----------
            if dados_cranio:
                colunas_cranio = ", ".join(dados_cranio.keys())
                placeholders_cranio = ", ".join(["%s"] * len(dados_cranio))

                sql_cranio = f"""
                    INSERT INTO cranio ({colunas_cranio})
                    VALUES ({placeholders_cranio})
                """
                cursor.execute(sql_cranio, list(dados_cranio.values()))
            conexao.commit()


                    # ---------- INSERT FACE ----------
            if dados_face:
                colunas_face = ", ".join(dados_face.keys())
                placeholders_face = ", ".join(["%s"] * len(dados_face))

                sql_face = f"""
                    INSERT INTO face ({colunas_face})
                    VALUES ({placeholders_face})
                """
                cursor.execute(sql_face, list(dados_face.values()))
            conexao.commit()

                    # ---------- INSERT OLHOS ----------
            if dados_olhos:
                colunas_olhos = ", ".join(dados_olhos.keys())
                placeholders_olhos = ", ".join(["%s"] * len(dados_olhos))

                sql_olhos = f"""
                    INSERT INTO olhos ({colunas_olhos})
                    VALUES ({placeholders_olhos})
                """
                cursor.execute(sql_olhos, list(dados_olhos.values()))
            conexao.commit()

                    # ---------- INSERT NARINAS ----------

            if dados_narinas:
                colunas_narinas = ", ".join(dados_narinas.keys())
                placeholders_narinas = ", ".join(["%s"] * len(dados_narinas))

                sql_narinas = f"""
                    INSERT INTO narinas ({colunas_narinas})
                    VALUES ({placeholders_narinas})
                """
                cursor.execute(sql_narinas, list(dados_narinas.values()))
            conexao.commit()

                    # ---------- INSERT PAVILHAO AUDITIVO EXTERNO ----------
            if dados_pavilhao_auditivo_externo:
                colunas_pa = ", ".join(dados_pavilhao_auditivo_externo.keys())
                placeholders_pa = ", ".join(["%s"] * len(dados_pavilhao_auditivo_externo))

                sql_pa = f"""
                    INSERT INTO pavilhao_auditivo_externo ({colunas_pa})
                    VALUES ({placeholders_pa})
                """
                cursor.execute(sql_pa, list(dados_pavilhao_auditivo_externo.values()))
            conexao.commit()

                    # ---------- INSERT REGIAO CERVICAL ----------
            if dados_regiao_cervical:
                colunas_rc = ", ".join(dados_regiao_cervical.keys())
                placeholders_rc = ", ".join(["%s"] * len(dados_regiao_cervical))

                sql_rc = f"""
                    INSERT INTO regiao_cervical ({colunas_rc})
                    VALUES ({placeholders_rc})
                """
                cursor.execute(sql_rc, list(dados_regiao_cervical.values()))
            conexao.commit()

                    # ---------- INSERT TORAX ----------
            if dados_torax:
                colunas_torax = ", ".join(dados_torax.keys())
                placeholders_torax = ", ".join(["%s"] * len(dados_torax))

                sql_torax = f"""
                    INSERT INTO torax ({colunas_torax})
                    VALUES ({placeholders_torax})
                """
                cursor.execute(sql_torax, list(dados_torax.values()))
            conexao.commit()

                    # ---------- INSERT BOCA E FARINGE ----------
            if dados_boca_e_faringe:
                colunas_bf = ", ".join(dados_boca_e_faringe.keys())
                placeholders_bf = ", ".join(["%s"] * len(dados_boca_e_faringe))

                sql_bf = f"""
                    INSERT INTO boca_e_faringe ({colunas_bf})
                    VALUES ({placeholders_bf})
                """
                cursor.execute(sql_bf, list(dados_boca_e_faringe.values()))
            conexao.commit()

                    # ---------- INSERT MAMAS ----------
            if dados_mamas:
                colunas_mamas = ", ".join(dados_mamas.keys())
                placeholders_mamas = ", ".join(["%s"] * len(dados_mamas))

                sql_mamas = f"""
                    INSERT INTO mamas ({colunas_mamas})
                    VALUES ({placeholders_mamas})
                """
                cursor.execute(sql_mamas, list(dados_mamas.values()))
            conexao.commit()

                    # ---------- INSERT PULMOES ----------
            if dados_pulmoes:
                colunas_pulmoes = ", ".join(dados_pulmoes.keys())
                placeholders_pulmoes = ", ".join(["%s"] * len(dados_pulmoes))

                sql_pulmoes = f"""
                    INSERT INTO pulmoes ({colunas_pulmoes})
                    VALUES ({placeholders_pulmoes})
                """
                cursor.execute(sql_pulmoes, list(dados_pulmoes.values()))
            conexao.commit()

                    # ---------- INSERT ABDOMEN ----------
            if dados_abdomen:
                colunas_abdomen = ", ".join(dados_abdomen.keys())
                placeholders_abdomen = ", ".join(["%s"] * len(dados_abdomen))

                sql_abdomen = f"""
                    INSERT INTO abdomen ({colunas_abdomen})
                    VALUES ({placeholders_abdomen})
                """
                cursor.execute(sql_abdomen, list(dados_abdomen.values()))
            conexao.commit()

                    # ---------- INSERT GENITURINARIO ----------
            if dados_geniturinario:
                colunas_geniturinario = ", ".join(dados_geniturinario.keys())
                placeholders_geniturinario = ", ".join(["%s"] * len(dados_geniturinario))

                sql_geniturinario = f"""
                    INSERT INTO geniturinario ({colunas_geniturinario})
                    VALUES ({placeholders_geniturinario})
                """
                cursor.execute(sql_geniturinario, list(dados_geniturinario.values()))
            conexao.commit()

                    # ---------- INSERT INSPECAO ANAL ----------
            if dados_inspecao_anal:
                colunas_anal = ", ".join(dados_inspecao_anal.keys())
                placeholders_anal = ", ".join(["%s"] * len(dados_inspecao_anal))

                sql_anal = f"""
                    INSERT INTO inspecao_anal ({colunas_anal})
                    VALUES ({placeholders_anal})
                """
                cursor.execute(sql_anal, list(dados_inspecao_anal.values()))
            conexao.commit()

            


            QtWidgets.QMessageBox.information(
                self,
                "Sucesso",
                "Prontuário salvo com sucesso!"
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Erro",
                f"Erro ao salvar no banco de dados:\n{str(e)}"
            )
            print("Erro ao salvar:", e)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()




    def gerar_pdf(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from PySide6.QtWidgets import QFileDialog, QMessageBox

        dados = {}

        for i in range(self.ui.tabWidget_2.count()):
            tab = self.ui.tabWidget_2.widget(i)

            for widget in tab.findChildren(QtWidgets.QWidget):
                name = widget.objectName()
                if not name:
                    continue

                if isinstance(widget, QtWidgets.QLineEdit):
                    if widget.text():
                        dados[name] = widget.text()

                elif isinstance(widget, QtWidgets.QComboBox):
                    if widget.currentText():
                        dados[name] = widget.currentText()

                elif isinstance(widget, QtWidgets.QSpinBox):
                    dados[name] = widget.value()

                elif isinstance(widget, QtWidgets.QDateEdit):
                    dados[name] = widget.date().toString("dd/MM/yyyy")

                elif isinstance(widget, QtWidgets.QRadioButton) and widget.isChecked():
                    parent = widget.parent()
                    while parent and not parent.objectName():
                        parent = parent.parent()
                    if parent:
                        dados[parent.objectName()] = widget.text()

        campos_obrigatorios = [
            "nome_completo",
            "numero_de_prontuario",
            "data_de_nascimento",
            "sexo",
        ]

        faltando = self.validar_campos_obrigatorios(dados, campos_obrigatorios)

        if faltando:
            QMessageBox.warning(
                self.ui.centralwidget,
                "Campos obrigatórios",
                "Preencha os seguintes campos antes de gerar o PDF:\n\n"
                + "\n".join(faltando)
            )
            return

        caminho, _ = QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            "Salvar PDF",
            "prontuario.pdf",
            "PDF Files (*.pdf)"
        )

        if not caminho:
            return
        
        from reportlab.lib import colors


        pdf = canvas.Canvas(caminho, pagesize=A4)
        largura, altura = A4

        # Margens
        margem_x = 40
        y = altura - 50


        # ================== TÍTULO ==================
        pdf.setFont("Helvetica-Bold", 18)
        pdf.setFillColor(colors.HexColor("#1B8F5A"))
        pdf.drawCentredString(largura / 2, y, "PRONTUÁRIO DO PACIENTE")

        y -= 10
        pdf.line(margem_x, y, largura - margem_x, y)

        y -= 30
        pdf.setFillColor(colors.black)

        # ================== CONTEÚDO ==================
        pdf.setFont("Helvetica", 10)

        for campo, valor in dados.items():
            if not valor:
                continue
             # Nome do campo em negrito
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(margem_x, y, campo.replace("_", " ").title() + ":")

            # Valor normal
            pdf.setFont("Helvetica", 10)
            pdf.drawString(margem_x + 170, y, str(valor))

            y -= 16
        # Quebra de página automática
            if y < 50:
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = altura - 50

        pdf.save()

        QMessageBox.information(
            self.ui.centralwidget,
            "PDF gerado",
            "PDF gerado com sucesso!"
        )
   
    def validar_campos_obrigatorios(self, dados, campos_obrigatorios):
        faltando = []

        for campo in campos_obrigatorios:
            if not dados.get(campo):
                faltando.append(campo)

        return faltando



    def buscar_paciente(self):
        """Busca paciente pelo nome ou número de prontuário e atualiza os cards e a tabela"""
        termo_busca = self.ui.lineEdit_7.text().strip()
        
        if not termo_busca:
            QtWidgets.QMessageBox.warning(
                self,
                "Aviso",
                "Digite um nome ou número de prontuário para buscar."
            )
            return
        
        conexao = None
        cursor = None
        
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()
            
            # Buscar paciente pelo nome ou número de prontuário
            sql_paciente = """
                SELECT numero_de_prontuario, nome_completo, idade, estado_civil, sexo, profissao, endereco, telefone, data_de_emissao_consulta
                FROM paciente 
                WHERE nome_completo LIKE %s OR numero_de_prontuario = %s
            """
            cursor.execute(sql_paciente, (f"%{termo_busca}%", termo_busca))
            resultado_paciente = cursor.fetchone()
            
            if not resultado_paciente:
                QtWidgets.QMessageBox.information(
                    self,
                    "Não encontrado",
                    "Paciente não encontrado. Verifique o nome ou número de prontuário."
                )
                return
            
            # Atualizar Card Paciente
            nome_paciente = resultado_paciente[1]
            idade_paciente = resultado_paciente[2] if resultado_paciente[2] else "Não informado"
            
            # Card Paciente: lbl_nome e lbl_leito
            self.ui.lbl_nome.setText(f"Nome: {nome_paciente}")
            self.ui.lbl_leito.setText(f"Idade: {idade_paciente} anos")
            
            # Atualizar table_registros com os dados do paciente
            # Colunas: Prontuário, Estado Civil, Sexo, Profissão, Endereço, Telefone, Data de Consulta
            self.ui.table_registros.setRowCount(1)
            self.ui.table_registros.setItem(0, 0, QtWidgets.QTableWidgetItem(str(resultado_paciente[0]) if resultado_paciente[0] else ""))
            self.ui.table_registros.setItem(0, 1, QtWidgets.QTableWidgetItem(str(resultado_paciente[3]) if resultado_paciente[3] else ""))
            self.ui.table_registros.setItem(0, 2, QtWidgets.QTableWidgetItem(str(resultado_paciente[4]) if resultado_paciente[4] else ""))
            self.ui.table_registros.setItem(0, 3, QtWidgets.QTableWidgetItem(str(resultado_paciente[5]) if resultado_paciente[5] else ""))
            self.ui.table_registros.setItem(0, 4, QtWidgets.QTableWidgetItem(str(resultado_paciente[6]) if resultado_paciente[6] else ""))
            self.ui.table_registros.setItem(0, 5, QtWidgets.QTableWidgetItem(str(resultado_paciente[7]) if resultado_paciente[7] else ""))
            self.ui.table_registros.setItem(0, 6, QtWidgets.QTableWidgetItem(str(resultado_paciente[8]) if resultado_paciente[8] else ""))
            
            # Buscar sinais vitais (mais recente)
            sql_sinais = """
                SELECT pressao_arterial, frequencia_cardiaca_pulso, saturacao_de_O2 
                FROM sinais_vitais 
                ORDER BY id_sinais DESC LIMIT 1
            """
            cursor.execute(sql_sinais)
            resultado_sinais = cursor.fetchone()
            
            # Atualizar Card Sinais Vitais (label_7, label_302, label_303)
            if resultado_sinais:
                pa = resultado_sinais[0] if resultado_sinais[0] else "Não informado"
                fc = resultado_sinais[1] if resultado_sinais[1] else "Não informado"
                spo2 = resultado_sinais[2] if resultado_sinais[2] else "Não informado"
                
                self.ui.lbl_pa.setText(f"PA: {pa}")
                self.ui.lbl_fc.setText(f"FC: {fc}")
                self.ui.lbl_spo2.setText(f"SpO2: {spo2}")
            else:
                self.ui.lbl_pa.setText("PA: Não informado")
                self.ui.lbl_fc.setText("FC: Não informado")
                self.ui.lbl_spo2.setText("SpO2: Não informado")
            
            # Buscar avaliação geral (mais recente)
            sql_avaliacao = """
                SELECT estado_geral, nivel_de_consciencia 
                FROM avaliacao_geral 
                ORDER BY id_avaliacao DESC LIMIT 1
            """
            cursor.execute(sql_avaliacao)
            resultado_avaliacao = cursor.fetchone()
            
            # Atualizar Card Avaliação Geral (label_305, label_306)
            if resultado_avaliacao:
                estado_geral = resultado_avaliacao[0] if resultado_avaliacao[0] else "Não informado"
                nivel_consciencia = resultado_avaliacao[1] if resultado_avaliacao[1] else "Não informado"
                
                self.ui.lbl_estado_geral.setText(f"Estado Geral: {estado_geral}")
                self.ui.lbl_ndc.setText(f"Nível de Consciência: {nivel_consciencia}")
            else:
                self.ui.lbl_estado_geral.setText("Estado Geral: Não informado")
                self.ui.lbl_ndc.setText("Nível de Consciência: Não informado")
        
            # Buscar internação para calcular dias
            sql_internacao = """
                SELECT data 
                FROM internacao 
                ORDER BY id_internacao DESC LIMIT 1
            """
            cursor.execute(sql_internacao)
            resultado_internacao = cursor.fetchone()
            
            # Atualizar Card Internação (label_308, label_309)
            if resultado_internacao and resultado_internacao[0]:
                data_internacao = resultado_internacao[0]
                
                # Calcular dias de internação
                from datetime import datetime
                
                if isinstance(data_internacao, str):
                    data_internacao = datetime.strptime(data_internacao, "%Y-%m-%d")
                
                data_atual = datetime.now().date()  # agora é date
                dias_internacao = (data_atual - data_internacao).days
                
                self.ui.lbl_dias.setText(f"{dias_internacao} dias")
                self.ui.lbl_status.setText("Internado")
            else:
                self.ui.lbl_dias.setText("0 dias")
                self.ui.lbl_status.setText("Internado")
            
            # Atualizar label do paciente na tela
            self.ui.label_nome_paciente.setText(f"Paciente: {nome_paciente}")
            
            QtWidgets.QMessageBox.information(
                self,
                "Sucesso",
                "Paciente encontrado! Dados atualizados nos cards e tabela."
            )
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Erro",
                f"Erro ao buscar paciente:\n{str(e)}"
            )
            print("Erro ao buscar paciente:", e)
            
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def limpar_dashboard(self):
        """Limpa os dados exibidos no dashboard"""
        self.ui.lineEdit_7.clear()
        self.ui.lbl_nome.setText("Nome: ")
        self.ui.lbl_leito.setText("Idade: ")
        self.ui.lbl_pa.setText("PA: ")
        self.ui.lbl_fc.setText("FC: ")
        self.ui.lbl_spo2.setText("SpO2: ")
        self.ui.lbl_estado_geral.setText("Estado Geral: ")
        self.ui.lbl_ndc.setText("Nível de Consciência: ")
        self.ui.lbl_dias.setText("Dias: ")
        self.ui.lbl_status.setText("Status: Ativo")
        self.ui.label_nome_paciente.setText("Nome Do Paciente:")
        self.ui.table_registros.clearContents()
        QtWidgets.QMessageBox.information(self, "Limpo", "Dados do dashboard foram limpos.")

    # ========== DADOS PACIENTE (Página de Consulta/Exclusão) ==========
    def pesquisar_paciente_dados(self):
        """Busca pacientes por nome ou número de prontuário e exibe na tabela"""
        nome = self.ui.campo_nome.text().strip()
        prontuario = self.ui.campo_prontuario.text().strip()
        
        if not nome and not prontuario:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Digite um nome ou número de prontuário para buscar.")
            return
        
        conexao = None
        cursor = None
        
        try:
            conexao = mysql.connector.connect(host="localhost", user="Pedro", password="", port="3306", database="homologacao")
            cursor = conexao.cursor()
            
            if nome and prontuario:
                sql = """SELECT numero_de_prontuario, nome_completo, data_de_nascimento, idade, sexo, estado_civil, profissao, endereco, telefone, data_de_emissao_consulta FROM paciente WHERE nome_completo LIKE %s OR numero_de_prontuario = %s"""
                cursor.execute(sql, (f"%{nome}%", prontuario))
            elif nome:
                sql = """SELECT numero_de_prontuario, nome_completo, data_de_nascimento, idade, sexo, estado_civil, profissao, endereco, telefone, data_de_emissao_consulta FROM paciente WHERE nome_completo LIKE %s"""
                cursor.execute(sql, (f"%{nome}%",))
            else:
                sql = """SELECT numero_de_prontuario, nome_completo, data_de_nascimento, idade, sexo, estado_civil, profissao, endereco, telefone, data_de_emissao_consulta FROM paciente WHERE numero_de_prontuario = %s"""
                cursor.execute(sql, (prontuario,))
            
            resultados = cursor.fetchall()
            
            if not resultados:
                QtWidgets.QMessageBox.information(self, "Não encontrado", "Nenhum paciente encontrado.")
                return
            
            tabela = self.ui.tabela_paciente
            tabela.setRowCount(0)
            tabela.setColumnCount(10)
            headers = ["Prontuário", "Nome", "Data Nasc.", "Idade", "Sexo", "Estado Civil", "Profissão", "Endereço", "Telefone", "Data Consulta"]
            tabela.setHorizontalHeaderLabels(headers)
            
            for row_data in resultados:
                row = tabela.rowCount()
                tabela.insertRow(row)
                for col, value in enumerate(row_data):
                    if col == 2 and value and hasattr(value, 'strftime'):
                        value = value.strftime("%d/%m/%Y")
                    elif col == 9 and value and hasattr(value, 'strftime'):
                        value = value.strftime("%d/%m/%Y")
                    item = QtWidgets.QTableWidgetItem(str(value) if value else "")
                    tabela.setItem(row, col, item)
            
            tabela.resizeColumnsToContents()
            QtWidgets.QMessageBox.information(self, "Sucesso", f"Encontrado(s) {len(resultados)} paciente(s).")
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao buscar: {str(e)}")
            print("Erro:", e)
        finally:
            if cursor: cursor.close()
            if conexao: conexao.close()

    def limpar_campos_dados(self):
        """Limpa os campos de busca e a tabela na página dados_paciente"""
        if hasattr(self.ui, 'campo_nome'): self.ui.campo_nome.clear()
        if hasattr(self.ui, 'campo_prontuario'): self.ui.campo_prontuario.clear()
        if hasattr(self.ui, 'tabela_paciente'): self.ui.tabela_paciente.setRowCount(0)
        QtWidgets.QMessageBox.information(self, "Limpo", "Campos e tabela foram limpos.")

    def excluir_paciente(self):
        """Exclui o paciente selecionado na tabela"""
        tabela = self.ui.tabela_paciente
        current_row = tabela.currentRow()
        
        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um paciente na tabela para excluir.")
            return
        
        prontuario_item = tabela.item(current_row, 0)
        if not prontuario_item or not prontuario_item.text():
            QtWidgets.QMessageBox.warning(self, "Erro", "Não foi possível obter o prontuário.")
            return
        
        numero_prontuario = prontuario_item.text()
        nome_paciente = tabela.item(current_row, 1).text() if tabela.item(current_row, 1) else ""
        
        resposta = QtWidgets.QMessageBox.question(self, "Confirmar Exclusão", 
            f"Excluir {nome_paciente} (Prontuário: {numero_prontuario})?", 
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        
        if resposta != QtWidgets.QMessageBox.Yes:
            return
        
        conexao = None
        cursor = None
        
        try:
            conexao = mysql.connector.connect(host="localhost", user="Pedro", password="", port="3306", database="homologacao")
            cursor = conexao.cursor()
            sql = "DELETE FROM paciente WHERE numero_de_prontuario = %s"
            cursor.execute(sql, (numero_prontuario,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                tabela.removeRow(current_row)
                QtWidgets.QMessageBox.information(self, "Sucesso", "Paciente excluído!")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Não foi possível excluir.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {str(e)}")
        finally:
            if cursor: cursor.close()
            if conexao: conexao.close()


    def pesquisar_usuario_tec(self):
        """Busca técnicos por nome ou RA e exibe na tabela"""
        nome = self.ui.campo_nome_tec.text().strip()
        ra = self.ui.campo_ra_tec.text().strip()

        if not nome and not ra:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Digite um nome ou RA para buscar.")
            return

        conexao = None
        cursor = None

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            if nome and ra:
                sql = """
                    SELECT id_usuario, nome_usuario, registro, cpf
                    FROM usuario
                    WHERE nome_usuario LIKE %s OR registro = %s
                """
                cursor.execute(sql, (f"%{nome}%", ra))

            elif nome:
                sql = """
                    SELECT id_usuario, nome_usuario, registro, cpf
                    FROM usuario
                    WHERE nome_usuario LIKE %s
                """
                cursor.execute(sql, (f"%{nome}%",))

            else:
                sql = """
                    SELECT id_usuario, nome_usuario, registro, cpf
                    FROM usuario
                    WHERE registro = %s
                """
                cursor.execute(sql, (ra,))

            resultados = cursor.fetchall()

            if not resultados:
                QtWidgets.QMessageBox.information(self, "Não encontrado", "Nenhum técnico encontrado.")
                return

            tabela = self.ui.tabela_tecnicos
            tabela.setRowCount(0)
            tabela.setColumnCount(4)

            headers = ["ID", "Nome", "RA", "CPF"]
            tabela.setHorizontalHeaderLabels(headers)

            for row_data in resultados:
                row = tabela.rowCount()
                tabela.insertRow(row)
                for col, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value) if value else "")
                    tabela.setItem(row, col, item)

            tabela.resizeColumnsToContents()
            QtWidgets.QMessageBox.information(
                self,
                "Sucesso",
                f"Encontrado(s) {len(resultados)} técnico(s)."
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao buscar: {str(e)}")
            print("Erro:", e)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()


    def limpar_campos_tec(self):
        """Limpa os campos e a tabela de técnicos"""
        if hasattr(self.ui, 'campo_nome_tec'):
            self.ui.campo_nome_tec.clear()

        if hasattr(self.ui, 'campo_ra_tec'):
            self.ui.campo_ra_tec.clear()

        if hasattr(self.ui, 'tabela_tecnicos'):
            self.ui.tabela_tecnicos.setRowCount(0)

        QtWidgets.QMessageBox.information(self, "Limpo", "Campos e tabela foram limpos.")


    def excluir_usuario_tec(self):
        """Exclui o técnico selecionado na tabela"""
        tabela = self.ui.tabela_tecnicos
        current_row = tabela.currentRow()

        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Selecione um técnico para excluir.")
            return

        id_item = tabela.item(current_row, 0)
        nome_item = tabela.item(current_row, 1)

        if not id_item or not id_item.text():
            QtWidgets.QMessageBox.warning(self, "Erro", "Não foi possível obter o ID.")
            return

        id_usuario = id_item.text()
        nome = nome_item.text() if nome_item else ""

        resposta = QtWidgets.QMessageBox.question(
            self,
            "Confirmar Exclusão",
            f"Excluir o técnico {nome} (ID: {id_usuario})?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if resposta != QtWidgets.QMessageBox.Yes:
            return

        conexao = None
        cursor = None

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            sql = "DELETE FROM usuarios WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            conexao.commit()

            if cursor.rowcount > 0:
                tabela.removeRow(current_row)
                QtWidgets.QMessageBox.information(self, "Sucesso", "Técnico excluído!")
            else:
                QtWidgets.QMessageBox.warning(self, "Erro", "Não foi possível excluir.")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro: {str(e)}")

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def carregar_tecnicos_conta(self):
        """Carrega todos os técnicos na tabela da conta"""
        conexao = None
        cursor = None

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="Pedro",
                password="",
                port="3306",
                database="homologacao"
            )
            cursor = conexao.cursor()

            sql = """
                SELECT id_usuario, nome_usuario, registro, cpf
                FROM usuario
                ORDER BY nome_usuario
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()

            tabela = self.ui.tabela_tec_conta
            tabela.setRowCount(0)
            tabela.setColumnCount(4)

            headers = ["ID", "Usuário", "RA", "CPF"]
            tabela.setHorizontalHeaderLabels(headers)

            for row_data in resultados:
                row = tabela.rowCount()
                tabela.insertRow(row)
                for col, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value) if value else "")
                    tabela.setItem(row, col, item)

            # Configurar tabela para ocupar 100% do espaço
            header = tabela.horizontalHeader()
            header.setStretchLastSection(True)
            
            # Ajustar a primeira coluna também
            tabela.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Erro",
                f"Erro ao carregar técnicos:\n{str(e)}"
            )
            print("Erro:", e)

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def criar_grafico_atividade(self):

        self.ui.grafico_placeholder.setStyleSheet("background: red;")

        plot = pg.PlotWidget()
        plot.setBackground('#0f172a')  # fundo dark igual seus cards

        plot.showGrid(x=False, y=False)
        plot.showAxis('right', False)   
        plot.showAxis('top', False)

        plot.getAxis('left').setPen(pg.mkPen('#94a3b8'))
        plot.getAxis('bottom').setPen(pg.mkPen('#94a3b8'))

        plot.setBackground('w')
        plot.enableAutoRange(False)
        plot.setXRange(1, 5)
        plot.setYRange(0, 50)

        dias = np.array([1, 2, 3, 4, 5])
        valores = np.array([10, 30, 20, 40, 25])

        # spline cúbica
        x_smooth = np.linspace(dias.min(), dias.max(), 300)
        y_smooth = make_interp_spline(dias, valores, k=3)(x_smooth)

        pen = pg.mkPen(color='#38bdf8', width=3)  # azul moderno

        linha = plot.plot(
            x_smooth,
            y_smooth,
            pen=pen
        )

        fill = pg.FillBetweenItem(
            linha,
            pg.PlotDataItem(x_smooth, np.zeros(len(x_smooth))),
            brush=(101, 68, 200)  # roxo com transparência
        )

        plot.addItem(fill)



        # 👇 TUDO ISSO TEM QUE FICAR DENTRO DA FUNÇÃO
        layout = self.ui.grafico_placeholder.layout()

        if layout is None:
            layout = QVBoxLayout(self.ui.grafico_placeholder)
            layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(plot)

    
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################
 
        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##
        
        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Bem Cuidar')
        UIFunctions.labelTitle(self, 'Bem Cuidar')
        UIFunctions.labelDescription(self, ' ')
        ## ==> END ##
 
        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##
 
        ## ==> CREATE MENUS
        ########################################################################
 
        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##
 
        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        #abbr hover mouse
        UIFunctions.addNewMenu(self, u"Início", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, u"Homologação", "btn_info_paciente", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, u"Busca de Técnico", "btn_new_user", "url(:/16x16/icons/16x16/cil-user.png)", True)
        UIFunctions.addNewMenu(self, u"Busca Do Paciente", "btn_dados_paciente", "url(:/16x16/icons/16x16/cil-clipboard.png)", True)
        UIFunctions.addNewMenu(self, u"Conta", "btn_widgets", "url(:/16x16/icons/16x16/cil-user.png)", False)
       
        ## ==> END ##
 
        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##,
        
 
        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
   
        ## ==> END ##
 
     
 
 
        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
 
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
 
        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##
 
        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##
 
        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################
 
 
 
 
        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################
 
 
 
        ## ==> QTableWidget RARAMETERS
        ########################################################################
        
        ## ==> END ##
 
 
 
        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################
 
 
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
 
    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()
 
        # PAGINA INICIO
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Dashboard")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
 
        # PAGINA NOVO USUARIO
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.adicionar_usuario)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "Consulta De Usuários")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
 
        #PAGINA DE RELATORIOS
        if btnWidget.objectName() == "btn_info_paciente":
            self.ui.stackedWidget.setCurrentWidget(self.ui.info_paciente)
            UIFunctions.resetStyle(self, "btn_info_paciente")
            UIFunctions.labelPage(self, "Prontuário do Paciente")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        #PAGINA DE DADOS DO PACIENTE
        if btnWidget.objectName() == "btn_dados_paciente":
            self.ui.stackedWidget.setCurrentWidget(self.ui.dados_paciente)
            UIFunctions.resetStyle(self, "btn_dados_paciente")
            UIFunctions.labelPage(self, "Consulta De Pacientes")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGINA CONTA
        if btnWidget.objectName() == "btn_widgets":
            print("Botão da conta clicado")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            self.ui.page_widgets.update()
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Gerenciar Conta")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

            # Atualizar labels com nome do usuário e RA
            print(f"Atualizando labels para usuário: {self.usuario}")
            self.ui.label_usuario_conta.setText(f"Técnico(a): {self.usuario}")
            self.ui.label_ra_conta.setText(f"{self.ra}")
            
            # Carregar técnicos na tabela da conta
            self.carregar_tecnicos_conta()
 
    ## ==> END ##
 
    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################
 
    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##
 
    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.MouseButton.LeftButton:
            print('Mouse click: LEFT CLICK')
        elif event.buttons() == Qt.MouseButton.RightButton:
            print('Mouse click: RIGHT CLICK')
        elif event.buttons() == Qt.MouseButton.MiddleButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##
 
    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##
 
    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)
 
    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##
 
    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################
 
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    
    login = LoginWindow()
    login.show()

    sys.exit(app.exec())
