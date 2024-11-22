from .config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    """Creates database tables."""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully!")
    except SQLAlchemyError as e:
        print(f"Error creating database tables: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BaseDAO:
    def __init__(self, db):
        self.db = db
    
    def create(self, table, data):
        new_object = table(**data)
        self.db.add(new_object)
        self.db.commit()
        self.db.refresh(new_object)
        return new_object

    def get_by_id(self, table, object_id):
        return self.db.query(table).filter(table.id == object_id).first()
    
    def get_by_ids(self, table, object_ids):
        return self.db.query(table).filter(table.id.in_(object_ids)).all()

    def get_all(self, table):
        return self.db.query(table).all()

    def get_by_variables(self, table, variables):
        query = self.db.query(*[getattr(table, variable) for variable in variables])
        for variable, value in variables.items():
            query = query.filter(getattr(table, variable) == value)
        return query.all()

    def get_by_conditions(self, table, conditions):
        return self.db.query(table).filter_by(**conditions).all()

    def update(self, table, object_id, data):
        obj = self.get_by_id(table, object_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            self.db.commit()
            self.db.refresh(obj)
        return obj

    def delete(self, object_id):
        obj = self.get_by_id(object_id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
        return obj