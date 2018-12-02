import unittest

ops = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
}


def find_duplicated_frequency(changes):
    total = 0
    already_seen = set()
    length = len(changes)
    counter = 0

    while total not in already_seen:
        already_seen.add(total)
        change = changes[counter]
        total = ops[change[0]](total, int(change[1:]))
        counter += 1
        if counter >= length:
            counter = 0
    return total


class TestSolution(unittest.TestCase):

    def test_example1(self):
        changes = ["+1", "-2", "+3", "+1"]
        total = find_duplicated_frequency(changes)

        self.assertEqual(2, total)

    def test_example2(self):
        changes = ["+1", "-1"]
        total = find_duplicated_frequency(changes)

        self.assertEqual(0, total)

    def test_example3(self):
        changes = ["+3", "+3", "+4", "-2", "-4"]
        total = find_duplicated_frequency(changes)

        self.assertEqual(10, total)

    def test_example4(self):
        changes = ["-6", "+3", "+8", "+5", "-6"]
        total = find_duplicated_frequency(changes)

        self.assertEqual(5, total)

    def test_example5(self):
        changes = ["+7", "+7", "-2", "-7", "-4"]
        total = find_duplicated_frequency(changes)

        self.assertEqual(14, total)

    def test_finalSolution(self):
        with open("input.txt") as f:
            changes = f.readlines()
            total = find_duplicated_frequency(changes)

            print(total)
