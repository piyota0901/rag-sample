from qdrant_client import QdrantClient
from .database import get_qdrant_client
from .interfaces import IClientProvider

class QdrantClientProvider(IClientProvider):
    def get_client(self) -> QdrantClient:
        return get_qdrant_client()