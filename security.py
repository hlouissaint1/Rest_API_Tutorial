__author__ = "Himmler Louissaint"

from werkzeug.security import safe_str_cmp
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from models.user import UserModel


def authenticate(username, password):
     user = UserModel.find_by_username(username)
     if user.username and safe_str_cmp(password, user.password):
         return {'username': username, 'password': password}


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


if __name__ == '__main__':
    user = authenticate('kara', 'nami')
 #   print(user)
