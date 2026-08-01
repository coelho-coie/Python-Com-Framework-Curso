PROJETO_CANTINA/
├── clientes/             # App de gestão de usuários, clientes e perfis.
├── media/                # Diretório para armazenamento de uploads (ex: fotos dos produtos).
├── pagamentos/           # App para processamento de vendas e métodos de pagamento.
├── pedidos/              # App para controle de carrinho e ordens de serviço.
├── produtos/             # App para gerenciamento do catálogo e estoque.
├── setup/                # Pasta de configuração central (settings.py, urls.py, wsgi.py).
├── static/               # Arquivos estáticos servidos pelo servidor.
│   ├── css/              # Pastas para arquivos de estilização.
│   └── img/              # Pastas para imagens fixas e ícones do sistema.
├── templates/            # Arquivos de visualização HTML.
│   └── registration/     # Pasta para templates do sistema de autenticação.
└── venv/                 # Ambiente virtual com as bibliotecas isoladas.

PROJETO_CANTINA/                  # Pasta raiz do projeto
├── clientes/                    # App responsável pelos clientes (cadastro, dados, etc.)
│   ├── templates/               # Templates HTML do app clientes
│   │   ├── clientes/            # Subpasta padrão para organização dos templates do app
│   │   │   └── cadastro.html    # Página de cadastro de clientes
│   │   └── semuso.txt           # Arquivo auxiliar (não utilizado)
│   └── urls.py                  # Rotas específicas do app clientes
├── media/                       # Arquivos enviados pelo usuário (uploads)
│   └── salgados/                # Imagens dos produtos (ex: fotos dos salgados)
├── pedidos/                     # App responsável pelos pedidos
│   ├── templates/               # Templates HTML do app pedidos
│   │   ├── pedidos/             # Subpasta padrão para organização dos templates do app
│   │   │   ├── carrinho.html    # Página do carrinho
│   │   │   ├── lista_pedidos.html # Listagem de pedidos
│   │   │   └── novo_pedido.html # Criação de novo pedido
│   │   └── semuso.txt           # Arquivo auxiliar (não utilizado)
│   └── urls.py                  # Rotas específicas do app pedidos
├── produtos/                    # App responsável pelos produtos/cardápio
│   ├── templates/               # Templates HTML do app produtos
│   │   ├── produtos/            # Subpasta padrão para organização dos templates do app
│   │   │   ├── cardapio.html    # Página de cardápio
│   │   │   └── home.html        # Página inicial
│   │   └── semuso.txt           # Arquivo auxiliar (não utilizado)
│   └── urls.py                  # Rotas específicas do app produtos
├── static/                      # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/                     # Arquivos de estilo (CSS)
│   ├── img/                     # Imagens do layout (logos, ícones, etc.)
│   └── semuso.txt               # Arquivo auxiliar (não utilizado)
├── templates/                   # Templates globais do projeto
│   ├── registration/            # Templates de autenticação do Django
│   │   └── login.html           # Página de login
│   └── base.html                # Template base (layout principal do site)
├── .gitignore                   # Arquivos/pastas ignorados pelo Git
├── README.md                    # Documentação do projeto
└── requirements.txt             # Dependências do projeto (Python)