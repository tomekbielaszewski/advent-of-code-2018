import unittest


def calculate_checksum(ids):
    pass


class TestSolution(unittest.TestCase):

    def test_example1(self):
        ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        checksum = calculate_checksum(ids)

        self.assertEqual(12, checksum)

    def test_finalSolution(self):
        with open("input.txt") as f:
            changes = f.readlines()
            total = calculate_checksum(changes)

            print(total)
