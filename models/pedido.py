from . import db

class Pedido(db.Model):
    __tablenME__= "pedidos"
    
    produto_id = db.column(db.integer, primary_key=True)
    