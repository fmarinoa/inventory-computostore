from datetime import datetime


class User:
    def __init__(self, username: str, password: str, name: str, email: str, role: str = "admin"):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email
        self.__role = role
        self.__date_creation = datetime.now()
        self.__status = True

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def date_creation(self):
        return self.__date_creation

    @date_creation.setter
    def date_creation(self, date_creation: datetime):
        self.__date_creation = date_creation

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: bool):
        self.__status = status

    def __str__(self):
        date_str = self.date_creation.strftime("%d/%m/%Y %H:%M:%S") if isinstance(self.date_creation, datetime) else str(self.date_creation)
        status_str = "Active" if self.status else "Inactive"
        return (
            f"Usuario: {self.username}, Nombre: {self.name}, Email: {self.email}, "
            f"Rol: {self.role}, Fecha de creación: {date_str}, Estado: {status_str}"
        )

    def verify_user(self, username) -> bool:
        return self.username == username

    def verify_password(self, password) -> bool:
        return self.password == password
    
    def verify_status(self) -> bool:
        return self.status