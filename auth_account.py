from auth import *

# Set up a test user and permission
authentificator.add_user("joe", "joepassword", "Mother", "joe@gmail.com")
authorizor.add_permission("test program")
authorizor.add_permission("change program")
authorizor.permit_user("test program", "joe")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }

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

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            secret_question = input("secret question: ")
            captcha = input("input {}: ".format(self.CAPTCHA()))
            while not self.check_captcha(captcha):
                captcha = input("input {}: ".format(self.CAPTCHA()))
            try:
                logged_in = authentificator.login(username, password,\
                                                  secret_question)
            except InvalidUsername:
                print("Sorry, that username does not exist")
            except InvalidPassword:
                print("Sorry, Incorect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            authorizor.check_permission(
                permission, self.username)
        except NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except NotPermittedError as e:
            print("{} cannot {}".format(
                e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemExit

    def menu(self):
        try:
            answer = ""
            while True:
                while True:
                    print("""
    Please enter a command:
    \tlogin\tLogin
    \ttest\tTest the program
    \tchange\tChange the program
    \tquit\tQuit
                    """)
                    answer = input("enter a comand: ").lower()
                    try:
                        func = self.menu_map[answer]
                    except KeyError:
                        print("{} is not a valid option".format(
                            answer))
                    else:
                        func()
        finally:
            print("Thank you for testing the auth module")
Editor().menu()
