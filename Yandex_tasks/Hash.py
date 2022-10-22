"""
Создать мультимножество.
Используем хешфункцию F(x) = x % setsize
Так, для 27 хешномер будет F(27) = 27 % 10 = 7

"""


class Hashtable():
    def __init__(self, setsize):
        self.setsize = setsize
        self.myset = [[] for _ in range(setsize)]

    def add(self, x):
        self.myset[x % self.setsize].append(x)

    def find(self, x):
        for val in self.myset[x % self.setsize]:
            if x == val:
                return True
        return False

    def print_table(self):
        print(self.myset)

    def delete(self, x):
        sub_list = self.myset[x % self.setsize]
        for i in range(len(sub_list)):
            if sub_list[i] == x:
                sub_list[i] = sub_list[-1]
                sub_list.pop()


if __name__ == '__main__':
    table = Hashtable(setsize=10)
    table.add(1)
    table.add(2)
    table.print_table()
    table.delete(2)
    table.print_table()
