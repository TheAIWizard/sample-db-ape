import pandas as pd
import pyarrow.parquet as pq
import numpy as np

# Charger le DataFrame depuis le fichier Parquet
df = pq.read_table('chemin_vers_votre_fichier.parquet').to_pandas()

# Convertir la colonne de dates en format datetime si ce n'est pas déjà fait
df['date_column'] = pd.to_datetime(df['date_column'])

# Filtrer les lignes à partir du 1er janvier 2023
df = df[df['date_column'] >= '2023-01-01']

# Extraire n lignes au hasard uniformément
n = 10  # Remplacez 10 par le nombre de lignes que vous souhaitez extraire
random_rows = df.sample(n)

# Afficher les lignes extraites
print(random_rows)

# Sauvegarder le résultat dans un nouveau fichier Parquet
output_file = 'chemin_vers_output.parquet'
pq.write_table(pa.Table.from_pandas(random_rows), output_file)
