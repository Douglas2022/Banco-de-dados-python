from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste se necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClienteInput(BaseModel):
    nome: str
    email: str
    telefone: str
    endereco: str
    data_nascimento: str

# Função para conectar ao banco de dados
def conectar_banco():
    try:
        config = {
            'user': 'root',
            'password': '',  # Coloque sua senha aqui, se houver
            'host': 'localhost',
            'database': 'Mysql',  # Nome correto do banco de dados
        }
        conexao = mysql.connector.connect(**config)
        return conexao
    except Error as e:
        print("Erro ao conectar ao banco:", e)
        return None

@app.get("/")
def pagina_inicial():
    try:
        conexao = conectar_banco()
        if conexao is None:
            return {"erro": "Não foi possível conectar ao banco de dados."}

        cursor = conexao.cursor(dictionary=True)
        sql = 'SELECT * FROM clientes'  # Alterado para consultar a tabela "clientes"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado

    except Exception as e:
        return {"erro": str(e)}
