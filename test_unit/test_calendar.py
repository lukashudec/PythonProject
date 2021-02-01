import unittest
from calendar_merge import format_input, get_free_time, get_free_block

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
bound1 = [['9:00', '20:00']]
calendar2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound2 = [['10:00', '18:30']]
output = [['15:00', '16:00'], ['18:00', '18:30']]


class TestSolver(unittest.TestCase):

    def test_get_free_block_general(self):
        self.assertEqual(output,
                         get_free_block(calendar1, bound1, calendar2, bound2),
                         'different values expected')

    def test_get_free_time(self):
        output = [[900, 960], [1080, 1110]]
        self.assertEqual(get_free_time(sorted(format_input(calendar1, bound1) + format_input(calendar2, bound2))),
                         output,
                         'different values expected')


if __name__ == '__main__':
    unittest.main()
