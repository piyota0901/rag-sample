from fastapi import APIRouter
from mypackage.application import startup_application

router = APIRouter(prefix="/startups", tags=["startups"])

@router.get("/health")
def health():
    return {"status": "ok"}

# query="xx"を受け取って、StartupsService.find()を呼び出す
@router.get("/")
def search(keyword: str, limit: int = 10):
    return startup_application.search_startups(keyword=keyword, limit=limit)

@router.get("/rag/")
def rag_search(query: str) -> str:
    return startup_application.search_by_rag(query=query)