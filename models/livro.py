# models/livro.py
from datetime import datetime

class Livro: 
    def __init__(self, titulo, autor, ano_publicacao, genero, isbn, data_aquisicao_str, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.isbn = isbn
        self.preco = preco
        self.disponivel = True
        
        # Converte a string "DD/MM/AAAA" para um formato de data matemático
        self.data_aquisicao = datetime.strptime(data_aquisicao_str, "%d/%m/%Y").date()

    def __str__(self):
        return f"Livro: {self.titulo} (Adquirido em {self.data_aquisicao.strftime('%d/%m/%Y')})"
        