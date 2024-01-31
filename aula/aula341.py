from PySide6.QtWidgets import QApplication, QPushButton
import sys
app = QApplication(sys.argv)

botao =  QPushButton('texto botao')
botao.setStyleSheet('font-size: 40px; color: red ;') # css dentro do argumento botao
botao.show() #  Adiciona o widget na hierarqui e exibe a janela

botao2 =  QPushButton('texto botao')
botao2.show() 

app.exec() # O loop da aplicacção