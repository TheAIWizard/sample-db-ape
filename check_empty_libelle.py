import pyarrow.parquet as pq
import pandas as pd


df = pq.read_table("/home/onyxia/work/sample-db-ape/20240124_sirene4.parquet").to_pandas()

# Filtrer les lignes avec des chaînes vides dans la colonne spécifiée
lignes_vides = df.loc[df['liasse_numero'] == "J00019990357"]

# Afficher le DataFrame résultant
print(df[df["activ_pr_lib_et"].apply(lambda x: x == '' or x is None)])
print(pd.to_datetime(df['date_modification']).min().strftime("%Y%m%d"))
print(df[(df['activ_pr_lib_et'] != df['activ_pr_lib'])][["activ_pr_lib","activ_pr_lib_et"]])
print(df["evenement_type"].unique())
print(df["activ_pr_lib_et"]=="La société a pour objet, tant en France qu'à l'étranger : - Conception et fabrication d'aménagements intérieurs personnalisés ; - Installati   (ligne 809)")