import Singleton


class User(Singleton):

    def login(self, username, password):
        pass
        # returns userid

    def add_user(self, username, userid, password, confirm_password, email):
        pass

    def del_user(self, userid):
        pass

    def set_pass(self, userid, new_pass, confirm_pass):
        pass
