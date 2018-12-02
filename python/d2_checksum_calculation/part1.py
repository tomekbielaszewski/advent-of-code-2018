import unittest
from functools import reduce


class Solution:
    @staticmethod
    def calculate_checksum(ids):
        counted_letters_in_ids = [Solution.count_letters(_id) for _id in ids]
        doubled_char_occurrences_in_ids = Solution.filter_occurrences_in_amount_of(2, counted_letters_in_ids)
        tripled_char_occurrences_in_ids = Solution.filter_occurrences_in_amount_of(3, counted_letters_in_ids)
        amount_of_doubled_char_occurrences = reduce(Solution.count_if_any, doubled_char_occurrences_in_ids, 0)
        amount_of_tripled_char_occurrences = reduce(Solution.count_if_any, tripled_char_occurrences_in_ids, 0)
        return amount_of_doubled_char_occurrences * amount_of_tripled_char_occurrences

    @staticmethod
    def count_if_any(acc, i):
        if i > 0:
            acc += 1
        return acc

    @staticmethod
    def filter_occurrences_in_amount_of(amount, counted_letters_in_ids):
        return [Solution.count_occurrence_amounts(amount, counted_letters) for counted_letters in
                counted_letters_in_ids]

    @staticmethod
    def count_letters(_id):
        counted_letters = {}
        for char in _id:
            if char in counted_letters.keys():
                counted_letters[char] += 1
            else:
                counted_letters[char] = 1
        return counted_letters

    @staticmethod
    def count_occurrence_amounts(occurrences, counted_letters):
        return len({k: v for (k, v) in counted_letters.items() if v == occurrences})


class TestSolution(unittest.TestCase):

    def test_example1(self):
        ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        checksum = Solution.calculate_checksum(ids)

        self.assertEqual(12, checksum)

    def test_finalSolution(self):
        with open("input.txt") as f:
            changes = f.readlines()
            total = Solution.calculate_checksum(changes)

            print(total)
