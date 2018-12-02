import unittest

ops = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
}


def calcFrequency(changes):
    total = 0
    for change in changes:
        total = ops[change[0]](total, int(change[1:]))
    return total


class TestSolution(unittest.TestCase):

    def test_example1(self):
        changes = ["+1", "-2", "+3", "+1"]
        total = calcFrequency(changes)

        self.assertEqual(3, total)

    def test_example2(self):
        changes = ["+1", "+1", "+1"]
        total = calcFrequency(changes)

        self.assertEqual(3, total)

    def test_example3(self):
        changes = ["+1", "+1", "-2"]
        total = calcFrequency(changes)

        self.assertEqual(0, total)

    def test_example4(self):
        changes = ["-1", "-2", "-3"]
        total = calcFrequency(changes)

        self.assertEqual(-6, total)

    def test_finalSolution(self):
        with open("input.txt") as f:
            changes = f.readlines()
            total = calcFrequency(changes)

            print(total)
