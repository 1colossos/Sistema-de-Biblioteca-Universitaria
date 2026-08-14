
class Usuario:
    def __init__(self, nome, matricula, email, idade, numeroTel, senha):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.idade = idade
        self.numeroTel = numeroTel
        self.senha = senha  # Em um sistema real, a senha deve ser criptografada (hash)
        
    def __str__(self):
        return f"Usuário: {self.nome} (Matrícula: {self.matricula})" f"Email: {self.email} (Idade: {self.idade}) (Número de Telefone: {self.numeroTel}) (Senha: {self.senha})"