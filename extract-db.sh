mc cp --recursive s3/projet-ape/extractions/20240124_sirene4.parquet ./
EXTRACT_DB=$(python extract-db.py "20240124_sirene4.parquet" "2500")
mc mv $EXTRACT_DB "s3/projet-ape/Label Studio/Annotation APE 2024/NAF 2008/Extract manuelle/"