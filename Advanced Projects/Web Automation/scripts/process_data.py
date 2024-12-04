import pandas as pd

df = pd.read_csv('data/books.csv')
df['price'] = df['price'].str.replace('£', '').astype(float)
df.to_csv('data/cleaned_books.csv', index=False)
