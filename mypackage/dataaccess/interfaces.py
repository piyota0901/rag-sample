import abc
from typing import List, Union
import numpy as np

from torch import Tensor

from mypackage.domain.models import Startup

class IClientProvider(abc.ABC):
    @abc.abstractmethod
    def get_client(self):
        raise NotImplementedError

class IRepository(abc.ABC):
    @abc.abstractmethod
    def find(self, vector: Union[List[Tensor], np.ndarray, Tensor], limit: int) -> list[Startup]:
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, entity):
        raise NotImplementedError