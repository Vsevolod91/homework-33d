class TeamIterator:
    def __init__(self, team):
        self.team_jun = team._juniorMembers
        self.team_sen = team._seniorMembers
        self.start_jun = 0
        self.stop_jun = len(self.team_jun)
        self.start_sen = 0
        self.stop_sen = len(self.team_sen)
        self.step = 1
        self.value_jun = -1
        self.value_sen = -1

    def __next__(self):
        if self.stop_jun - self.value_jun > 1:
            if self.value_jun + self.step < self.stop_jun:
                self.value_jun += self.step
                return self.team_jun[self.value_jun], "junior"
            else:
                raise StopIteration
        else:
            if self.value_sen + self.step < self.stop_sen:
                self.value_sen += self.step
                return self.team_sen[self.value_sen], "senior"
            else:
                raise StopIteration

class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()