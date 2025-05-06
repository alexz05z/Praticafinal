from flask import Flask , render_template
from datetime import date

app = Flask(__name__)

@app.route('/dashboard')
def tienda():

    nombre_admin = "Francisco"
    tienda = "TecnoMarket"
    fecha = date.today()


    producto = {
        "nombre": "ratón inalámbrico",
        "descripcion": "Dispositivo ergonómico con conexión Bluetooth",
        "precio": 19.99
    }
    return render_template("producto.html", producto=producto)

if __name__ == '__main__':
    app.run()