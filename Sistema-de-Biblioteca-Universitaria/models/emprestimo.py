# models/emprestimo.py
from datetime import datetime, date, timedelta

class Emprestimo:
    TAXA_MULTA_DIARIA = 2.50  # R$ 2,50 por dia de atraso

    def __init__(self, usuario, livro, data_emprestimo_str, dias_prazo=7):
        self.usuario = usuario
        self.livro = livro
        
        # Converte a string de empréstimo para data
        self.data_emprestimo = datetime.strptime(data_emprestimo_str, "%d/%m/%Y").date()
        
        # Calcula a data prevista somando os dias de prazo
        self.data_devolucao_prevista = self.data_emprestimo + timedelta(days=dias_prazo)
        self.data_devolucao_real = None # Começa vazio, pois ainda não devolveu
        
        self.livro.disponivel = False # Bloqueia o livro

    def registrar_devolucao(self, data_devolucao_str):
        """Registra a entrega do livro e libera ele para outro aluno"""
        self.data_devolucao_real = datetime.strptime(data_devolucao_str, "%d/%m/%Y").date()
        self.livro.disponivel = True

    def calcular_multa(self):
        """Calcula o valor da multa se houver atraso"""
        # Se o livro já foi devolvido, calculamos com base no dia que ele entregou
        if self.data_devolucao_real:
            data_base = self.data_devolucao_real
        else:
            # Se ainda não devolveu, calculamos a multa até o dia de HOJE
            data_base = date.today()

        # Verifica se passou do prazo
        if data_base > self.data_devolucao_prevista:
            dias_atraso = (data_base - self.data_devolucao_prevista).days
            return dias_atraso * self.TAXA_MULTA_DIARIA
        
        return 0.0 # Sem multa, entregou no prazo!