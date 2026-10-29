select a.matricula
     , a.nome as aluno
     , c.nome as curso
     , d.nome as disciplina
     , n.semestre
     , n.atividade
     , n.nota
  from notas n
  inner join alunos a
  on n.matricula = a.matricula
  inner join cursos c
  on a.id_curso = c.id_curso
  inner join disciplinas d
  on n.id_disciplina = d.id_disciplina
  order by a.nome, n.semestre, d.nome, n.atividade
