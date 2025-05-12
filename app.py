from flask import Flask , render_template , request , redirect, url_for
from datetime import date
from pymongo import MongoClient

app = Flask(__name__)

online = MongoClient("mongodb+srv://arodsan013a:T1L7WBu0UDrxvMtH@alexz.lqhssf7.mongodb.net/")

app.db = online.tienda

nombre_admin = "Francisco"
tienda = "TecnoMarket"
fecha = date.today()

@app.route('/')
def inicio():
    pagina = "indice"

    

    productos = [producto for producto in app.db.productos.find({})]

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


    return render_template("dashboard.html",nombre_admin=nombre_admin,tienda=tienda,fecha=fecha,productos=productos,clientes=clientes,pedidos=pedidos,clientes_activos=clientes_activos,cliente_pedido=cliente_pedido,total=total, pagina=pagina ,total_stock=total_stock)

@app.route("/productos", methods=["GET", "POST"])
def productos():
    productos = [producto for producto in app.db.productos.find({})]

    pagina = "productos"
    
    if request.method == "POST":
        formulario = request.form.get("tipo_formulario")
        if formulario == "agregar_productos":
            prod = {
                "nombre": request.form.get("product"),
                "precio": float(request.form.get("price")),
                "stock": int(request.form.get("stock")),
                "categoria": request.form.get("category")
            }
            app.db.productos.insert_one(prod)
            return redirect(url_for("productos"))
        
        elif formulario == "eliminar_productos":
            eliprod = request.form.get("elproduct")
            app.db.productos.delete_one({"nombre": eliprod})
            return redirect(url_for("productos"))
        
        elif formulario == "cambiar_stock":
            nombre_prod = request.form.get("prod_a_cambiar").strip()
            nuevo_stock = request.form.get("nuevo_stock")
            nuevo_precio = request.form.get("nuevo_precio")

            cambios = {}
            if nuevo_stock:
                cambios["stock"] = int(nuevo_stock)
            if nuevo_precio:
                cambios["precio"] = float(nuevo_precio)

            if cambios:
                app.db.productos.update_one({"nombre": nombre_prod}, {"$set": cambios})
            
            return redirect(url_for("productos"))


    return render_template("dashboard.html", 
                           nombre_admin=nombre_admin, 
                           tienda=tienda, 
                           fecha=fecha, 
                           productos=productos,pagina=pagina,
                           )
if __name__ == '__main__':
    app.run()