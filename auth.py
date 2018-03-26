import hashlib
import string
import random


class User:
    ID = 0

    def __init__(self, username, password, secret_question, email):
        """
        Create a new user object. The password
        will be encrypted before storing.
        :param username: str
        :param password: str
        :param secret_question: str
        :param email: str
        :param rights: str
        """
        self.username = username
        self._password = self._encrypt_pw(password)
        self.is_logged_in = False
        self.ID = User.ID
        self._secret_question = self._encrypt_pw(secret_question)
        self.status = True
        self.email = email

    def _encrypt_pw(self, password):
        """
        Encrypt the password with the username and return
        the sha digest.
        :param password: str
        :return: str
        """
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        Return True if the password is valid for this
        user, false otherwise
        :param password: str
        :return: Bool
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self._password

    def CAPTCHA(self):
        """
        return Captcha
        :return: str
        """
        letters = string.ascii_letters
        captcha = ''
        for i in range(4):
            captcha += random.choice(letters)
        self._captcha = captcha
        return captcha

    def check_captcha(self, captcha):
        """
        Return true if captcha is True, false otherwise
        :param captcha: str
        :return: bool
        """
        return captcha == self._captcha

    def check_secret_question(self, secret_question):
        """
        Return true if captcha is True, false otherwise
        :param secret_question:
        :return:
        """
        encrypted = self._encrypt_pw(secret_question)
        return encrypted == self._secret_question

    def send_email(self):
        """
        send something to email
        :return: None
        """
        print("Send mail.We closed your profile because someone tried log")
        print(" in it too many times")
        self.status = False


class AuthException(Exception):
    def __init__(self, username, user=None):
        """
        initialise class
        :param username: str
        :param user: User
        """
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class InvalidSecret_question(AuthException):
    pass


class Secret_questionTooShort(AuthException):
    pass


class Authenticator:
    def __init__(self):
        """
        Construct an autenticator to manage
        users logging in and out.
        """
        self.users = {}

    def add_user(self, username, password, secret_question, email):
        """
        add new user
        :param username: str
        :param password: str
        :param secret_question: str
        :param email: str
        :return: None
        """
        if username in self.users:
            raise UsernameAlreadyExists
        if len(password) < 6:
            raise PasswordTooShort
        if len(secret_question) < 4:
            raise Secret_questionTooShort
        self.users[username] = User(username, password, secret_question, email)

    def login(self, username, password, secret_question):
        """
        login in program
        :param username: str
        :param password: str
        :param secret_question: str
        :return: bool
        """
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        if not user.check_secret_question(secret_question):
            raise InvalidSecret_question(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        """
        test if user if logged
        :param username: str
        :return: bool
        """
        if username in self.users:
            return self.users[username]. is_logged_in
        return False

authentificator = Authenticator()


class Authorizor:
    def __init__(self, authentificator):
        self.authentificator = authentificator
        self.permissions = {}

    def add_permission(self, perm_name):
        """
        Create a new permission that users can be added to
        :param perm_name:
        :return: None
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user
        :param perm_name: str
        :param username: str
        :return: None
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authentificator.users:
                raise InvalidUsername(username)
            perm_set.add(username)


def check_permission(self, perm_name, username):
        """
        check if permission exist
        :param perm_name: str
        :param username: str
        :return: bool
        """
        if not self.authentificator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True
authorizor = Authorizor(authentificator)
