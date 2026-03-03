# 08_classes.py
class Avenger:
    def __init__(self, name, age, gender, power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.weapon = weapon

    def get_info(self):
        print(self.name, self.power, self.weapon)

    def is_leader(self):
        if self.name == "Captain America":
            return True
        return False

cap = Avenger("Captain America", 100, "Male", "Strength", "Shield")
iron = Avenger("Iron Man", 45, "Male", "Technology", "Armor")

cap.get_info()
print("Leader:", cap.is_leader())