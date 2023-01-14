import types


class FlatIterator:

    def __init__(self, any_list):
        self.any_list = any_list
        self.cursor = -1
        self.cursor_2 = 0
        self.list_len = len(any_list)

    def __iter__(self):
        self.cursor += 1
        self.cursor_2 = 0
        return self

    def __next__(self):
        if self.cursor_2 == len(self.any_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.cursor_2 += 1
        return self.any_list[self.cursor][self.cursor_2 - 1]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


# test = [item for item in FlatIterator(list_of_lists_1)]
# print(test)

def flat_generator(any_list):
    for inner_list in any_list:
        for item in inner_list:
            yield item


def test_2():
    list_of_lists_2 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


# test2 = [item for item in flat_generator(list_of_lists_1)]
# print(test2)

def main():
    test_1()
    test_2()


if __name__ == '__main__':
    main()
