
<p align="center">
  <img src="https://your-image-url.com/banner.png" alt="Project Banner" width="100%" />
</p>

# 📚 FastAPI MADR

Uma API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para facilitar [descrição breve do objetivo da API].  
Ideal para quem busca uma base sólida em Python para aplicações modernas, com autenticação, testes e banco de dados integrados.

## 🚀 Visão Geral

Este projeto oferece uma estrutura robusta e modular para criação de APIs, com foco em boas práticas de código, segurança e testes automatizados.  
É possível executar localmente com SQLite ou em ambiente containerizado com Docker e PostgreSQL.

Principais recursos:
- CRUD completo com autenticação via JWT  
- Banco de dados relacional com SQLAlchemy e Alembic  
- Testes automatizados com cobertura total usando `pytest`  
- CI com GitHub Actions (pronto para deploy contínuo)  

## 🛠️ Tecnologias e Ferramentas

- **FastAPI** · Framework web rápido e assíncrono  
- **Pydantic** · Validação de dados com tipagem estática  
- **PostgreSQL / SQLite** · Banco de dados relacional  
- **SQLAlchemy** · ORM para Python  
- **Alembic** · Migrações de banco de dados  
- **JWT** · Autenticação baseada em token  
- **Pytest + FactoryBoy + Freezegun + Testcontainers** · Suite de testes robusta  
- **Ruff** · Linter e formatador rápido  
- **Taskipy** · Automação de comandos  

## 🧪 Como Executar os Testes

Certifique-se de ter o Docker instalado, pois alguns testes utilizam containers para o banco:

```
task test
```

Para visualizar a cobertura de testes:

```
open htmlcov/index.html
```

## 💻 Como Rodar o Projeto

### 1. Clonar o repositório e acessar a pasta:

```
git clone git@github.com:vgrcontreras/fastapi_madr.git && cd fastapi_madr
```

### 2. Usando Docker:

Crie um arquivo `.env` com base no `.env-example` e execute:

```
docker compose up --build
```

Acesse via navegador:

```
http://localhost:8000/docs
```

### 3. Rodando Localmente com SQLite:

Certifique-se de ter Python 3.12+ instalado e, preferencialmente, use `pyenv` e `poetry`:

```
pyenv local 3.12.2 && poetry install && poetry run alembic upgrade head && poetry run uvicorn src.app:app --reload
```

## 🔐 Autenticação

As rotas protegidas exigem um token JWT.  
Use o endpoint `/auth` para obter o token e envie-o nos headers das requisições autenticadas:

```
Authorization: Bearer <seu_token>
```

## 🧹 Formatando o Código

Para aplicar os padrões definidos pelo projeto:

```
task format
```

## ✨ Melhorias Futuras

- [ ] Implementar suporte assíncrono no banco de dados  
- [ ] Adicionar caching com Redis  
- [ ] Criar interface web para gerenciamento de dados  

## 👤 Autor

Feito por [Victor Contreras](www.linkedin.com/in/vgr-contreras)  
Contribuições, ideias e feedbacks são sempre bem-vindos!
