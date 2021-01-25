import calendar_merge as c

c1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
b1 = ['9:00', '20:00']
c2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
b2 = ['10:00', '18:30']
output = [['15:00', '16:00'], ['18:00', '18:30']]


def test_get_free_block_general():
    assert output == c.get_free_block(c1, b1, c2, b2),\
        "actual different from expected"


def test_get_free_time():
    output = [[900, 960], [1080, 1110]]
    assert c.get_free_time(sorted(c.format_input(c1, b1)+c.format_input(c2, b2))) == output,\
        "actual different from expected"
