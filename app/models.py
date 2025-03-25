from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app import db

# Tabela de Usuários
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    tipo_usuario = Column(String)  # Cliente ou Suporte
    data_criacao = Column(DateTime, default=db.func.current_timestamp())
    empresa = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    tickets = relationship("Ticket", back_populates="usuario", cascade="all, delete-orphan")
    mensagens = relationship("Mensagem", back_populates="usuario", cascade="all, delete-orphan")
    arquivos = relationship("Arquivo", back_populates="usuario", cascade="all, delete-orphan")

    # Flask-Login methods
    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


# Tabela de Tickets
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="aberto")  # Aberto, Em Andamento, Fechado
    prioridade = Column(String, default="média")  # Baixa, Média, Alta
    data_criacao = Column(DateTime, default=db.func.current_timestamp())
    data_fechamento = Column(DateTime, nullable=True)

    usuario = relationship("Usuario", back_populates="tickets")
    mensagens = relationship("Mensagem", back_populates="ticket", cascade="all, delete-orphan")
    arquivos = relationship("Arquivo", back_populates="ticket", cascade="all, delete-orphan")


# Tabela de Mensagens
class Mensagem(db.Model):
    __tablename__ = 'mensagens'
    id = Column(Integer, primary_key=True, index=True)
    id_ticket = Column(Integer, ForeignKey('tickets.id'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    mensagem = Column(String)
    data_envio = Column(DateTime, default=db.func.current_timestamp())

    ticket = relationship("Ticket", back_populates="mensagens")
    usuario = relationship("Usuario", back_populates="mensagens")


# Tabela de Arquivos
class Arquivo(db.Model):
    __tablename__ = 'arquivos'
    id = Column(Integer, primary_key=True, index=True)
    id_ticket = Column(Integer, ForeignKey('tickets.id'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    nome_arquivo = Column(String)
    caminho = Column(String)
    data_upload = Column(DateTime, default=db.func.current_timestamp())

    ticket = relationship("Ticket", back_populates="arquivos")
    usuario = relationship("Usuario", back_populates="arquivos")
