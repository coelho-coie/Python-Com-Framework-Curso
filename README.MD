<h1 align="center">🐍 Python com Framework — Curso</h1>

<p align="center">
  Projetos e exercícios do curso de Python e Django, no <b>SENAI Sertãozinho</b>.<br>
  <sub>Cada projeto vive em uma branch própria.</sub>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white">
  <img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white">
  <img alt="Curso" src="https://img.shields.io/badge/Curso-conclu%C3%ADdo-brightgreen?style=flat">
</p>

| Branch | Projeto |
|---|---|
| [`master`](https://github.com/coelho-coie/Python-Com-Framework-Curso/tree/master) | 🍔 Cantina Digital — gestão de pedidos, cardápio e pagamentos (projeto final, abaixo) |
| [`Calc`](https://github.com/coelho-coie/Python-Com-Framework-Curso/tree/Calc) | 🧮 Calculadora de IMC |
| [`ContStr`](https://github.com/coelho-coie/Python-Com-Framework-Curso/tree/ContStr) | 🔤 Contador de caracteres e palavras |
| [`CalcContStr`](https://github.com/coelho-coie/Python-Com-Framework-Curso/tree/CalcContStr) | 🧩 Calculadora + contador no mesmo projeto |
| [`Exercicios-py`](https://github.com/coelho-coie/Python-Com-Framework-Curso/tree/Exercicios-py) | 📚 Exercícios de Python, Dia 01 a Dia 07 |

---

# 🍔 Cantina Digital - Sistema de Gestão de Pedidos

Um sistema web completo e moderno para gerenciamento de cantinas, desenvolvido em **Django**. O projeto permite a visualização de cardápios interativos, cadastro de clientes, gestão de produtos e fluxo completo de carrinho de compras e pedidos.

---

## 🚀 Funcionalidades Principais

- **🏠 Home & Cardápio Digital (`produtos`)**:
  - Exibição de produtos/salgados organizados por cards interativos.
  - Animações fluidas no carregamento e verificação automática de disponibilidade.
  - Exibição dinâmica de preços formatados e fotos dos produtos.
  - Suporte a imagens padrão para itens sem upload.

- **🛒 Gestão de Pedidos e Carrinho (`pedidos`)**:
  - Adição e remoção de produtos no carrinho em tempo real.
  - Visualização resumida e detalhada do carrinho de compras.
  - Acompanhamento do histórico e listagem dos pedidos.

- **👤 Gestão de Clientes (`clientes`)**:
  - Interface dedicada para cadastro de clientes e dados de perfil.
  - Autenticação e telas de login integradas com o sistema nativo do Django.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3, Django
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons, AOS (Animate On Scroll)
- **Banco de Dados**: SQLite (padrão de desenvolvimento)
- **Gerenciamento de Arquivos**: Django Media File Uploads

---

## 📂 Estrutura do Projeto

```bash
PROJETO_CANTINA/                  # Pasta raiz do projeto
├── clientes/                     # App responsável pelos clientes (cadastro, dados, etc.)
│   ├── templates/                # Templates HTML do app clientes
│   │   ├── clientes/             # Subpasta padrão para organização dos templates do app
│   │   │   └── cadastro.html     # Página de cadastro de clientes
│   │   └── semuso.txt            # Arquivo auxiliar
│   └── urls.py                   # Rotas específicas do app clientes
├── media/                        # Arquivos enviados pelo usuário (uploads)
│   └── salgados/                 # Imagens dos produtos (ex: fotos dos salgados)
├── pedidos/                      # App responsável pelos pedidos
│   ├── templates/                # Templates HTML do app pedidos
│   │   ├── pedidos/              # Subpasta padrão para organização dos templates do app
│   │   │   ├── carrinho.html     # Página do carrinho
│   │   │   ├── lista_pedidos.html # Listagem de pedidos
│   │   │   └── novo_pedido.html  # Criação de novo pedido
│   │   └── semuso.txt            # Arquivo auxiliar
│   └── urls.py                   # Rotas específicas do app pedidos
├── produtos/                     # App responsável pelos produtos/cardápio
│   ├── templates/                # Templates HTML do app produtos
│   │   ├── produtos/             # Subpasta padrão para organização dos templates do app
│   │   │   ├── cardapio.html     # Página de cardápio
│   │   │   └── home.html         # Página inicial
│   │   └── semuso.txt            # Arquivo auxiliar
│   └── urls.py                   # Rotas específicas do app produtos
├── static/                       # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/                      # Arquivos de estilo (CSS)
│   ├── img/                      # Imagens do layout (logos, ícones, etc.)
│   └── semuso.txt                # Arquivo auxiliar
├── templates/                    # Templates globais do projeto
│   ├── registration/             # Templates de autenticação do Django
│   │   └── login.html            # Página de login
│   └── base.html                 # Template base (layout principal do site)
├── .gitignore                    # Arquivos/pastas ignorados pelo Git
├── README.md                     # Documentação do projeto
└── requirements.txt              # Dependências do projeto (Python)
```

---

## ⚙️ Como Executar o Projeto Localmente

### 📋 Pré-requisitos
- **Python 3.10+** instalado
- **Git** instalado

### 🔧 Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/projeto-cantina.git
   cd projeto-cantina
   ```

2. **Criar e Ativar o Ambiente Virtual (venv):**
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```powershell
     python -m venv venv
     . env\Scripts ctivate
     ```

3. **Instalar as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar as Migrações do Banco de Dados:**
   ```bash
   python manage.py migrate
   ```

5. **Criar um Superusuário (para acessar o painel administrativo):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciando o Servidor de Desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acessar a Aplicação:**
   Abra o seu navegador e acesse: `http://127.0.0.1:8000/`

---