import unittest
import calendar_merge

c1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
c2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
b2 = ['10:00', '18:30']
output = [['15:00', '16:00'], ['18:00', '18:30']]


class TestSolver(unittest.TestCase):

    def test_get_free_block_general(self):
        self.assertEqual(output, calendar_merge.get_free_block(c1, b1, c2, b2), 'texticek')

    def test_get_free_block_output_format(self):
        self.assertEqual(calendar_merge.get_free_block(c1, b1, c2, b2), output, 'texticek')

    def test_get_free_block_30min_window(self):
        self.assertEqual(calendar_merge.get_free_block(c1, b1, c2, b2), output, 'texticek')

    def test_get_free_time(self):
        output = [[900, 960], [1080, 1110]]
        self.assertEqual(calendar_merge.get_free_time(sorted(calendar_merge.format_input(c1, b1) + calendar_merge.format_input(c2, b2))), output, 'texticek')


if __name__ == '__main__':
    unittest.main()
