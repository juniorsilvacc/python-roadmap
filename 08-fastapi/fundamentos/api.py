from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

jogadores = {
    1: {"nome": "Neymar", "time": "PSG"},
    2: {"nome": "Messi", "time": "PSG"},
    3: {"nome": "Cristiano", "time": "Manchester"},
}

class Jogador(BaseModel):
    nome:str
    time:str

class AtualizaJogador(BaseModel):
    nome: Optional[str] = None
    time: Optional[str] = None

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# -----------------------------
# MODELOS
# -----------------------------

class Jogador(BaseModel):
    nome: str
    time: str

class AtualizaJogador(BaseModel):
    nome: Optional[str] = None
    time: Optional[str] = None

# Banco de dados fictício (em memória)
jogadores = {
    1: {"nome": "João", "time": "Flamengo"},
    2: {"nome": "Pedro", "time": "Palmeiras"}
}

# -----------------------------
# ROTAS
# -----------------------------

# Listar todos os jogadores
@app.get("/")
def listar_jogadores():
    return jogadores

# Obter jogador pelo ID
@app.get("/jogadores/{id_jogador}")
def get_jogador(id_jogador: int):
    if id_jogador not in jogadores:
        return {"erro": "Jogador não encontrado"}
    return jogadores[id_jogador]

# Obter jogador pelo nome do time
@app.get("/jogadores/time/")
def get_jogador_time(time: str):
    #resultado = [dados for dados in jogadores.values() if dados["time"] == time]
    resultado = []
    for dados in jogadores.values():  # percorre todos os jogadores
        if dados["time"] == time:     # verifica se o time bate
            resultado.append(dados)   # adiciona jogador à lista

    if not resultado:
        return {"mensagem": "Nenhum jogador encontrado para este time"}
    return resultado

# Cadastrar novo jogador
@app.post("/jogadores/{jogador_id}")
def post_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {"erro": "Jogador já existe"}
    jogadores[jogador_id] = jogador.dict()
    return {"mensagem": "Jogador cadastrado com sucesso", "jogador": jogadores[jogador_id]}

# Atualizar jogador existente
@app.put("/jogadores/{jogador_id}")
def put_jogador(jogador_id: int, jogador: AtualizaJogador):
    if jogador_id not in jogadores:
        return {"erro": "Jogador não encontrado"}
    if jogador.nome:
        jogadores[jogador_id]["nome"] = jogador.nome
    if jogador.time:
        jogadores[jogador_id]["time"] = jogador.time
    return {"mensagem": "Jogador atualizado com sucesso", "jogador": jogadores[jogador_id]}

# Excluir jogador
@app.delete("/jogadores/{jogador_id}")
def delete_jogador(jogador_id: int):
    if jogador_id not in jogadores:
        return {"erro": "Jogador não encontrado"}
    del jogadores[jogador_id]
    return {"mensagem": "Jogador excluído com sucesso"}
