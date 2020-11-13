import pandas as pd
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

datos={"Pelicula":["Avengers End Game","Avatar","Titanic","Star Wars Episodio VII","Avengers Infinity War"], "Recaudacion": [2797,2787,2187,2068,2048]}
df=pd.DataFrame(datos)

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("graficosM.ui",self)
        self.Boton_Seleccionar.clicked.connect(self.obtenerObjeto)
        self.Boton_Guardar.clicked.connect(self.guardarCsv)

    def obtenerObjeto(self):
        item=self.Opcion_Graficos.currentText()
        if item=="Grafica Barras Horizontal":
            df.groupby('Pelicula')['Recaudacion'].sum().plot(kind='barh', legend='Reverse', color="purple")
            plt.xlabel("Recaudacion (En millones)")
            plt.ylabel("Pelicula")
            plt.title("Peliculas mas taquilleras")
            self.label_Comentario.setText(f"Seleccionaste la {item}")
            plt.show()
        elif item=="Grafica Barras Vertical":
            df.groupby('Pelicula')['Recaudacion'].sum().plot(kind='bar', legend='Reverse', color="green")
            plt.xlabel("Pelicula")
            plt.ylabel("Recaudacion (En millones)")
            plt.title("Peliculas mas taquilleras")
            self.label_Comentario.setText(f"Seleccionaste la {item}")
            plt.show()
        elif item=="Grafica Lineas":
            df.groupby('Pelicula')['Recaudacion'].sum().plot(kind='line', legend='Reverse', color="black")
            plt.xlabel("Pelicula")
            plt.ylabel("Recaudacion (En millones)")
            plt.title("Peliculas mas taquilleras")
            self.label_Comentario.setText(f"Seleccionaste la {item}")
            plt.show()
        elif item=="Grafica Pastel":
            df.groupby('Pelicula')['Recaudacion'].sum().plot(kind='pie', explode=(0,0.2,0,0,0), autopct="%0.1f %%")
            plt.xlabel("")
            plt.ylabel("")
            plt.title("Peliculas mas taquilleras")
            self.label_Comentario.setText(f"Seleccionaste la {item}")
            plt.show()
        else:
            self.label_Comentario.setText(str(df))
    def guardarCsv(self):
        df.to_csv('evidencia_PIA.csv',index=True, header=True)
        self.label_Comentario.setText("La información se ha guardado en un csv.")

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()