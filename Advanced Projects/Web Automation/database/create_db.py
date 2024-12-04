import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/books.db')
df = pd.read_csv(r"/data/books.csv")
df.to_sql('books', engine, index=False, if_exists='replace')
print("Database created and data saved to database/books.db")
