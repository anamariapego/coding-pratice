from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repo: UsersRepositoryInterface) -> None:
        self.users_repo = users_repo

    def find_user(self, first_name: str) -> Dict:
        pass
