from pathlib import Path
import os


def manage_gcp_auth(cert_path=cert_path):
    """Make connection to gcp authenticated"""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(cert_path)