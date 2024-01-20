import injector
from mypackage.dataaccess.interfaces import IRepository
from mypackage.domain.models import Startup
from mypackage.core.machine_learning import text2vector

class StartupsService:
    @injector.inject
    def __init__(self, repository: IRepository):
        self.repository = repository

    def find(self, text: str, limit: int = 10) -> list[Startup]:
        vector = text2vector(text)
        return self.repository.find(vector=vector, limit=limit)

    def save(self):
        pass

    def delete(self):
        pass