import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Базовый класс для моделей
Base = declarative_base()


# Модель Subject
class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)


# Фикстура для подключения к БД
@pytest.fixture(scope='session')
def engine():
    return create_engine('postgresql://postgres:229@localhost:5432/QA')


# Фикстура для создания таблиц
@pytest.fixture(scope='session')
def create_tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


# Фикстура для сессии
@pytest.fixture
def db_session(engine, create_tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()