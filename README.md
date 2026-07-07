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

### Parte 3: URLs Dinâmicas, Templates e Atalhos
* Criação de templates HTML estruturados para listagem e exibição detalhada de perguntas.
* Uso estratégico do atalho `get_object_or_404()` para interceptar ausência de registros sem quebrar o desacoplamento das camadas do framework.
* Substituição de URLs fixas (*hardcoded*) nos arquivos de template pela tag dinâmica `{% url %}`.
* Configuração de espaço de nomes (*namespacing*) com a propriedade `app_name` no arquivo de rotas local para evitar conflito de escopos.

### Parte 4: Formulários e Lógica de Negócio (POST)
* Construção de formulários web interativos para recepção e processamento de votos.
* Implementação obrigatória da tag de segurança `{% csrf_token %}` nativa contra ataques do tipo Cross-Site Request Forgery.
* Tratamento explícito de exceções de requisições malformadas (`KeyError`) diretamente na view de voto.
* Aplicação rigorosa do padrão de arquitetura web **PRG (Post/Redirect/Get)** utilizando `HttpResponseRedirect` e `reverse` para mitigar o reenvio acidental de formulários por F5.

### Parte 5: Testes Automatizados de Integração
* Escrita de testes de ponta a ponta com a biblioteca padrão `TestCase` utilizando o cliente HTTP de simulação (`self.client`).
* Cobertura de cenários para fluxos válidos com redirecionamento correto e atualização do estado do banco via `refresh_from_db()`.
* Testagem estruturada de fluxos de exceção (voto em branco) validando o retorno de erro textual de forma estrita.

### Parte 7: Customização Avançada do Django Admin
* Customização aprofundada da interface do painel administrativo no arquivo `polls/admin.py`.
* Otimização da experiência com a inserção de filtros de busca laterais, campos pesquisáveis, paginação automatizada e ordenação de colunas.
* Acoplamento em linha (*inlines*) de tabelas para criação e edição simultânea de escolhas (`Choice`) direto no formulário da pergunta (`Question`).

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

5.  **Execute a suíte de testes do aplicativo:**
    ```bash
    uv run python manage.py test polls
    ```

Acesse o projeto em `http://127.0.0.1:8000/polls/` ou o painel administrativo em `http://127.0.0.1:8000/admin/`.