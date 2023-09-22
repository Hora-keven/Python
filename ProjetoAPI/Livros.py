from sqlalchemy import Integer, String, Table, create_engine
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase, Session
engine = create_engine("sqlite:///Livros.db", echo=True)





class Base(DeclarativeBase):
  ...
class Livro(Base):
    __tablename__ = 'Livros'
    id:Mapped[int] = mapped_column(primary_key=True, nullable=True)
    nome_livro:Mapped[str]=mapped_column(String(100))
    quantidade_livro:Mapped[int]=mapped_column(Integer)


Base.metadata.create_all(engine)