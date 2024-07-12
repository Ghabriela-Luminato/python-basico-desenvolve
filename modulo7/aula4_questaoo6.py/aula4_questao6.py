# aula4_questao6.py

import csv

# Caminho para o arquivo Spotify CSV
spotify_file = "spotify-2023.csv"

# Lista para armazenar as músicas mais populares de cada ano
top_songs = []

# Processa o arquivo Spotify CSV
with open(spotify_file, "r", encoding="latin-1") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pula o cabeçalho
    
    for row in reader:
        # Verifica se o ano está no intervalo de 2012 a 2022
        released_year = int(row[3])
        if 2012 <= released_year <= 2022:
            # Verifica se o número de artistas é 1 (ignora múltiplos artistas)
            artist_count = int(row[2])
            if artist_count == 1:
                track_name = row[0]
                artist_name = row[1]
                streams = int(row[8])
                top_songs.append([track_name, artist_name, released_year, streams])

# Ordena as músicas pelo número de streams (em ordem decrescente)
top_songs.sort(key=lambda x: x[3], reverse=True)

# Seleciona as 10 músicas mais populares de cada ano
top_songs_by_year = {}
for song in top_songs:
    year = song[2]
    if year not in top_songs_by_year and len(top_songs_by_year) < 10:
        top_songs_by_year[year]
