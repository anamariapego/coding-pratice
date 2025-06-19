from .user_finder import UserFinder
from src.infra.db.repositories.users_repository import UsersRepository

def test_find_user():
    repo = UsersRepository()
    user_finder = UserFinder(repo)
