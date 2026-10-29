# Sistema de Gestão de Estudantes

Aplicação em Python que faz o CRUD de um sistema de gestão de estudantes em um banco de dados Oracle. O sistema controla cursos, disciplinas, alunos e notas, com relatórios de média por turma e de notas dos alunos.

- **Disciplina:** Banco de Dados
- **Professor:** Howard Roatti
- **Semestre:** 2026/2
- **Autor:** Luiz Henrique Garcia

## Modelo de dados

O sistema tem quatro tabelas:

| Tabela | Descrição |
|---|---|
| `CURSOS` | Cursos oferecidos (nome e duração em semestres) |
| `DISCIPLINAS` | Disciplinas, cada uma pertencente a um curso |
| `ALUNOS` | Alunos, cada um matriculado em um curso |
| `NOTAS` | Notas de um aluno em uma disciplina, com semestre e atividade (entre 0 e 10) |

Os relacionamentos são: um curso tem várias disciplinas e vários alunos; um aluno e uma disciplina têm várias notas.

Diagrama relacional: [diagrams/DIAGRAMA_RELACIONAL_ESTUDANTES.png](diagrams/DIAGRAMA_RELACIONAL_ESTUDANTES.png) (código-fonte em [Mermaid](diagrams/DIAGRAMA_RELACIONAL_ESTUDANTES.mmd)).

## Requisitos (Linux)

- Python 3
- Banco de dados Oracle em execução no mesmo computador (`localhost:1521`, serviço `XE`)
- Bibliotecas Python do arquivo `src/requirements.txt`: `cx_Oracle`, `pandas` e `numpy`

> CONFIRMAR: se a máquina virtual da disciplina já tem essas bibliotecas instaladas.

## Configuração

1. Baixe o projeto:

```shell
git clone https://github.com/LuizgarciaMonteiro/luiz-henrique-garcia-sistema-gestao-estudantes.git
cd luiz-henrique-garcia-sistema-gestao-estudantes
```

2. Instale as dependências, se necessário:

```shell
pip install -r src/requirements.txt
```

3. Informe o usuário e a senha do Oracle no arquivo `src/conexion/passphrase/authentication.oracle`, no formato `usuario,senha`.

> CONFIRMAR: o usuário e a senha usados na máquina virtual.

## Como executar

Todos os comandos devem ser executados **de dentro da pasta `src`**:

```shell
cd src
```

1. Criar as tabelas e inserir os dados de exemplo. Atenção: este comando apaga as tabelas existentes e todos os dados:

```shell
python create_tables_and_records.py
```

Na primeira execução, aparecem erros de "tabela não existe" nos comandos `DROP`. É esperado.

2. Executar o sistema:

```shell
python principal.py
```

3. Testar apenas a conexão com o banco (opcional):

```shell
python test.py
```

## Como usar

Ao iniciar, o sistema mostra o nome da aplicação, o total de registros de cada tabela e os dados do autor. Depois, exibe o menu principal:

| Opção | O que faz |
|---|---|
| 1 - Relatórios | Média por turma (disciplina e semestre) e notas dos alunos |
| 2 - Inserir Registros | Cadastra cursos, disciplinas, alunos e notas |
| 3 - Atualizar Registros | Altera registros existentes |
| 4 - Remover Registros | Remove registros, com confirmação. Registros usados por outras tabelas não podem ser removidos |
| 5 - Sair | Encerra o sistema |

## Organização do projeto

- [diagrams](diagrams): diagrama relacional.
- [sql](sql): scripts SQL.
  - [create_tables_estudantes.sql](sql/create_tables_estudantes.sql): apaga e cria as tabelas, as sequences e os relacionamentos.
  - [inserting_samples_records.sql](sql/inserting_samples_records.sql): registros de exemplo.
- [src](src): código do sistema.
  - [conexion](src/conexion): conexão com o Oracle.
  - [model](src/model): classes das entidades (`Curso`, `Disciplina`, `Aluno` e `Nota`).
  - [controller](src/controller): classes que fazem inserir, atualizar e remover no banco.
  - [reports](src/reports): execução dos relatórios.
  - [sql](src/sql): consultas SQL dos relatórios.
  - [utils](src/utils): menus e tela inicial.
  - [principal.py](src/principal.py): programa principal.

## Uso de IA

Ferramentas de IA foram usadas como apoio, e todos os prompts estão registrados em [PROMPTS.md](PROMPTS.md).
