import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

def text2vector(text: str) -> np.ndarray:
    """Converts text to vector

    Args:
        text (str): _description_

    Returns:
        np.ndarray: _description_
    """
    return MODEL.encode(text)