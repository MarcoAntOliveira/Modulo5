from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

import sys
app = QApplication(sys.argv)

botao =  QPushButton('texto botao')
botao.setStyleSheet('font-size: 40px; color: red ;') # css dentro do argumento botao
botao.show() #  Adiciona o widget na hierarqui e exibe a janela

botao2 =  QPushButton('texto botao')
botao2.show() 

botao3 =  QPushButton('texto botao')
botao3.show() 

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao3, 1, 2, 1, 1)
layout.addWidget(botao2, 3, 1, 1, 2)
central_widget.show()# entra hierarquia e mpostre sua janela


app.exec() # O loop da aplicacção