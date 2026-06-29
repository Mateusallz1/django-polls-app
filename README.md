# Django Polls App

Um aplicativo de enquetes desenvolvido em Python utilizando o framework Django, baseado no tutorial oficial da documentação do Django. Este projeto serve para consolidação de conceitos de arquitetura MVT, ORM, migrações e painel administrativo.

## 🚀 Tecnologias Utilizadas

* **Python 3.12+**
* **Django 5.x**
* **uv:** Gerenciador de pacotes e ambientes virtuais extremamente rápido.
* **SQLite:** Banco de dados em arquivo para ambiente de desenvolvimento.

---

## 🛠️ O que foi implementado até o momento

### Parte 1: Setup e Estrutura Inicial
* Inicialização do ambiente isolado e instalação do Django utilizando o `uv`.
* Criação da estrutura do projeto principal (`mysite`) e do aplicativo isolado (`polls`).
* Configuração do fluxo de requisição/resposta usando **Function-Based Views (FBV)** para o index do app.
* Configuração do sistema descentralizado de rotas utilizando `include()` no `urls.py` global.

### Parte 2: Modelos, Banco de Dados e Admin
* Configuração de localização do projeto para `pt-br` e fuso horário `America/Sao_Paulo`.
* Criação dos modelos de dados relacionais Muitos-para-Um (`Question` e `Choice`) em `polls/models.py`.
* Uso do sistema de migrações (`makemigrations` e `migrate`) para persistência estruturada no SQLite.
* Manipulação de dados, testes de relacionamentos reversos (`choice_set`) e consultas via Django Shell.
* Criação de superusuário e registro dos modelos para visualização no painel nativo do **Django Admin**.

---

## 💻 Como executar o projeto localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/django-polls-app.git](https://github.com/seu-usuario/django-polls-app.git)
    cd django-polls-app
    ```

2.  **Instale as dependências (necessário ter o `uv` instalado):**
    ```bash
    uv sync
    ```

3.  **Execute as migrações para preparar o banco de dados:**
    ```bash
    uv run python manage.py migrate
    ```

4.  **Inicie o servidor de desenvolvimento:**
    ```bash
    uv run python manage.py runserver
    ```

Acesse o projeto em `http://127.0.0.1:8000/polls/` ou o painel administrativo em `http://127.0.0.1:8000/admin/`.
