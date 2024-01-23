from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
    Módulo que faz a inicialização da conexão do banco com o SQLAlchemy e criação de tabelas
"""
def init_app(app):
    """
        Função que inicializa a conexão do banco com o SQLAlchemy e criação de tabelas
    """
    db.init_app(app)

    #Criação tabelas
    with app.app_context():
        #Tabelas a serem criadas
        db.create_all()
