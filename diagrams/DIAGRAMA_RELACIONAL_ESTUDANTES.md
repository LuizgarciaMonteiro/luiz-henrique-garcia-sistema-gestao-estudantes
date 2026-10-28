erDiagram
    CURSOS ||--o{ DISCIPLINAS : "possui"
    CURSOS ||--o{ ALUNOS : "possui"
    ALUNOS ||--o{ NOTAS : "recebe"
    DISCIPLINAS ||--o{ NOTAS : "avalia"

    CURSOS {
        NUMBER id_curso PK "NOT NULL"
        VARCHAR2(100) nome "NOT NULL"
        NUMBER duracao_semestres "NOT NULL"
    }

    DISCIPLINAS {
        NUMBER id_disciplina PK "NOT NULL"
        VARCHAR2(100) nome "NOT NULL"
        NUMBER carga_horaria "NOT NULL"
        NUMBER id_curso FK "NOT NULL"
    }

    ALUNOS {
        VARCHAR2(15) matricula PK "NOT NULL"
        VARCHAR2(100) nome "NOT NULL"
        NUMBER id_curso FK "NOT NULL"
    }

    NOTAS {
        NUMBER id_nota PK "NOT NULL"
        VARCHAR2(15) matricula FK "NOT NULL"
        NUMBER id_disciplina FK "NOT NULL"
        VARCHAR2(6) semestre "NOT NULL"
        VARCHAR2(50) atividade "NOT NULL"
        NUMBER(4,2) nota "NOT NULL, entre 0 e 10"
    }
