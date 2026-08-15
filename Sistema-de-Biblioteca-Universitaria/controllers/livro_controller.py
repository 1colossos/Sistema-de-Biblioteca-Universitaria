from models.livro import Livro
from database.db import livros_db

class LivroController:
    
    @staticmethod
    def cadastrar_livro(titulo, autor, ano_publicacao, genero, isbn, data_aquisicao_str, preco):
        novo_livro = Livro(titulo, autor, ano_publicacao, genero, isbn, data_aquisicao_str, preco)
        livros_db.append(novo_livro)
        return True, f"Livro '{titulo}' cadastrado no acervo!"

    @staticmethod
    def listar_disponiveis():
        """Retorna apenas os livros que não estão emprestados (História 6)"""
        disponiveis = [livro for livro in livros_db if livro.disponivel]
        return disponiveis

    @staticmethod
    def buscar_obra(termo_busca):
        """Busca livros por título ou autor ignorando maiúsculas/minúsculas (História 3)"""
        resultados = []
        termo = termo_busca.lower()
        
        for livro in livros_db:
            if termo in livro.titulo.lower() or termo in livro.autor.lower():
                resultados.append(livro)
                
        return resultados