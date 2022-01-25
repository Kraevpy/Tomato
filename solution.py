class Tomato:
    '''Статическое свойство states {} <-- dictionary хранит все стадии созревания томата'''

    states = {
        0: 'Отсутствует',
        1: 'Цветение',
        2: 'Зеленые',
        3: 'Красные'}

    '''Метод сожержит 2 динамических свойства 1.index <-- который передается пораметром
                                              2._state <-- принимает первое значение из словаря states 
                                              по умолчанию _state = 0'''

    def __init__(self, index):
        self._index = index
        self._state = 0

    '''Метод grow() переводит все томаты которые не созрели на следующую стадию созревания в функции _tomato_state()
      котрую вызываю в методе grow(), не знаю зачем это ебалово придумали по условию задачи, просто лишний метод :)
      единственное что можно вывести из него это томаты переведенные на следующую стадию, но для этого у меня есть метод 
      _print_state() по условию..........................??? :) '''

    def grow(self):
        self._tomato_state()

    '''Метод is_ripe() позволяет выяснить созрел ли томат, если не созрел то в какой стади созревания находится
     т.к под key 3 в dictionary хранится значение "красный", в условии выясняю если томат "красный" он созрел'''

    def is_ripe(self):
        if self._state == 3:
            return f'Томат --> {self._state}'
        return f'Томат --> {self._state}'

    def _tomato_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Томат {self._index} -->  {Tomato.states[self._state]}')


class TomatoBush:

    '''Метод принимает в качестве параметра количество томатов и на его основе
-- создается список объектов класса Tomato, этот список храниться внутри tomatoes.'''

    def __init__(self, number_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(0, number_tomatoes)]

    '''Метод grow_all()  переводит все объекты из списка томатов на следующий этап созревания'''

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    '''В методе all_are_ripe() функция all() будет возвращать True, если все томаты из списка стали спелыми "True" 
    builtins.py <-- def all(*args, **kwargs): # real signature unknown
    Return True if bool(x) is True for all values x in the iterable.
    If the iterable is empty, return True.
    '''

    def all_are_ripe(self) -> bool:
        for tomato in self.tomatoes:
            return all(tomato.is_ripe())

    '''в этом методе give_away_all() собираем уражай'''

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    '''В методе  определены два динамических свойства:
       1) name - передается параметром, является публичным и 2) _plant - принимает объект класса class Tomato:'''

    def __init__(self, name, plant):
        self._plant: TomatoBush = plant
        self.name = name

    '''Метод work() заставляет садовника работать, что позволяет растению становиться более зрелым'''

    def work(self):
        print(f'{self.name} работает')
        self._plant.grow_all()

    '''Метод harvest() проверяет если томаты созрели то садовнику нужно их собрать, если не созрели
       получаем придупреждение что томаты еще нельзя собирать '''

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f'{self.name} пошел собирает уражай томаты уже созрели')
        else:
            print('Томаты еще нельзя собирать, они не созрели')

    '''@staticmethod <-- knowledge_base() просто печатает информацию о сборке томатов
       в какой переуд их можно собирать '''

    @staticmethod
    def knowledge_base(name_gardener):
        print(f'{name_gardener} собирает томаты только когда они созрели ')


Gardener.knowledge_base(name_gardener="Leva")
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Leva', great_tomato_bush)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()