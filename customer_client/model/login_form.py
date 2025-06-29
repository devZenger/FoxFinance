from service import ServerRequest

from .model_utilites import check_email


class LoginForm:
    def __init__(self):
        self._email = ""
        self._password = ""
        self.response = ""

        self.form_names = {"email": "Email Adresse",
                           "password": "Passwort_Login"}

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, input: str):
        check = check_email(input)
        if check:
            self._email = input
        else:
            raise ValueError("Ungültige Eingabe")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, input: str):
        if len(input) >= 12:
            self._password = input
        else:
            raise ValueError("Passwort ist zu kurz, min. 12 Zeichen")

    def to_dict(self):
        return {
            "email": self.email,
            "password": str(self.password)
        }

    def post_login_form(self) -> bool:

        to_transmit = self.to_dict()

        url_part = "token"

        server_request = ServerRequest()

        success, self.response = server_request.make_post_request(url_part=url_part,
                                                                  token=None,
                                                                  to_transmit=to_transmit)

        return success
