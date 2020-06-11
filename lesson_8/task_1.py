# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter


class MyNode:                                   # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, value):                # метод для обхода дерева
        self.left.walk(code, value + ['0'])
        self.right.walk(code, value + ['1'])


class Leaflet:                                  # класс для листков дерева, у него нет потомков
    def __init__(self, char):
        self.char = char

    def walk(self, code, value):                # потомков у листков нет
        code[self.char] = ''.join(value)        # если строка длиной 1 то value = ''


def _make_leaflets(obj: str):                   # функция для создания листьев
    new_counted = {}
    for key, val in dict(Counter(obj)).items():
        new_counted[Leaflet(key)] = val
    return list(new_counted.items())


def huffman_encode(string_):                    # функция кодирования строки в коды Хаффмана
    items = _make_leaflets(string_)
    while len(items) >= 2:
        left_leaflet = items.pop()
        right_leaflet = items.pop()
        leaflet_count = left_leaflet[1] + right_leaflet[1]
        items.append((MyNode(left=left_leaflet[0], right=right_leaflet[0]), leaflet_count))
        items.sort(key=itemgetter(1), reverse=True)
    _node = items.pop()[0]
    code = {}
    _node.walk(code, [])
    for key in code:                            # в цикле for проходим по ключам словаря и выводим ключ -> значение
        print(key, '->', code[key])
    for i in string_:                           # в цикле for проходим по строке и выводим значения ключей словаря
        print(code[i], end='')


if __name__ == '__main__':
    huffman_encode(input('Введите строку или слово для кодирования: '))

