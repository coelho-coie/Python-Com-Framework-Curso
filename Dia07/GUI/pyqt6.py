import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QAction

# --- Funções (Slots) ---
def abrir_arquivo():
    caminho, _ = QFileDialog.getOpenFileName(janela, "Abrir Arquivo", "", "Arquivos de Texto (*.txt)")
    if caminho:
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                editor.setText(f.read())
        except Exception as e:
            QMessageBox.critical(janela, "Erro", f"Não foi possível abrir o arquivo: {e}")

def salvar_arquivo():
    caminho, _ = QFileDialog.getSaveFileName(janela, "Salvar Arquivo Como", "", "Arquivos de Texto (*.txt)")
    if caminho:
        try:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(editor.toPlainText())
        except Exception as e:
            QMessageBox.critical(janela, "Erro", f"Não foi possível salvar o arquivo: {e}")

# --- Interface ---
app = QApplication(sys.argv)
# Usamos QMainWindow pois ela já vem com suporte a menus, barras de status, etc.
janela = QMainWindow()
janela.setWindowTitle("Editor de Texto")
janela.setGeometry(100, 100, 800, 600)

# Widget central de texto
editor = QTextEdit()
janela.setCentralWidget(editor)

# Barra de menus
menu_bar = janela.menuBar()
menu_arquivo = menu_bar.addMenu("Arquivo")

# Ações do menu
acao_abrir = QAction("Abrir...", janela)
acao_abrir.triggered.connect(abrir_arquivo)
menu_arquivo.addAction(acao_abrir)

acao_salvar = QAction("Salvar Como...", janela)
acao_salvar.triggered.connect(salvar_arquivo)
menu_arquivo.addAction(acao_salvar)

menu_arquivo.addSeparator()

acao_sair = QAction("Sair", janela)
acao_sair.triggered.connect(janela.close)
menu_arquivo.addAction(acao_sair)

janela.show()
sys.exit(app.exec())