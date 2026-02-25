class Style():

    style_main_window = """
    QMainWindow {
        background-color: white;
    }
    """

    style_bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(85, 170, 127);
        background-color: rgb(85, 170, 127);
        text-align: left;
        padding-left: 43px;
        font-weight: bold;
        font-size: 11pt;
        
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(85, 170, 127); /* Verde */
        border-left: 28px solid rgb(85, 170, 127);
        
    }
    QPushButton:pressed {
        background-color: rgb(69, 139, 103); /* Verde */
        border-left: 28px solid rgb(69, 139, 103);
    }
    """
    )


DARK_THEME = """
/* Base geral */
QWidget, QStackedWidget {
    background-color: #020617;
    color: #e5e7eb;
}

/* Labels (inclui logo) */
QLabel {
    color: #e5e7eb;
}

/* Frames */
QFrame {
    background-color: #020617;
}

/* Campos */
QLineEdit, QTextEdit, QComboBox {
    background-color: #020617;
    border: 1px solid #334155;
    color: #e5e7eb;
    padding: 6px;
}

/* Botões */
QPushButton {
    background-color: #0f172a;
    color: #e5e7eb;
    padding: 8px;
}

QPushButton:hover {
    background-color: #1e293b;
}

/* ===== TABELA BRANCA NO MODO ESCURO ===== */
QTableWidget {
    background-color: #ffffff;
    color: #020617;
    gridline-color: #cbd5e1;
    border: 1px solid #cbd5e1;
}

QHeaderView::section {
    background-color: #e5e7eb;
    color: #020617;
    border: 1px solid #cbd5e1;
}

QLabel#label_usuario,
QLabel#label_nome_paciente {
    color: #ffffff;
}


QGroupBox {
    background-color: #020617;
    color: #ffffff;
    border: 2px solid #334155;
}

QGroupBox::title {
    color: #e5e7eb;
}

QGroupBox QLabel {
    color: #e5e7eb;
}

QGroupBox QLineEdit,
QGroupBox QTextEdit,
QGroupBox QComboBox {
    background-color: #020617;
    color: #e5e7eb;
    border: 1px solid #334155;
}

/* =========================
   COMBOBOX – TEXTO VISÍVEL
   ========================= */
QComboBox {
    color: #e5e7eb;
}

QComboBox QAbstractItemView {
    background-color: #020617;
    color: #e5e7eb;
    selection-background-color: rgb(85, 170, 127);
    selection-color: #020617;
}

/* =========================
   DATE EDIT – TEXTO DA DATA
   ========================= */
QDateEdit {
    color: #e5e7eb;
}

/* =========================
   PLACEHOLDER
   ========================= */
QLineEdit::placeholder {
    color: #64748b;
}
"""




LIGHT_THEME = """
/* Base geral */
QWidget, QStackedWidget {
    background-color: #f8fafc;
    color: #020617;
}

/* Labels (inclui logo) */
QLabel {
    color: #020617;
}


/* Frames */
QFrame {
    background-color: #f8fafc;
}

/* Campos */
QLineEdit, QTextEdit, QComboBox {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    color: #020617;
    padding: 6px;
}

/* Botões */
QPushButton {
    background-color: #020617;
    color: #ffffff;
    padding: 8px;
}

QPushButton:hover {
    background-color: #334155;
}

/* ===== TABELA CLARA ===== */
QTableWidget {
    background-color: #ffffff;
    color: #020617;
    gridline-color: #cbd5e1;
    border: 1px solid #cbd5e1;
}

QHeaderView::section {
    background-color: #e5e7eb;
    color: #020617;
    border: 1px solid #cbd5e1;
}

QLabel#label_usuario,
QLabel#label_nome_paciente {
    color: #000000;
}


QGroupBox {
    background-color: #f8fafc;
    color: #020617;
    border: 2px solid #cbd5e1;
}

QGroupBox::title {
    color: #020617;
}

QGroupBox QLabel {
    color: #000000;
}

QGroupBox QLineEdit,
QGroupBox QTextEdit,
QGroupBox QComboBox {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #cbd5e1;
}

/* =========================
   COMBOBOX – TEXTO VISÍVEL
   ========================= */
QComboBox {
    color: #020617;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #020617;
    selection-background-color: rgb(85, 170, 127);
    selection-color: #ffffff;
}

/* =========================
   DATE EDIT – TEXTO DA DATA
   ========================= */
QDateEdit {
    color: #020617;
}

/* =========================
   PLACEHOLDER
   ========================= */
QLineEdit::placeholder {
    color: #94a3b8;
}


"""
