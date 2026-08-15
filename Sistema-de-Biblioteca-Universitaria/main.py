# main.py
from controllers.usuario_controller import UsuarioController
from controllers.auth_controller import AuthController
from controllers.livro_controller import LivroController
from controllers.emprestimo_controller import EmprestimoController

def carregar_dados_iniciais():
    """Função Seed: Insere livros iniciais para podermos testar a aplicação"""
    LivroController.cadastrar_livro("Clean Code", "Robert C. Martin", 2008, "Tecnologia", "978-85", "12/08/2026", 150.00)
    LivroController.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia", "978-00", "10/08/2026", 120.00)
    LivroController.cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, "Literatura Brasileira", "978-850", "01/08/2026", 45.00)
    LivroController.cadastrar_livro("1984", "George Orwell", 1949, "Distopia", "978-014", "15/08/2026", 60.00)
    LivroController.cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", "978-015", "20/08/2026", 35.00)
    LivroController.cadastrar_livro("A Revolução dos Bichos", "George Orwell", 1945, "Fábula Política", "978-019", "25/08/2026", 50.00)
    LivroController.cadastrar_livro("O Código Da Vinci", "Dan Brown", 2003, "Suspense", "978-030", "30/08/2026", 80.00)
    LivroController.cadastrar_livro("A Menina que Roubava Livros", "Markus Zusak", 2005, "Ficção Histórica", "978-037", "05/09/2026", 70.00)
    LivroController.cadastrar_livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia", "978-026", "10/09/2026", 90.00)
    LivroController.cadastrar_livro("O Alquimista", "Paulo Coelho", 1988, "Ficção", "978-006", "15/09/2026", 55.00)
    LivroController.cadastrar_livro("A Guerra dos Tronos", "George R.R. Martin", 1996, "Fantasia Épica", "978-055", "20/09/2026", 200.00)
    LivroController.cadastrar_livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, "Romance Gótico", "978-014", "25/09/2026", 65.00)
    LivroController.cadastrar_livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925, "Romance", "978-074", "30/09/2026", 75.00)
    LivroController.cadastrar_livro("A Cabana", "William P. Young", 2007, "Ficção", "978-031", "05/10/2026", 85.00)
    LivroController.cadastrar_livro("O Diário de Anne Frank", "Anne Frank", 1947, "Memórias", "978-055", "10/10/2026", 40.00)
    LivroController.cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", "978-015", "15/10/2026", 35.00)
    LivroController.cadastrar_livro("O Código Da Vinci", "Dan Brown", 2003, "Suspense", "978-030", "20/10/2026", 80.00)

def menu_logado(usuario_logado):
    """Interface para quando o usuário está autenticado no sistema"""
    while True:
        print(f"\n--- Painel do Aluno: {usuario_logado.nome} ---")
        print("1. Buscar Obras")
        print("2. Listar Livros Disponíveis")
        print("3. Realizar Empréstimo")
        print("4. Devolver Livro")
        print("5. Meus Empréstimos")
        print("0. Fazer Logout")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            termo = input("Digite o título ou autor: ")
            resultados = LivroController.buscar_obra(termo)
            if resultados:
                print("\n--- Resultados da Busca ---")
                for livro in resultados:
                    print(livro)
            else:
                print("\nNenhuma obra encontrada.")
                
        elif opcao == '2':
            disponiveis = LivroController.listar_disponiveis()
            if disponiveis:
                print("\n--- Livros Disponíveis ---")
                for livro in disponiveis:
                    print(livro)
            else:
                print("\nNenhum livro disponível no momento.")
                
        elif opcao == '3':
            titulo_busca = input("Digite o título EXATO do livro que deseja pegar: ")
            resultados = LivroController.buscar_obra(titulo_busca)
            if resultados and resultados[0].disponivel:
                data_hoje = input("Informe a data de hoje (DD/MM/AAAA): ") 
                sucesso, msg = EmprestimoController.realizar_emprestimo(usuario_logado, resultados[0], data_hoje)
                print(f"\n{msg}")
            else:
                print("\nLivro não encontrado ou já está emprestado.")
                
        elif opcao == '4':
            meus_emprestimos = EmprestimoController.listar_emprestimos_usuario(usuario_logado)
            # Filtra apenas os empréstimos que ainda não foram devolvidos
            ativos = [emp for emp in meus_emprestimos if not emp.data_devolucao_real]
            
            if ativos:
                print("\n--- Seus Empréstimos Ativos ---")
                for i, emp in enumerate(ativos):
                    print(f"[{i}] {emp.livro.titulo} (Devolução prevista: {emp.data_devolucao_prevista.strftime('%d/%m/%Y')})")
                
                try:
                    escolha = int(input("Digite o NÚMERO correspondente ao empréstimo que deseja devolver: "))
                    if 0 <= escolha < len(ativos):
                        data_devolucao = input("Digite a data de devolução (DD/MM/AAAA): ")
                        sucesso, msg = EmprestimoController.realizar_devolucao(ativos[escolha], data_devolucao)
                        print(f"\n{msg}")
                    else:
                        print("\nOpção inválida.")
                except ValueError:
                    print("\nPor favor, digite apenas números.")
            else:
                print("\nVocê não possui empréstimos pendentes de devolução.")
                
        elif opcao == '5':
            meus_emprestimos = EmprestimoController.listar_emprestimos_usuario(usuario_logado)
            if meus_emprestimos:
                print("\n--- Histórico de Empréstimos ---")
                for emp in meus_emprestimos:
                    status = "Devolvido" if emp.data_devolucao_real else "Ativo"
                    print(f"- {emp.livro.titulo} | Status: {status}")
            else:
                print("\nVocê ainda não realizou nenhum empréstimo.")
                
        elif opcao == '0':
            print("\nSaindo da sua conta...")
            break
        else:
            print("\nOpção inválida, tente novamente.")

def main():
    """Menu principal do sistema (Visitante)"""
    carregar_dados_iniciais()
    
    while True:
        print("\n" + "="*40)
        print("🎓 SISTEMA DE BIBLIOTECA UNIVERSITÁRIA")
        print("="*40)
        print("1. Cadastrar novo usuário")
        print("2. Fazer Login")
        print("0. Encerrar sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n--- Novo Cadastro ---")
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            email = input("E-mail: ")
            idade = input("Idade: ")
            numeroTel = input("Telefone: ")
            senha = input("Senha: ")
            sucesso, msg = UsuarioController.cadastrar_usuario(nome, matricula, email, idade, numeroTel, senha)
            print(f"\n{msg}")
            
        elif opcao == '2':
            print("\n--- Acesso ao Sistema ---")
            email = input("E-mail: ")
            senha = input("Senha: ")
            sucesso, resultado = AuthController.login(email, senha)
            
            if sucesso:
                print("\nLogin efetuado com sucesso!")
                # Chama o menu secundário passando o usuário logado
                menu_logado(resultado) 
            else:
                print(f"\n{resultado}") 
                
        elif opcao == '0':
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida, tente novamente.")

# Garante que o script só rode se for chamado diretamente
if __name__ == "__main__":
    main()