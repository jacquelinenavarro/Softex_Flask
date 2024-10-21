from flask import Blueprint, request, jsonify
from models import db, Produto

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.json
    novo_produto = Produto(produto_nome = data['produto_nome'],produto_preco = data['produto_preco'] )
    db.session.add(novo_produto)
    db.session.commit()
    
    return jsonify({'id':novo_produto.produto_id, 'nome':novo_produto.produto_nome}), 201

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id':p.produto_id, 'nome':p.produto_nome, 'preco':p.produto_preco}for p in produtos]), 200

@produto_bp.route('/produtos/<int:id>',methods=['PUT'])
def atualizar_produto(id):
    data = request.json
    produto = Produto.query.get(id)
    
    if not produto:
        return jsonify({'message':'Produto não encontrado'}), 404
    
    produto.nome = data['produto_nome']
    db.session.commit()
    return jsonify ({'id':produto.produto_id, 'nome': produto.produto_nome, 'preco':produto.produto_preco}), 200

@produto_bp.route('/produtos/<int:id>',methods=['DELETE'])
def deletar_produto(id):
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({'message':'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return jsonify ({'message':'Produto detelado com sucesso'}), 200


    