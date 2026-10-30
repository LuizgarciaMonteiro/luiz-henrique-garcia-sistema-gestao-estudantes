MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Média por Turma (disciplina e semestre)
2 - Notas dos Alunos
0 - Voltar
"""

MENU_ENTIDADES = """Entidades
1 - CURSOS
2 - DISCIPLINAS
3 - ALUNOS
4 - NOTAS
0 - Voltar
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=5):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")
