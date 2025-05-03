class User:
    def __init__(self, username, password, firstname, lastname, phone):
        self.__username = username
        self.__password = password
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phone = phone

    @property
    def firstname(self):
        return self.__firstname.capitalize()

    @firstname.setter
    def firstname(self, new_fname):
        self.__firstname = new_fname



    @property
    def lastname(self):
        return self.__lastname.capitalize()

    @lastname.setter
    def lastname(self, new_lname):
        self.__laststname = new_lname

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_user):
        self.__username = new_user

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    def __str__(self):
        return f"Username: {self.username}, Name: {self.firstname} {self.lastname}, Phone: {self.phone}"


class ClassBooking(User):
    def __init__(self, username, password, firstname, lastname, phone, selected_classes):
        super().__init__(username, password, firstname, lastname, phone)
        self.selected_classes = selected_classes

    def __str__(self):
        return f"User: {self.firstname} {self.lastname}, Classes: {', '.join(self.selected_classes)}"

class TrainerBooking(User):
    def __init__(self, username, password, firstname, lastname, phone, selected_trainer_name):
        super().__init__(username, password, firstname, lastname, phone)
        self.selected_trainer_name = selected_trainer_name

    def __str__(self):
        return f"User: {self.firstname} {self.lastname}, Trainer: {self.selected_trainer_name}"

