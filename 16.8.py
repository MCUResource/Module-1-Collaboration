from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///books.db")
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT title FROM books ORDER BY title ASC")
    )
    
    for row in result:
        print(row[0])
        