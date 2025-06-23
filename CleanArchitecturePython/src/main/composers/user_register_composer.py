from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController

# Método que juntas os componentes para formar o controller
def user_register_composer():
    repository = UsersRepository()
    use_case = UserRegister(repository)
    controller = UserRegisterController(use_case)

    return controller.handle
