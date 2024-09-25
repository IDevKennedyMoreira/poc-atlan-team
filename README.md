# Sistema de Login e Registro com Django e Flet

Este é um sistema de login e registro desenvolvido utilizando Django como backend e Flet como frontend. O sistema permite que os usuários se registrem com um email corporativo, matrícula e senha, e realizem o login com as mesmas credenciais.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração do Backend](#configuração-do-backend)
- [Configuração do Frontend](#configuração-do-frontend)
- [Executando o Projeto](#executando-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Django
- Flet
- Um banco de dados (SQLite, PostgreSQL, etc.)

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio

2. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv

3. **Ative o ambiente virtual:**

    ```bash
    venv\Scripts\activate

    source venv/bin/activate

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt

## Configuração do Backend

1. **Navegue até o diretório do backend:**

    ```bash
    cd backend

2. **Crie e aplique as migrações:**

    ```bash
    python manage.py migrate

3. **Crie um superusuário (opcional):**

    ```bash
    python manage.py createsuperuser

4. **Inicie o servidor Django:**

    ```bash
    python manage.py runserver

## Configuração do Frontend

1. **Navegue até o diretório do frontend:**

    ```bash
    cd frontend


2. **Inicie a aplicação Flet:**

    ```bash
    python main.py

## Executando o Projeto

1. Certifique-se de que o servidor Django esteja em execução.
2. Inicie a aplicação Flet.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
