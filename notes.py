# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, fc = "", a = 0, w = 0.0, n = "") -> None:
        self.fur_color = fc
        self.age = a
        self.weight = w
        self.name = n
        self.fetch_count = 0

    def __str__(self) -> str:
        s = "Dog's name is " + self.name + "\n"
        s += "and their age is " + str(self.age) + "\n"
        s += "and their fur color is " + self.fur_color + "\n"
        return s
    
    def play_fetch(self, iterations):
        self.fetch_count += iterations

dog1 = Dog("brown", 9, 25.3, "scotch")
dog2 = Dog("black", 3, 100, "logan")

# print(dog1)

dog1.play_fetch(20)
dog2.play_fetch(15)

print(f"{dog1} has played fetch {fetch_count} times")