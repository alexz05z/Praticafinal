from flask import Flask , render_template
from datetime import date

app = Flask(__name__)

@app.route('/dashboard')
def tienda():

    nombre_admin = "Francisco"
    tienda = "TecnoMarket"
    fecha = date.today()


    productos = [
        {"nombre": "Placa Asus", "precio": 300.0, "stock": 2, "categoria": "Componentes"},
        {"nombre": "Raton Stellseries", "precio": 15.0, "stock": 5, "categoria": "Accesorios"},
        {"nombre": "Monitor Asus", "precio": 249.99, "stock": 0, "categoria": "Pantallas"},
        {"nombre": "Teclado Ozono", "precio": 65.0, "stock": 20, "categoria": "Accesorios"}
    ]
    clientes = [
        {"nombre": "Alejandro Rodriguez", "email": "alexfraleda@correo.com", "activo": True, "pedidos": 10},
        {"nombre": "Pepe Sanchez", "email": "pepe@correo.com", "activo": False, "pedidos": 1},
        {"nombre": "Manolo Gomez", "email": "manolo@correo.com", "activo": True, "pedidos": 50}
    ]
    pedidos = [
        {"cliente": "Alejandro Rodriguez", "total": 3600.0, "fecha": "2025-05-01"},
        {"cliente": "Pepe Sanchez", "total": 15.5, "fecha": "2025-05-03"},
        {"cliente": "Manolo Gomez", "total": 5000.0, "fecha": "2025-05-04"}
    ]

    total_stock = 0
    for producto in productos:
        total_stock += producto["stock"]

    clientes_activos = 0
    for cliente in clientes:
        if cliente["activo"]:
            clientes_activos += 1

    cliente_pedido = clientes[0]
    for cliente in clientes:
        if cliente["pedidos"] > cliente_pedido["pedidos"]:
            cliente_pedido = cliente


    total = 0
    for pedido in pedidos:
        total += pedido["total"]


    return render_template("dashboard.html",nombre_admin=nombre_admin,tienda=tienda,fecha=fecha,productos=productos,clientes=clientes,pedidos=pedidos,total_stock=total_stock,clientes_activos=clientes_activos,cliente_pedido=cliente_pedido,total=total)

if __name__ == '__main__':
    app.run()