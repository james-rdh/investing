import psycopg2
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PostgresqlDAO:
    def __init__(self, db):
        self.db = db
        connection_string = get_connection_string(DB_CONFIG)
        conn = psycopg2.connect(connection_string)
        logger.info("Connected to the database!")
        return conn
    except psycopg2.Error as e:
        logger.error(f"Error connecting to the database: {e}")
        raise
   
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

    def delete(self, table, object_id):
        obj = self.get_by_id(table, object_id)
        if obj:
            self.db.delete(table, obj)
            self.db.commit()
        return obj
    
class DAOFactory:
    @staticmethod
    def get_dao(db):
        return PostgresqlDAO(db)