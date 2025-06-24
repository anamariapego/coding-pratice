from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController

def user_register_composer():
    """
    Função responsável por compor o controller da funcionalidade de registro de usuário.

    Junta os componentes da Clean Architecture:
    - Repositório (infraestrutura)
    - Caso de uso (aplicação)
    - Controller (apresentação)

    Return: 
        Método `handle` do controller, pronto para ser usado no adaptador de rota
    """
    repository = UsersRepository()               # Camada de infraestrutura (acesso ao banco)
    use_case = UserRegister(repository)          # Camada de aplicação (regra de negócio)
    controller = UserRegisterController(use_case)  # Camada de apresentação (interface da aplicação)

    return controller.handle
