import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contadorPalabras)
    
    def ContarPalabras(self):
        #Recuperar el texto✅
        texto = self.edtCaracteres.text()
        #Separar las plabras✅
        palabras = texto.split()
        #Contar las palbras✅
        cantidadPalabras = len(palabras)
        #Contar los caracteres
        print("Se  ha presionado el botón...")

app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())