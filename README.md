# Sistema de Biblioteca Universitária 📚

Este é um sistema de linha de comando desenvolvido em Python para gerenciar o acervo e os empréstimos de uma biblioteca universitária. O projeto foi construído utilizando os princípios da arquitetura MVC (Model, View, Controller) e utiliza o armazenamento em memória para simular um banco de dados.

> **Contexto Acadêmico:**  
> Este projeto foi desenvolvido como trabalho prático para a disciplina de **Desenvolvimento Ágil** da **Universidade Estadual do Maranhão (UEMA)**. O objetivo principal do repositório é aplicar na prática os conceitos do framework Scrum (organização em Sprints, divisão de papéis e gestão de backlog) aliados a boas práticas de engenharia de software.

## 🚀 Funcionalidades

O sistema foi dividido em duas áreas principais: o Menu de Visitante e o Painel do Aluno.

### Gestão de Usuários e Autenticação
* O sistema permite o cadastro de novos usuários solicitando nome, matrícula, e-mail, idade, telefone e senha.
* Existe uma validação que impede o cadastro de matrículas ou e-mails já existentes no banco de dados.
* Os usuários podem fazer login no sistema informando e-mail e senha.

### Gestão de Acervo (Livros)
* O sistema é inicializado automaticamente com três livros base para testes: "Clean Code", "O Senhor dos Anéis" e "Dom Casmurro".
* Os livros possuem atributos detalhados, como título, autor, ano de publicação, gênero, ISBN, data de aquisição e preço.
* É possível buscar obras específicas no acervo digitando o título ou o autor, e a busca ignora diferenças entre letras maiúsculas e minúsculas.
* O usuário logado pode listar todos os livros que estão atualmente disponíveis para empréstimo.

### Empréstimos e Devoluções
* O aluno pode realizar o empréstimo de um livro buscando pelo título exato.
* Ao realizar um empréstimo, o prazo de devolução é calculado automaticamente com um limite de 7 dias.
* Quando um livro é emprestado, o seu status de disponibilidade é alterado para bloquear novos empréstimos do mesmo exemplar.
* O sistema registra a devolução de livros informando a data de entrega, liberando a obra de volta para o acervo.
* O sistema possui uma lógica de cálculo de multa por atraso, cobrando R$ 2,50 por cada dia excedido do prazo original.
* Os alunos podem visualizar o seu histórico completo de empréstimos, separando os empréstimos ativos dos já devolvidos.

## 📂 Estrutura do Projeto (MVC)

A arquitetura do código está dividida nos seguintes módulos:

* **`models/`**: Representa as entidades principais do sistema, contendo as classes `Usuario`, `Livro` e `Emprestimo`.
* **`controllers/`**: Responsável por toda a regra de negócio da aplicação.
  * O `UsuarioController` lida com as validações de criação de conta.
  * O `AuthController` é responsável por verificar as credenciais no momento do login.
  * O `LivroController` gerencia as buscas e o catálogo de obras.
  * O `EmprestimoController` processa as transações de retirada e devolução de livros.
* **`database/`**: Contém o arquivo `db.py`, que abriga as listas globais (`usuarios_db`, `livros_db` e `emprestimos_db`) para armazenar os dados em tempo de execução.
* **`main.py`**: Atua como a camada de visualização (View), providenciando as interfaces e menus interativos de linha de comando para o usuário.

## ⚙️ Como Executar

Para rodar o sistema na sua máquina localmente, clone o repositório e execute o arquivo principal a partir do seu terminal:

```bash
python main.py
