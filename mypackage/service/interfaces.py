import abc

class IStartupService(abc.ABC):
    @abc.abstractmethod
    def find_startup(self, id: int) -> list[]:
        pass