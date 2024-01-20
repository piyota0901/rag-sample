from pydantic import BaseModel


class StartupSchema(BaseModel):
    id: int
    score: float
    name: str
    alt: str
    description: str
    link: str
    city: str
    images: str