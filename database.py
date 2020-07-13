import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Credentials for DataBase connection
DBUSER = 'postgres'
DBPASS = 'test123'
DBHOST = 'db_pg'
DBPORT = '5432'
DBNAME = 'SIHA_postgres'

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user=DBUSER,
        password=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME))

db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
        import models
        Base.metadata.create_all(bind=engine)