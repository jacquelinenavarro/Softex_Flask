from flask import Blueprint, request, jsonify
from models import db, Usuario

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    
    usuario = request.json
    novo_usuario = Usuario(usuario_login=usuario['usuario_login'],usuario_senha=usuario['usuario_senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    
    return jsonify({'id': novo_usuario.usuario_id,'nome': novo_usuario.usuario_login}), 201
    