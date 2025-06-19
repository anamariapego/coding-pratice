from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from typing import List
from src.domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        """
        Método para inserir um usuário no banco de dados.
        """
        with DBConnectionHandler() as db_handler:
            try: 
                new_register = UsersEntity(first_name=first_name, last_name=last_name, age=age)
                db_handler.session.add(new_register)
                db_handler.session.commit()

            except Exception as e:
                db_handler.session.rollback()
                print(f"An error occurred while inserting user: {e}")
            finally:
                db_handler.session.close()

    @classmethod
    def get_all_users(cls) -> None:
        """
        Método para obter todos os usuários do banco de dados.
        """
        with DBConnectionHandler() as db_handler:
            try:
                users = db_handler.session.query(UsersEntity).all()
                return users
            except Exception as e:
                print(f"An error occurred while fetching users: {e}")
                return None
            finally:
                db_handler.session.close()

    @classmethod
    def get_user_by_first_name(cls, first_name: str) -> List[Users]:
        """
        Método para obter um usuário pelo ID.
        """
        with DBConnectionHandler() as db_handler:
            try:
                user = db_handler.session.query(UsersEntity).filter(UsersEntity.first_name == first_name).first()
                return user
            except Exception as e:
                print(f"An error occurred while fetching user by ID: {e}")
                return None
            finally:
                db_handler.session.close()

    @classmethod
    def update_user(cls, user_id: int, first_name: str, last_name: str, age: int) -> None:
        """
        Método para atualizar um usuário no banco de dados.
        """
        with DBConnectionHandler() as db_handler:
            try:
                user = db_handler.session.query(UsersEntity).filter(UsersEntity.id == user_id).first()
                if user:
                    user.first_name = first_name
                    user.last_name = last_name
                    user.age = age
                    db_handler.session.commit()
                else:
                    print(f"User with ID {user_id} not found.")
            except Exception as e:
                db_handler.session.rollback()
                print(f"An error occurred while updating user: {e}")
            finally:
                db_handler.session.close()

    @classmethod
    def delete_user(cls, id: int) -> None:
        """
        Método para deletar um usuário do banco de dados.
        """
        with DBConnectionHandler() as db_handler:
            try:
                user = db_handler.session.query(UsersEntity).filter(UsersEntity.id == id).first()
                if user:
                    db_handler.session.delete(user)
                    db_handler.session.commit()
                else:
                    print(f"User with ID {id} not found.")
            except Exception as e:
                db_handler.session.rollback()
                print(f"An error occurred while deleting user: {e}")
            finally:
                db_handler.session.close()
