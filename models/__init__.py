#from .produto import db, Produto
from flask_sqlalchemy import SQLAlchemy

#Cria instancia do QLAlchemy
db = SQLAlchemy()

#Importa os modelos (Produto e Usuário) após a criação do bd
from . produto import Produto
from . usuario import Usuario