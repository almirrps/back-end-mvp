## Projeto CadCliente - Cadastro Único de Clientes
Projeto back-end de apresentação MVP do Sprint Desenvolvimento Full Stack Básico.
------------------------------
## 📌 Índice

* [Sobre o Projeto](#-sobre-o-projeto)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Pré-requisitos](#-pré-requisitos)
* [Instalação](#-instalação)
* [Como Executar](#-como-executar)
* [Acessando Documentação](#-acessando-documentação)
* [Como Contribuir](#-como-contribuir)
------------------------------
## 📖 Sobre o Projeto

Este projeto tem o objetivo de realizar o cadastro de clientes com endereço para envios de correspondências e notificações.
------------------------------
## ✨ Funcionalidades

* 1: Cadastro de clientes
* 2: Cadastro de endereços relacionados ao cliente cadastrado
* 3: Consulta de clientes por meio do nome e seus respectivos endereços cadastrados
* 4: Deleção de clientes
* 5: Deleção de endereços de um determinado cliente
------------------------------
## 🛠 Tecnologias Utilizadas

As principais ferramentas e bibliotecas usadas no desenvolvimento:
* [Python 3.12](https://www.python.org/downloads/release/python-3120/)
* [Flask](https://pypi.org/project/Flask/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
------------------------------
## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
* Python (versão 3.x recomendada)
* Gerenciador de pacotes pip (geralmente já vem com o Python)
* (Opcional) Ambiente virtual como venv ou conda [7, 8, 9] 
------------------------------
## 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

   1. Clone o repositório: 

git clone https://github.com/almirrps/back-end-mvp.git


   2. Entre na pasta do projeto:

cd back-end-mvp


   3. Crie e ative um ambiente virtual (recomendado):

# Windows
python -m venv venv
venv\Scripts\activate
# Linux/macOS
python3 -m venv venv
source .venv/bin/activate


   4. Instale as dependências:

pip install -r requirements.txt
------------------------------
## 🚀 Como Executar

Com o terminal na pasta raiz do projeto, execute o comando abaixo:

(env)$ flask run --host 0.0.0.0 --port 5000
------------------------------
## 🧪 Acessando Documentação

Para acessar a documentação do Swagger da aplicação, digite no browser de sua preferência o link abaixo:

http://192.168.18.225:5000/openapi/
------------------------------
## 🤝 Como Contribuir

Contribuições são sempre bem-vindas! Para contribuir:

   1. Faça um Fork do projeto.
   2. Crie uma Branch para sua funcionalidade (git checkout -b feature/nova-funcionalidade).
   3. Faça o Commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').
   4. Faça o Push para a branch (git push origin feature/nova-funcionalidade).
   5. Abra um Pull Request.