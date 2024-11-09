import random


class Cat:
    def __init__(self, name, age=0, health=100, energy=100):
        self.name = name
        self.age = age
        self.health = health
        self.energy = energy
        self.alive = True

    def live_day(self):
        if not self.alive:
            print(f"{self.name} больше не с нами.")
            return
        self.age += 1 / 365
        self.energy -= random.randint(5, 15)
        self.health -= random.randint(2, 10)
        print(f"{self.name} прожил ещё один день. Возраст: {self.age:.2f} лет, "
              f"Здоровье: {self.health}, Энергия: {self.energy}")

        if self.energy <= 0 or self.health <= 0:
            self.alive = False
            print(f"{self.name} ушел из жизни в возрасте {self.age:.2f} лет.")

    def eat(self, food_amount):
        if self.alive:
            self.energy += food_amount
            self.health += food_amount // 2
            if self.energy > 100:
                self.energy = 100
            if self.health > 100:
                self.health = 100
            print(f"{self.name} поел и восстановил силы. Энергия: {self.energy}, Здоровье: {self.health}")
        else:
            print(f"{self.name} больше не может есть.")

    def sleep(self, hours):
        if self.alive:
            self.energy += hours * 10
            if self.energy > 100:
                self.energy = 100
            print(f"{self.name} поспал и восстановил энергию. Энергия: {self.energy}")
        else:
            print(f"{self.name} больше не может спать.")

my_cat = Cat(name="Мурзик")

for _ in range(10):
    my_cat.live_day()
    if my_cat.alive:
        my_cat.eat(20)
        my_cat.sleep(3)
