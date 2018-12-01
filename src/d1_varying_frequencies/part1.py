import unittest

ops = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
}


class Solution:
    def calcFrequency(self, changes):
        total = 0
        for change in changes:
            total = ops[change[0]](total, int(change[1:]))
        return total


class TestSolution(unittest.TestCase):

    def test_example1(self):
        changes = ["+1", "-2", "+3", "+1"]
        total = Solution().calcFrequency(changes)

        self.assertEqual(3, total)

    def test_example2(self):
        changes = ["+1", "+1", "+1"]
        total = Solution().calcFrequency(changes)

        self.assertEqual(3, total)

    def test_example3(self):
        changes = ["+1", "+1", "-2"]
        total = Solution().calcFrequency(changes)

        self.assertEqual(0, total)

    def test_example4(self):
        changes = ["-1", "-2", "-3"]
        total = Solution().calcFrequency(changes)

        self.assertEqual(-6, total)

    def test_finalSolution(self):
        with open("part1.txt") as f:
            changes = f.readlines()
            total = Solution().calcFrequency(changes)

            print(total)
