# contabilidadepy
# Sistema de Livro de Contas

Um sistema web para gerenciamento de registros contábeis, desenvolvido com Python (Flask) e interface web HTML/CSS.

## Estrutura do Projeto

```
├── static/                  # Pasta para arquivos estáticos
│   └── style.css           # Arquivo CSS para estilização da interface
├── templates/              # Pasta para templates HTML
│   └── index.html         # Página principal do sistema
├── backend em python app.py # Arquivo principal do servidor Flask
├── database.py            # Módulo para gerenciamento dos registros
└── pyproject.toml         # Configurações e dependências do projeto
```

## Descrição dos Componentes

### Arquivos Principais
- `backend em python app.py`: Servidor Flask que gerencia as rotas e a lógica do aplicativo
- `database.py`: Gerencia o armazenamento e manipulação dos registros contábeis
- `templates/index.html`: Interface principal onde os usuários interagem com o sistema
- `static/style.css`: Define o estilo visual da aplicação

### Funcionalidades
- Adição de registros contábeis com data, documentos e descrição
- Visualização dos registros em formato de tabela
- Exclusão de registros individuais
- Interface intuitiva e responsiva

### Tecnologias Utilizadas
- Backend: Python com Flask
- Frontend: HTML, CSS e JavaScript
- Banco de Dados: Sistema de armazenamento em memória

## Como Executar
O projeto pode ser executado através do botão "Run" no ambiente Replit, que iniciará o servidor Flask na porta 8080.
