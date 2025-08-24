import pandas as pd
import json

# Lee el archivo CSV
df = pd.read_csv('movies_initial.csv')

# Guarda el DataFrame en formato JSONL (una línea por registro)
df.to_json('movies.json', orient='records', lines=True)

# Lista para guardar las películas
movies = []

# Lee el archivo JSONL línea por línea
with open('movies.json', 'r', encoding='utf-8') as file:
    for line in file:
        movies.append(json.loads(line))

# Imprime hasta 100 películas (aquí solo mostramos la primera por el break)
for i in range(min(100, len(movies))):
    movie = movies[i]
    print(movie)
    break
