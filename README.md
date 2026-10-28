# Sistema de Gestão Escolar (SGE) — MVP

Sistema web para gestão escolar no formato SESI/SENAI (ensino médio integrado ao técnico), construído em Python com Flask.

> ⚠️ **Status: MVP em desenvolvimento.** O projeto está na primeira fase — apenas o cadastro de alunos funciona. Diversas funcionalidades descritas nos requisitos ainda não foram implementadas. Veja a seção [O que falta fazer](#o-que-falta-fazer) para detalhes.

---

## Tecnologias

| Camada       | Tecnologia                    |
|-------------|-------------------------------|
| Backend     | Python 3.14 + Flask           |
| Banco de dados | SQLite (transição para PostgreSQL planejada) |
| Forms       | Flask-WTF + WTForms           |
| Templates   | Jinja2 (HTML puro)            |
| Infra       | ~~Docker (planejado)~~        |

## Arquitetura

O código segue o padrão **MVC**:

```
sistema/
├── app.py                      # Entrada da aplicação, rotas
├── database.py                 # Conexão com o banco (SQLite)
├── escola.db                   # Banco de dados SQLite
├── controllers/
│   └── Aluno_controller.py     # Rotas e lógica de controle
├── models/
│   └── Aluno.py                # Entidade Aluno
├── repositories/
│   └── Aluno_Repository.py     # CRUD no banco de dados
├── views/
│   └── Aluno_form.py           # Formulário com validações
└── templates/
    ├── index.html              # Página inicial
    ├── formulario.html         # Formulário de cadastro
    └── lista_alunos.html       # (vazio — não implementado)
```

### Principais decisões
- **Banco:** SQLite para desenvolvimento/testes; PostgreSQL definido para produção (conexao com MySQL existente no código, mas comentada).
- **Frontend:** HTML + Jinja2 puro na fase atual. React está planejado para a segunda etapa.
- **Autenticação:** Não existe. Acesso livre a todas as rotas no momento.

---

## O que foi feito

### Funcionalidades implementadas

- ✅ Rota inicial (`/`) com link para cadastro
- ✅ Formulário de cadastro de aluno com validações (nome, email, data de nascimento) via Flask-WTF
- ✅ Inserção de alunos no banco SQLite
- ✅ Estrutura MVC completa para a entidade **Aluno** (model → repository → controller → template)
- ✅ Documentação de requisitos, arquitetura e notas de desenvolvimento em `documentos/`
- ✅ Virtualenv configurado com as dependências básicas

### Requisitos atendidos

| ID      | Descrição                        | Status    |
|---------|----------------------------------|-----------|
| RF01    | Cadastrar, listar, consultar, editar e desativar alunos | Parcial — apenas cadastrar |
| RF02–RF08 | Demais funcionalidades (disciplinas, turmas, notas, frequência, boletim, risco, pesquisa) | ❌ Não implementado |

---

## Como rodar localmente

### Pré-requisitos
- Python 3.14+
- Pip

### Passos

```bash
# Criar e ativar o virtualenv (já existe .venv, mas recomendo reconstruir)
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install Flask Flask-WTF WTForms email-validator

# Rodar a aplicação
cd sistema
python app.py
```

A aplicação iniciará em `http://127.0.0.1:5000`.

> **Nota:** A tabela é criada automaticamente na primeira execução (`Criar_tabela()`), mas observe que ela é chamada **após** `app.run()`, o que significa que só terá efeito em execuções subsequentes se o servidor for reiniciado.

---

## O que falta fazer

### Crítico (bloqueia qualquer uso real)

- **[ ] Autenticação e autorização**
  - Tela de login
  - Sessão de usuário
  - 5 perfis de acesso: Aluno, Professor, Diretoria, Pais, Administrador
  - Proteção de rotas por perfil
- **[ ] Infraestrutura em container (Docker)**
  - `Dockerfile` para a aplicação
  - `docker-compose.yml` com serviço do banco (PostgreSQL)
  - Variáveis de ambiente para configuração sensível (secret key, DB credentials)
  - Migração da conexão SQLite para PostgreSQL
- **[ ] Correção de bugs existentes**
  - `Criar_tabela()` chamado após `app.run()` — precisa ser invertido
  - Chave secreta hardcodada em `app.py`
  - `lista_alunos.html` vazio e sem rota correspondente
  - Matricula gerada pelo model nunca é salva no banco

### Funcionalidades não implementadas

| Prioridade | Funcionalidade | Requisitos |
|------------|---------------|------------|
| Alta       | Listar, consultar, editar e desativar alunos | RF01 |
| Alta       | Cadastro de disciplinas e turmas, vinculação | RF02 |
| Alta       | Matrícula/unmatrícula de alunos em turmas | RF03 |
| Média      | Lançamento de notas | RF04 |
| Média      | Registro de frequência/chamada | RF05 |
| Média      | Boletim do aluno | RF06 |
| Baixa      | Alunos em risco (nota/frequência) | RF07 |
| Baixa      | Pesquisa e filtros de alunos | RF08 |
| —          | Dashboard com métricas | Arquitetura.md |

### Melhorias estruturais

- Separar backend (API) do frontend (React) — segunda etapa do plano
- Adicionar `requirements.txt`
- Adicionar estilos CSS / framework responsivo
- Testes automatizados
- Migração de esquema para PostgreSQL

---

## Fases do projeto

1. **MVP atual** — backend Python, HTML puro, cadastro de alunos
2. **Segunda fase** — separação back/frontend, API Python + React, autenticação
3. **Terceira fase** — todos os perfis de usuário, funcionalidades completas, deploy em container

---

## Documentação

| Arquivo             | Conteúdo                                           |
|---------------------|----------------------------------------------------|
| `documentos/requisitos.md`    | Requisitos funcionais, regras de negócio e não funcionais |
| `documentos/arquitetura.md`   | Decisões de arquitetura, telas planejadas, fases  |
| `documentos/1.controllers.md` | Notas sobre a camada de controller                 |
| `documentos/1.models.md`      | Notas sobre a camada de model                      |
| `documentos/1.formularios.md` | Notas sobre formulários com Flask-WTF              |
| `documentos/fluxograma_funcionamento.png` | Fluxograma do funcionamento do sistema |

---

## Licença

Projeto acadêmico/pessoal.
