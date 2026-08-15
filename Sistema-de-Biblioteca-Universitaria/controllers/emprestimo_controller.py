from models.emprestimo import Emprestimo
from database.db import emprestimos_db

class EmprestimoController:
    
    @staticmethod
    def realizar_emprestimo(usuario, livro, data_emprestimo_str):
        # Regra de Negócio: Só pode emprestar se o livro estiver disponível
        if not livro.disponivel:
            return False, f"Erro: O livro '{livro.titulo}' já está emprestado."
        
        # Cria o empréstimo (o modelo já se encarrega de marcar o livro como indisponível)
        novo_emprestimo = Emprestimo(usuario, livro, data_emprestimo_str)
        
        # Salva o registro no nosso banco de dados em memória
        emprestimos_db.append(novo_emprestimo)
        
        data_prevista = novo_emprestimo.data_devolucao_prevista.strftime('%d/%m/%Y')
        return True, f"Empréstimo realizado com sucesso! Devolução prevista para: {data_prevista}"

    @staticmethod
    def realizar_devolucao(emprestimo, data_devolucao_str):
        # O modelo processa as datas e libera o livro novamente
        emprestimo.registrar_devolucao(data_devolucao_str)
        
        # Verifica se passou do prazo para aplicar a multa
        valor_multa = emprestimo.calcular_multa()
        
        mensagem = f"Devolução do livro '{emprestimo.livro.titulo}' realizada."
        if valor_multa > 0:
            mensagem += f" ATENÇÃO: Consta uma multa por atraso no valor de R$ {valor_multa:.2f}."
            
        return True, mensagem
        
    @staticmethod
    def listar_emprestimos_usuario(usuario):
        """Retorna todos os empréstimos (ativos ou devolvidos) de um usuário específico"""
        return [emp for emp in emprestimos_db if emp.usuario.matricula == usuario.matricula]