# 1
class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return f"{self.price * 15.6} Egyptian Pounds"


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")
print("#" * 10)


# 2
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def full_details(self):
        return f"Hello {'Mr ' if self.gender == 'Male' else 'Mrs '}{self.first_name}, [{40 - self.age}] Years to Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())
print(user_two.full_details())
print("#" * 10)


# 3
class Message:
    @staticmethod
    def print_message():
        return "Hello From Class Message"


print(Message.print_message())
print("#" * 10)


# 4
class Games:

    def __init__(self, game):
        self.game = game

    def show_games(self):
        if isinstance(self.game, str):
            print(f'I Have One Game Called "{self.game}"')
        elif isinstance(self.game, list):
            print("I Have Many Games:")
            for game in self.game:
                print(f"-- {game}")
        elif isinstance(self.game, int):
            print(f"I Have Game {self.game}")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()
print("#" * 10)


# 5
class Members:

    def __init__(self, n, p):
        self.name = n

        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)


class Moderators(Members):
    def __init__(self, n, p):
        super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
print(member_two.show_info())
print("#" * 10)


# 6
class A:

    def __init__(self, one):
        self.one = one


class B:

    def __init__(self, two):
        self.two = two


class C:

    def __init__(self, three):
        self.three = three


class Name(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name is {self.one}{self.two}{self.three}"


the_name = Name("El", "ze", "ro")

print(the_name.show_name())
