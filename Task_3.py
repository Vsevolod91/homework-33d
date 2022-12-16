class MyList(list):
    def __new__(cls, *args, **kwargs):
        print("Работает магический метод __new__")
        return super().__new__(cls)

    def __init__(self, lst):
        print("Работает магический метод __init__")
        self.__lst = lst

    def __str__(self):
        print("Работает магический метод __str__")
        return f"{self.__lst}"

    def __setitem__(self, key, value):
        print("Работает магический метод __setattr__")
        self.__lst[key] = value

    def __getitem__(self, item):
        print("Работает магический метод __getattr__")
        return self.__lst[item]

    def __len__(self):
        print("Работает магический метод __len__")
        return len(self.__lst)


if __name__ == "__main__":
    lst = MyList(['Jone', 'Snow', 'Java'])

    if not lst[2] == 'Python':
        lst[2] = 'Python'

    print(lst)
    print(len(lst))