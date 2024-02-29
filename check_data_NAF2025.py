import os
import s3fs
import pyarrow.parquet as pq


def read_from_s3(bucket: str, path: str):
    fs = s3fs.S3FileSystem(
        client_kwargs={"endpoint_url": "https://" + "minio.lab.sspcloud.fr"},
        key=os.getenv("AWS_ACCESS_KEY_ID"),
        secret=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    # Read Parquet files directly into a single table
    dataset = pq.ParquetDataset(
        f"s3://{bucket}/{path}/",
        filesystem=fs
    )
    table = dataset.read()
    return table

# Example usage:
bucket_name = "projet-ape"
path_in_bucket = "NAF-revision/correspondance_NAF.parquet"
table_from_s3 = read_from_s3(bucket_name, path_in_bucket)
print(table_from_s3["NAF2008"])
