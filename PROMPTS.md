# PROMPTS.md

Registro dos prompts usados como apoio de IA neste trabalho, conforme o item 5 das Observações Importantes do edital.

- **Ferramenta:** Claude (Anthropic), via Claude Code
- **Autor dos prompts:** Luiz Henrique Garcia
- **Como usamos a IA:** um passo de cada vez. Eu peço, leio a explicação, e só então avançamos. O objetivo é entender o código, não só copiá-lo.

Cada entrada tem: o prompt, a fonte e o que eu fiz com a resposta.

---

## Prompt 1 — Pedido de ajuda e envio do edital

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi ajuda para o trabalho de banco de dados, informei que estou sem grupo e que o prazo é dia 30, e perguntei se podia enviar a especificação, o tema e o exemplo do professor. Depois enviei o edital em PDF, escolhi o tema "Sistema de Gestão de Estudantes" e combinei de seguirmos passo a passo, sem a IA dar passos maiores do que eu pedir.
- **O que fizemos com a resposta:** A IA leu o edital e resumiu o que é exigido (menu, relatórios, entregáveis, pontuação, PROMPTS.md) e propôs um plano em etapas seguindo o roteiro do professor. Usei o resumo para me organizar.

## Prompt 2 — E-mail para o professor

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi ajuda para escrever um e-mail ao professor avisando que farei o trabalho sozinho.
- **O que fizemos com a resposta:** Recebi um modelo de e-mail, preenchi com meus dados e enviei pelo meu e-mail.

## Prompt 3 — Escolha do banco de dados

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Informei que só tenho acesso à máquina virtual da faculdade quando estou lá e pedi para seguirmos o melhor caminho para rodar nela. Depois esclareci que o edital já indica o caminho e pedi para fazermos o que o professor pediu.
- **O que fizemos com a resposta:** Decidimos usar Oracle com Python, seguindo o projeto de exemplo do professor.

## Prompt 4 — Fork do projeto de exemplo

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para começar a Etapa 0 (preparar o ambiente).
- **O que fizemos com a resposta:** Segui as instruções e fiz o fork do `example_crud_oracle` na minha conta do GitHub.

## Prompt 5 — Conhecer o projeto do professor

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Enviei o link do meu fork e disse que o fork estava feito.
- **O que fizemos com a resposta:** A IA leu a estrutura do projeto e explicou o que cada pasta faz (model, controller, conexion, sql, reports, utils, principal). Usei a explicação para entender o projeto antes de alterá-lo.

## Prompt 6 — Criação do PROMPTS.md

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para criar o PROMPTS.md.
- **O que fizemos com a resposta:** A IA gerou este arquivo com o registro dos prompts anteriores. Vou adicioná-lo ao repositório e atualizá-lo a cada novo prompt.


## Prompt 7 — Escolha das entidades

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para começar a Etapa 1 (modelagem). Depois perguntei se o aluno poderia ter mais de uma nota e mais de uma atividade, ou se só guardaríamos a média final.
- **O que fizemos com a resposta:** A IA propôs entidades iniciais (cursos, alunos e notas) e explicou que a média não precisa ser guardada, porque pode ser calculada com `AVG()`. Aceitei a ideia de guardar uma linha por nota, com um campo de atividade.

## Prompt 8 — Disciplinas

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Perguntei se o professor poderia reclamar da falta de disciplinas. Disse que a explicação ficou confusa porque misturava curso e disciplina. Depois escolhi o modelo completo.
- **O que fizemos com a resposta:** A IA esclareceu a diferença entre curso (a graduação) e disciplina (a matéria) e apresentou duas opções. Escolhi a opção com 4 tabelas: CURSOS, DISCIPLINAS, ALUNOS e NOTAS.

## Prompt 9 — Campos de CURSOS, DISCIPLINAS e ALUNOS

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Concordei com cada tabela e pedi para seguir para a próxima, uma de cada vez.
- **O que fizemos com a resposta:** A IA propôs os campos, os tipos do Oracle e as chaves primárias e estrangeiras de cada tabela. Revisei e aceitei, com a mudança descrita no Prompt 10.

## Prompt 10 — Turma e semestre

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Questionei se a turma era mesmo necessária, de onde vinha a exigência de média por turma e se poderia ser por disciplina ou curso. Expliquei que, para mim, turma é a média dos alunos de uma disciplina em um semestre.
- **O que fizemos com a resposta:** A IA confirmou que a exigência vinha só da tabela de temas sugeridos do edital, que não é obrigatória. Reconheceu que a minha definição de turma estava certa. Decidimos tirar a turma de ALUNOS e acrescentar o campo `semestre` em NOTAS. A turma passa a ser a combinação de disciplina e semestre.

## Prompt 11 — Tabela NOTAS e regras

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Concordei com os campos de NOTAS. Perguntei se era possível limitar as notas entre 0 e 10 e se a nota final poderia ser a média simples das notas de cada aluno por disciplina e semestre.
- **O que fizemos com a resposta:** A IA explicou a restrição `CHECK (nota BETWEEN 0 AND 10)` e o cálculo da média com `AVG` e `GROUP BY`, sem guardar a nota final na tabela. Aceitei as duas ideias.

## Prompt 12 — Diagrama relacional

- **Data:** 28/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para criar o diagrama.
- **O que fizemos com a resposta:** A IA escreveu o código Mermaid. Gerei a imagem no mermaid.live, conferi as tabelas e as ligações, troquei o nome de uma ligação e guardei o PNG e o arquivo `.mmd` na pasta `diagrams/`.

- 
## Prompt 13 — Script de criação das tabelas

- **Data:** 29/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para fazermos o script SQL juntos, para eu aprender. Escrevi o código de cada tabela e das chaves estrangeiras, e a IA conferiu e apontou erros (`VARCHAR` em vez de `VARCHAR2`, campo faltando, nomes trocados, erros de digitação e tipos diferentes do diagrama). Também perguntei o que era LABDATABASE e o que era "CK".
- **O que fizemos com a resposta:** A IA explicou cada comando (`CREATE TABLE`, `PRIMARY KEY`, `ALTER TABLE ... FOREIGN KEY`, `CHECK`) e o padrão de nomes do professor. Corrigi meus erros e montei o arquivo `sql/create_tables_estudantes.sql`.



## Prompt 14 — Classes do modelo em Python

- **Data:** 29/10/2026
- **Fonte:** Claude (Anthropic)
- **Prompt:** Pedi para começar a Etapa 2 passo a passo. Escrevi a classe `Curso` com a ajuda da IA, que corrigiu meus erros (setters guardando no atributo errado, nomes inconsistentes, `to_string` faltando). Perguntei por que o `self` existe e se o `=None` é obrigatório. Depois pedi que a IA escrevesse as classes `Disciplina`, `Aluno` e `Nota`, por falta de tempo.
- **O que fizemos com a resposta:** Li cada classe e respondi a uma pergunta de conferência sobre cada uma (o que acontece com `curso=None`, por que o objeto guarda a associação completa e como chegar ao curso a partir de uma nota). Salvei os arquivos em `src/model/`.
