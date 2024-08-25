"""
Created on Sun Jan 29 18:41:37 2023
pagina web en python 3.8.5
@author: Eliel
"""

from flask import Flask
from flask import render_template

#objeto app
app=Flask(__name__)

#crear una ruta /url
"""
@app.route('/')
def home():
    return "hola"
"""

#crear una ruta con html
@app.route('/')
def home():
    return render_template('home.html')

#crear otra ruta 
@app.route('/about')
def about():
    return render_template("about.html")

#iniciar el servidor 
if __name__ =='__main__':
    #app.run()
    #para que el servidor se reinicie todo el tiempo
    #permite ver los cambios al instante 
    app.run(debug=True)
