import os
from qdrant_client import QdrantClient

def get_qdrant_client():
    """Create a QdrantClient instance
    """
    url = "http://" + os.environ["QDRANT_HOST"] + ":" + os.environ["QDRANT_PORT"]
    return QdrantClient(url=url)