from idlelib.debugger_r import close_subprocess_debugger

class Mybio():
    pass
name_1 = Mybio()
name_1.one = "Harsha"
name_1.two = "Madhu"
name_1.three = "Dinesh"

print(name_1.one, name_1.two, name_1.three)

name_2 = Mybio()

name_2.harsha = "CSE"
name_2.madhu = "B.COM"
name_2.dinesh = "EEE"

print(name_2.madhu, name_2.dinesh, name_2.harsha)

print ("======================= C O N S T R U C T O R =======================")


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("001", "Dinesh")
user_2 = User("002", "Harsha")







