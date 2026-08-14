# controllers/usuario_controller.py
from models.usuario import Usuario
from database.db import usuarios_db

class UsuarioController:
    
    @staticmethod
    def cadastrar_usuario(nome, matricula, email, idade, numeroTel, senha): # <-- idade aqui
        for usuario in usuarios_db:
            if usuario.matricula == matricula:
                return False, "Erro: Matrícula já cadastrada no sistema."
            if usuario.email == email:
                return False, "Erro: E-mail já cadastrado no sistema."
        
        # Passando a idade na posição correta
        novo_usuario = Usuario(nome, matricula, email, idade, numeroTel, senha) 
        usuarios_db.append(novo_usuario)
        
        return True, f"Usuário {nome} cadastrado com sucesso!"