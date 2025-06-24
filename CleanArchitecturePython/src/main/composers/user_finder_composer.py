from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_finder_composer():
    """
    Função responsável por compor o controller da funcionalidade de busca de usuário.

    Junta os componentes da Clean Architecture:
    - Repositório (camada de infraestrutura)
    - Caso de uso (camada de aplicação)
    - Controller (camada de apresentação)

    Return: 
        Método `handle` do controller, pronto para ser usado no adaptador de rota
    """
    repository = UsersRepository()             # Camada de infraestrutura (acesso a dados)
    use_case = UserFinder(repository)          # Camada de aplicação (lógica de negócio)
    controller = UserFinderController(use_case)  # Camada de apresentação (controle da entrada)

    return controller.handle
