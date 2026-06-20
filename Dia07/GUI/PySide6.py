import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout

def sortear_nome():
    # .toPlainText() pega todo o texto do QTextEdit.
    texto_completo = campo_nomes.toPlainText()
    
    # .splitlines() divide o texto em uma lista, quebrando pelas linhas.
    # list comprehension para remover linhas vazias.
    nomes = [nome.strip() for nome in texto_completo.splitlines() if nome.strip()]
    
    if nomes:
        vencedor = random.choice(nomes)
        label_resultado.setText(f"🎉 O vencedor é: {vencedor} 🎉")
    else:
        label_resultado.setText("Nenhum nome na lista para sortear.")

# --- Interface ---
app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Sorteador de Nomes")
layout = QVBoxLayout()

# Widgets
label_instrucao = QLabel("Cole os nomes abaixo (um por linha):")
campo_nomes = QTextEdit()
botao_sortear = QPushButton("Sortear!")
label_resultado = QLabel("")
label_resultado.setStyleSheet("font-size: 16px; color: darkblue;")

# Conecta o botão
botao_sortear.clicked.connect(sortear_nome)

# Adiciona widgets ao layout
layout.addWidget(label_instrucao)
layout.addWidget(campo_nomes)
layout.addWidget(botao_sortear)
layout.addWidget(label_resultado)

janela.setLayout(layout)
janela.show()
sys.exit(app.exec())