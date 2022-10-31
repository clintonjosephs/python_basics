# To make a variable or method private you can just add two underscores to it
# Abstract classes are used to hide data and methods from the user, 
# it cannot be instantiated and can only be accessed via inheritance
# Abstract classes are used to create a template for other classes to follow

from abc import ABC, abstractmethod
# decorator is used to add meta data to a function

class User:
    first_name = ''
    last_name = ''
    email = ''
    phone_number = ''
    alias = ''
    password = ''

class UserAbstract(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass
    
    @abstractmethod
    def  get_all_users(self):
        pass
    
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class UserManager(UserAbstract):
    def create_user(self, user: User):
        print('User created')

    def get_all_users(self):
        print('All users')

    def get_user_by_id(self, user_id):
        print('User with id: ' + str(user_id))

user_manager = UserManager()
user_manager.create_user(User())