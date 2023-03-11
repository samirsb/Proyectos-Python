from PreEntrega2.main import login, db_file, read_db
import json

# Inicio del programa
db = dict()
try:
  f = open('base-datos.json')
  db = json.load(f)
  login(db)
  db_file(db)
  read_db(db)
except:
  login(db)
  db_file(db)
  read_db(db)