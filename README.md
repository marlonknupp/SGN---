# 💻 SGN - Sistema de Gestão de Notebooks

O **SGN** é um sistema web desenvolvido para realizar a gestão de notebooks em ambientes corporativos ou home office. 
Ele permite acompanhar o número total de notebooks incluíndo os que estão em Home Office, registrar ocorrências, controlar entradas e saídas,
além de visualizar a **localização dos equipamentos em um mapa interativo**.

---

## 🚀 Funcionalidades

- Cadastro e listagem de **notebooks**
- Gerenciamento de **usuários**
- Registro de **ocorrências**
- Controle de **entradas e saídas**
- Visualização em **mapa** da localização dos notebooks
- Painel com **métricas em tempo real**
- Filtros de pesquisa por modelo
- Interface moderna com tema escuro

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django**
- **PostgreSQL**
- **Bootstrap 5**
- **Leaflet.js** (mapa interativo)
- **Crispy Forms** (formulários estilizados)
- **HTML5 / CSS3 / JavaScript**

---

## 🧑‍💻 Como utilizar o sistema

1. **Clone o repositório:**
     git clone 
     cd sgn

**2 - Crie e ative o ambiente virtual:**
      python -m venv venv
      venv\Scripts\activate     # Windows

**3 - Instale as dependências:**

      pip install -r requirements.txt

**4 -- Configure o banco de dados PostgreSQL no settings.py.**

**5 -- Crie as tabelas e superusuário:** 

      python manage.py migrate
      python manage.py createsuperuser

**6 -- Rode o servidor:**

      python manage.py runserver
      http://127.0.0.1:8000/
