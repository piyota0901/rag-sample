from typing import List, Union
import numpy as np
import injector
from torch import Tensor
from qdrant_client import QdrantClient
from mypackage.dataaccess.interfaces import IRepository, IClientProvider
from mypackage.domain.models import Startup
from qdrant_client.models import ScoredPoint

class StartupsRepository(IRepository):
    @injector.inject
    def __init__(self, client_provider: IClientProvider):
        self.client: QdrantClient = client_provider.get_client()

    def find(self, vector: Union[List[Tensor], np.ndarray, Tensor], limit: int = 10) -> List[Startup]:
        results: List[ScoredPoint] = self.client.search(
            collection_name="startups",
            query_vector=vector,
            query_filter=None,
            limit=limit,
        )
        startups = [Startup(id=result.id, score=result.score, **result.payload) for result in results]
        return startups

    def save(self):
        pass

    def delete(self):
        pass