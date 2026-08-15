# 🎓 Sistema de Biblioteca Universitária

Este é um sistema de linha de comando desenvolvido em Python para gerenciar o acervo e os empréstimos de uma biblioteca universitária[cite: 10]. O projeto foi construído utilizando os princípios da arquitetura MVC (Model, View, Controller) e utiliza o armazenamento em memória para simular um banco de dados[cite: 10].

### Contexto Acadêmico
Este projeto é fruto de uma atividade prática desenvolvida para a disciplina de Desenvolvimento Ágil de Sistemas, no curso de Análise de Sistemas da Universidade Estadual do Maranhão (UEMA)[cite: 10]. A metodologia de desenvolvimento é baseada no framework Scrum, contemplando os papéis fundamentais de Scrum Master, Product Owner (PO) e Dev Team.

---

## 🚀 Funcionalidades

O sistema foi estruturado em duas áreas principais: o menu de visitante (deslogado) e o Painel do Aluno (logado)[cite: 6, 10].

### Gestão de Usuários e Autenticação
* O sistema permite o cadastro de novos usuários solicitando informações como nome, matrícula, e-mail, idade, telefone e senha[cite: 4, 6, 9, 10].
* Existe uma validação de negócio que impede a criação de contas com matrículas ou e-mails já existentes no sistema[cite: 4, 10].
* Os usuários cadastrados podem fazer login na plataforma informando seu e-mail e senha[cite: 1, 6, 10]. 
* O processo de autenticação verifica os dados e retorna sucesso ou mensagens de erro detalhadas em caso de e-mail não encontrado ou senha incorreta[cite: 1].

### Gestão do Acervo (Livros)
* O sistema é inicializado automaticamente com diversos livros base para facilitar os testes, incluindo clássicos como "Clean Code", "O Senhor dos Anéis" e "Dom Casmurro"[cite: 6, 10].
* Os livros no acervo possuem os atributos de título, autor, ano de publicação, gênero, ISBN, data de aquisição e preço[cite: 8, 10].
* É possível realizar buscas por obras específicas no acervo digitando o título ou o autor da obra[cite: 3, 6, 10]. 
* O algoritmo de busca foi projetado para ignorar diferenças entre letras maiúsculas e minúsculas[cite: 3, 10].
* O usuário logado pode visualizar uma lista filtrada contendo apenas os livros que estão atualmente disponíveis para empréstimo[cite: 3, 6, 10].

### Empréstimos e Devoluções
* Um aluno autenticado pode realizar o empréstimo de um exemplar buscando pelo título exato do livro[cite: 6, 10].
* Ao registrar um empréstimo, o prazo de devolução é estabelecido e calculado automaticamente com um limite de 7 dias[cite: 7, 10].
* Quando o empréstimo é concluído, o status de disponibilidade do livro é alterado para indisponível (bloqueado)[cite: 2, 7, 10].
* O sistema permite registrar a devolução de livros informando a data real de entrega, liberando a obra novamente para o catálogo[cite: 2, 7, 10].
* Existe uma lógica de multa por atraso incorporada, cobrando um valor fixo de R$ 2,50 por cada dia que exceder o prazo de devolução original[cite: 7, 10].
* Os alunos têm acesso a um painel para visualizar o seu histórico de empréstimos[cite: 6, 10]. 
* Este histórico separa claramente os empréstimos ativos (pendentes) daqueles que já foram devolvidos[cite: 6, 10].

---

## 📂 Estrutura do Projeto (Arquitetura MVC)

O código-fonte está modularizado para separar responsabilidades, seguindo o padrão MVC:

* **`models/`**: Este diretório representa as entidades centrais do sistema, contendo as declarações das classes `Usuario`, `Livro` e `Emprestimo`[cite: 10].
* **`controllers/`**: Esta camada é responsável por processar e validar toda a regra de negócio da aplicação[cite: 10].
  * O arquivo `usuario_controller.py` gerencia a criação e validação de novas contas de usuário[cite: 4, 10].
  * O arquivo `auth_controller.py` é responsável pela rotina de verificação de credenciais para efetuar o login[cite: 1, 10].
  * O arquivo `livro_controller.py` manipula as operações de catálogo e os algoritmos de busca de obras[cite: 3, 10].
  * O arquivo `emprestimo_controller.py` conduz o fluxo de retirada e devolução de exemplares pelos usuários[cite: 2, 10].
* **`database/`**: Este diretório contém o arquivo `db.py`, que simula tabelas de banco de dados armazenando listas globais (`usuarios_db`, `livros_db` e `emprestimos_db`) em tempo de execução[cite: 5, 10].
* **`main.py`**: Este módulo atua como a camada de visualização (View) principal[cite: 10]. Ele exibe as interfaces, menus interativos de linha de comando e processa as escolhas do visitante ou aluno logado[cite: 6, 10].

---

## ⚙️ Como Executar

Para iniciar a simulação do sistema na sua máquina, certifique-se de ter o Python instalado e execute o seguinte comando no diretório raiz do projeto[cite: 10]:

```bash
python main.py