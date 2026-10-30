# PROMPTS.md

Registro do uso de IA neste trabalho, conforme o item 5 das Observações Importantes do edital. Os prompts estão resumidos por etapa.

- **Ferramenta:** Claude (Anthropic), via Claude Code
- **Autor dos prompts:** Luiz Henrique Garcia
- **Período:** 22/10/2026 a 30/10/2026
- **Como usei a IA:** trabalhei em passos pequenos. A IA propunha ou escrevia, e eu lia, corrigia, respondia a perguntas de conferência e salvava no repositório.

## Etapa 1: entendimento do edital e planejamento

- **Fonte:** Claude (Anthropic)
- **Prompt:** Enviei o edital e o tema escolhido e pedi ajuda para planejar o trabalho passo a passo. Pedi também um modelo de e-mail ao professor e a explicação do projeto de exemplo.
- **O que a IA fez:** Resumiu as exigências do edital, propôs um plano em etapas e explicou a estrutura do projeto do professor.
- **O que eu fiz:** Escolhi Oracle e Python, fiz o fork do projeto de exemplo e criei o repositório.

## Etapa 2: modelagem e diagrama

- **Fonte:** Claude (Anthropic)
- **Prompt:** Perguntei como modelar várias notas e atividades por aluno, se a falta de disciplinas seria um problema e o que significava "turma". Pedi o diagrama relacional.
- **O que a IA fez:** Propôs alternativas de modelo e escreveu o código Mermaid do diagrama.
- **O que eu fiz:** Decidi pelo modelo de 4 tabelas (cursos, disciplinas, alunos e notas), defini que a turma é a combinação de disciplina e semestre (campo `semestre` em NOTAS), pedi a nota limitada entre 0 e 10, gerei a imagem do diagrama e guardei os arquivos em `diagrams/`.

## Etapa 3: script SQL de criação das tabelas

- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para fazermos o script juntos. Perguntei o que era o esquema `LABDATABASE`, o sufixo `CK` e como gerar os IDs.
- **O que a IA fez:** Explicou cada comando e o padrão do projeto de exemplo, e apontou erros no meu código. Escreveu o bloco de `DROP`.
- **O que eu fiz:** Escrevi os 4 `CREATE TABLE`, as 4 chaves estrangeiras, o `CHECK` da nota e as 3 sequences, e corrigi cada erro apontado.

## Etapa 4: classes do modelo

- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para escrever as classes em Python. Perguntei para que serve o `self` e se o `=None` é obrigatório. Pedi as classes `Disciplina`, `Aluno` e `Nota`.
- **O que a IA fez:** Explicou o código de exemplo do professor e escreveu as classes `Disciplina`, `Aluno` e `Nota`.
- **O que eu fiz:** Escrevi a classe `Curso` e corrigi os erros apontados (setters, nomes e `to_string`). Li as outras classes e respondi a uma pergunta de conferência sobre cada uma.

## Etapa 5: controllers

- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi os controllers, um método por vez, com explicação.
- **O que a IA fez:** Escreveu os 4 controllers (inserir, atualizar e excluir), seguindo o `controller_cliente.py` do projeto de exemplo.
- **O que eu fiz:** Li cada método, respondi a uma pergunta de conferência por método e salvei os arquivos.

## Etapa 6: relatórios, menus e programa principal

- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi os relatórios, os menus, a tela inicial e o `principal.py`.
- **O que a IA fez:** Escreveu as 2 consultas dos relatórios (uma com `GROUP BY` e outra com `JOIN`), a classe `Relatorio`, os menus, a tela inicial e o `principal.py`, com as perguntas de continuação do edital.
- **O que eu fiz:** Li as explicações, respondi às perguntas de conferência e salvei os arquivos.

## Etapa 7: dados de exemplo, README e teste na máquina virtual

- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi o que faltava para o projeto rodar e ser entregue, e ajuda para testá-lo na máquina virtual da disciplina.
- **O que a IA fez:** Escreveu os dados de exemplo, o `create_tables_and_records.py` e o `README.MD`, e verificou a sintaxe dos arquivos, os imports e as consultas dos relatórios em um banco de teste.
- **O que eu fiz:** Salvei os arquivos e testei o sistema no Oracle da máquina virtual. Nesse teste, a IA me orientou nos comandos e escreveu a versão ajustada do `oracle_queries.py` (uso de `oracledb`, serviço `XEPDB1` e leitura das credenciais). Apliquei os ajustes e atualizei o `README.MD` e o `requirements.txt`.
