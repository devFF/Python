class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_alive(age):
        return 0 < age < 85


# Обращение от имени класса:
print(Human.is_alive(25))

# Обращение от экземпляра:
igor = Human('Igor')
print(igor.is_alive(25))
