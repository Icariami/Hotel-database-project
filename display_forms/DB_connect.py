import psycopg2

def connect():
    '''
    Function connecting to the PostgreSQL database.
    Used in the further part of the project.
    '''
    return psycopg2.connect(
        host = "localhost", 
        database = "Hotel",
        user = "postgres",
        password = "Strzelce0", 
        port = "5432",
        )



