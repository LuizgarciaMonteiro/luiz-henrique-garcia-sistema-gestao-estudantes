select d.nome as disciplina
     , n.semestre
     , count(distinct n.matricula) as qtd_alunos
     , round(avg(n.nota), 2) as media
  from notas n
  inner join disciplinas d
  on n.id_disciplina = d.id_disciplina
  group by d.nome, n.semestre
  order by n.semestre, d.nome
