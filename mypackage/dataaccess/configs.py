import injector
from mypackage.dataaccess.interfaces import IClientProvider, IRepository
from mypackage.dataaccess.client_providers import QdrantClientProvider
from mypackage.dataaccess.repositories import StartupsRepository

class DevelopModule(injector.Module):
    def configure(self, binder):
        binder.bind(IClientProvider, to=QdrantClientProvider)
        binder.bind(IRepository, to=StartupsRepository)


def get_modules():
    return DevelopModule()