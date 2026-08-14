from database.db import usuarios_db

class AuthController:
    
    @staticmethod
    def login(email, senha): # <-- Atenção aqui: 'login' todo em minúsculo
        """
        Verifica se as credenciais batem com algum usuário no banco.
        Retorna (True, Usuario) em caso de sucesso ou (False, mensagem_erro) em caso de falha.
        """
        for usuario in usuarios_db:
            if usuario.email == email:
                if usuario.senha == senha:
                    return True, usuario
                else:
                    return False, "Erro: Senha incorreta."
        
        return False, "Erro: E-mail não encontrado."