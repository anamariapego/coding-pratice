from abc import ABC, abstractmethod
from src.domain.models.users import Users
from typing import List

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass
       
    @abstractmethod
    def get_user_by_first_name(self, first_name: str) -> List[Users]: pass