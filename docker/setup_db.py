# Import client library
import json
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

qdrant_client = QdrantClient("http://localhost:6333")
qdrant_client.recreate_collection(
    collection_name="startups",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)
fd = open("./startups_demo.json")
# payload is now an iterator over startup data
payload = map(json.loads, fd)
# Load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if you don't want to load all data into RAM
vectors = np.load("./startup_vectors.npy")

qdrant_client.upload_collection(
    collection_name="startups",
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256,  # How many vectors will be uploaded in a single request?
)