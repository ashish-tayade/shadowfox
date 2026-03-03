# 09_inheritance.py
class MobilePhone:
    def __init__(self, front, rear, ram, storage):
        self.screen = "Touch Screen"
        self.network = "4G/5G"
        self.front = front
        self.rear = rear
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Calling...")

class Apple(MobilePhone):
    def __init__(self, front, rear, ram, storage):
        super().__init__(front, rear, ram, storage)

class Samsung(MobilePhone):
    def __init__(self, front, rear, ram, storage):
        super().__init__(front, rear, ram, storage)

iphone = Apple("12MP","48MP","4GB","64GB")
samsung = Samsung("8MP","32MP","3GB","32GB")

iphone.make_call()