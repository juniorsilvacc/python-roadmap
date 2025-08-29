from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Inserir Dados

def adicionar_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# adicionar_filme("Interestrelar", 2014, 10.0)

def atualizar_filme(id, nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualizar_filme(1, "Homem Aranha", 2001, 9.9)

def excluir_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
    session.commit()
    session.close()

# excluir_filme(1)