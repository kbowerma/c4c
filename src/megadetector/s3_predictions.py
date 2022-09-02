# RUN MEGADETECTOR ON S3 IMAGES
import boto3
import errno
import os

# Set working directory to current file directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Setup S3 client
session = boto3.Session(profile_name="yerc")
s3_client = session.client("s3")

# Functions to download files from folder recursively
def assert_dir_exists(path):
    """
    Checks if directory tree in path exists. If not it created them.
    :param path: the path to check if it exists
    """
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def download_dir(client, bucket, path, target):
    """
    Downloads recursively the given S3 path to the target directory.
    :param client: S3 client to use.
    :param bucket: the name of the bucket to download from
    :param path: The S3 directory to download.
    :param target: the local directory to download the files to.
    """

    # Handle missing / at end of prefix
    if not path.endswith("/"):
        path += "/"

    paginator = client.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket, Prefix=path):
        # Download each file individually
        for key in result["Contents"]:
            # Calculate relative path
            rel_path = key["Key"][len(path) :]
            # Skip paths ending in /
            if not key["Key"].endswith("/"):
                local_file_path = os.path.join(target, rel_path)
                # Make sure directories exist
                local_file_dir = os.path.dirname(local_file_path)
                assert_dir_exists(local_file_dir)
                client.download_file(bucket, key["Key"], local_file_path)


# Specify vars
BUCKET_NAME = "epiic-c4c-prod"
S3_DIR = "2020 WildNET Camera Downloads/Sphinx Creek/06.10.2020/100_BTCF/"
LOCAL_DIR = "s3_images/sphinx_creek/"

# Download files from S3_DIR
download_dir(s3_client, BUCKET_NAME, S3_DIR, LOCAL_DIR)
