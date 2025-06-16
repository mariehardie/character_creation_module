'''
Main.py is a module containing the game code.
The player chooses the character, decides what it does, and accumulates
points based on its actions in the game. The "Skip" option allows the player
to escape from the game. Functions can be exported.
'''


from random import randint
from graphic_arts.start_game_banner import run_screensaver


# def attack(char_name: str, char_class: str) -> str:
#     '''Attack according to the character and add points.
#     Function returns status if player doesn't attack.
#     '''
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику {5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику {5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику {5 + randint(-3, -1)}')
#     return f'{char_name} не атакует.'


# def defence(char_name: str, char_class: str) -> str:
#     '''Function blocks according to the character and demonstrates points
#     of damage. Function returns status if player doesn't defend.
#     '''
#     if char_class == 'warrior':
#         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
#     if char_class == 'mage':
#         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
#     if char_class == 'healer':
#         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
#     return f'{char_name} не блокирует.'


# def special(char_name: str, char_class: str) -> str:
#     '''Player chooses a super power and earns points.
#     Function returns status in case of not using a special power.'''
#     if char_class == 'warrior':
#         return (f'{char_name} применил умение «Выносливость {80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил умение «Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил умение «Защита {10 + 30}»')
#     return f'{char_name} не использует суперсилу.'


# def start_training(char_name: str, char_class: str) -> str:
#     '''
#     Function for training a character. When player has already chosen his or
#     her character and chooses what it will do. Player can choose 'skip'.
#     '''
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи на выбор: attack, defence, special.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd = ''
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'


# def choice_char_class() -> str:
#     '''
#     Player chooses a character and confirms it with 'Y'.
#     '''
#     approve_choice = None
#     char_class = None
#     while approve_choice != 'y':
#         char_class = input('Выбери: warrior, mage, healer: ')
#         if char_class == 'warrior':
#             print('Воитель — дерзкий воин ближнего боя.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный врач.')
#         approve_choice = input('Нажми (Y) или выбери др. персонажа: ').lower()
#     return char_class


# if __name__ == '__main__':
#     """
#     Block for greeting and running all the game with an animation.
#     """
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class = choice_char_class()
#     print(start_training(char_name, char_class))


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80 


class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name
        
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} нанёс противнику урон, равный {value_defence}')

    def special(self):
        return (f'{self.name} применил специальное умение. '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')
    
    def __str__(self):
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')


class Warrior(Character):
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = 'дерзкий воин ближнего боя.'


class Mage(Character):
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = 'находчивый воин дальнего боя.'


class Healer(Character):
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = 'могущественный врач.'


def choice_char_class(char_name: str) -> Character:
    game_classes = {
         'warrior': Warrior,
         'mage': Mage,
         'healer': Healer
                    }
    approve_choice: str = None
    run_screensaver()
    while approve_choice != 'y':
        selected_classes = input('Введи название персонажа персонажа: '
                                 'за которого хочешь играть: '
                                 'Воитель — warrior,'
                                 'Маг — mage, Лекарь — healer: ').lower()
        char_class: Character = game_classes[selected_classes](char_name)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор'
                               'или выбери др. персонажа: ').lower()
    return char_class


def start_training(character: Character) -> str:
    print(character)
    print('Потренируйся управлять своими навыками.')
    commands = {
        'attack': character.attack(),
        'defence': character.defence(),
        'special': character.special()
    }
    cmd: str = None
    while cmd != 'skip':
        selected_command = input('Введи одну из команд: ' 
                                 'attack — чтобы атаковать противника, '
                                 'defence — чтобы блокировать атаку противника, '
                                 'special — чтобы использовать свою суперсилу: '
                                 )
        chosen_command = commands[selected_command]
        print(chosen_command)
        cmd = input('Если хочешь покинуть игру, введи комманду skip: ').lower()
    return 'Тренировка окончена'


warrior = choice_char_class('Кодослав')
print(start_training(warrior))