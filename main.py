from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class UsuarioInput(BaseModel):
    nome: str
    email: str

def connectar_banco():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'loja_api',
    }
    conexao = mysql.connector.connect(**config)
    return conexao

@app.get("/")
def paginaInicial():
    conexao = connectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'SELECT * FROM usuarios'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado
