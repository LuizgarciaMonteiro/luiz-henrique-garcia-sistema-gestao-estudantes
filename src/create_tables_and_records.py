from conexion.oracle_queries import OracleQueries

def executar_script(caminho:str):
  # Lê o arquivo e separa os comandos pelo ponto e vírgula
  with open(caminho, encoding="utf-8") as f:
    comandos = f.read().split(";")

  oracle = OracleQueries(can_write=True)
  oracle.connect()

  for comando in comandos:
    comando = comando.strip()
    if len(comando) > 0:
      print(comando)
      try:
        oracle.write(comando)
        print("Executado com sucesso")
      except Exception as e:
        print(e)

def run():
  print("Criando tabelas...")
  executar_script("../sql/create_tables_estudantes.sql")
  print("Tabelas criadas!")

  print("Gerando registros de exemplo...")
  executar_script("../sql/inserting_samples_records.sql")
  print("Registros gerados!")

if __name__ == '__main__':
  run()
