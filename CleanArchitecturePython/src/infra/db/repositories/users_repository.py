from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):
    """
    Repositório que lida com a persistência de dados da entidade Users.
    """

    @classmethod
    def insert_user(cls, name: str, email: str, age: int) -> None:
        """
        Insere um novo usuário no banco de dados.
        """
        with DBConnectionHandler() as db_handler:
            try: 
                new_register = UsersEntity(name=name, email=email, age=age)
                db_handler.session.add(new_register)
                db_handler.session.commit()

            except Exception as e:
                db_handler.session.rollback()
                print(f"[ERROR] Failed to insert user: {e}")
            finally:
                db_handler.session.close()


    @classmethod
    def get_user_by_email(cls, email: str) -> List[Users]:
        """
        Busca usuários pelo email.
        """
        with DBConnectionHandler() as db_handler:
            try:
                user = db_handler.session.query(UsersEntity).filter(UsersEntity.email == email).first()
                return user
            except Exception as e:
                print(f"[ERROR] Failed to fetch users by email: {e}")
                return None
            finally:
                db_handler.session.close()
