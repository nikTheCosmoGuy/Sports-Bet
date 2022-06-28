from pathlib import Path
import os

project_name = None

def manage_gcp_auth(cert_path=cert_path):
    """Make connection to gcp authenticated"""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(cert_path)

bq_uri = None if project_name is None else f'bigquery://{project_name}'
