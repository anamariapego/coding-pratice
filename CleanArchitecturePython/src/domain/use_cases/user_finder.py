from abc import ABC, abstractmethod
from typing import Dict

# Interface 
class UserFinder(ABC):
    @abstractmethod
    def find_user(self, first_name: str) -> Dict:
        pass