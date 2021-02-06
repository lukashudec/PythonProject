from Calendar import Calendar

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
bound1 = [['9:00', '20:00']]
calendar2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound2 = [['10:00', '18:30']]
output = [['15:00', '16:00'], ['18:00', '18:30']]
calendar1_string = '9:00-10:30,12:00-13:00,16:00-18:00'
bound1_string = '9:00-20:00'


def test_calendar_creation():
    cal1 = Calendar(calendar1, bound1)
    cal2 = Calendar.from_string(calendar1_string, bound1_string)
    assert cal1.is_equal(cal2), 'calendars are not equal'


def test_calendar_merge():
    cal1 = Calendar(calendar1, bound1)
    cal2 = Calendar(calendar2, bound2)
    merged_cal1 = cal1.merge_with_calendar(cal2)
    merged_cal2 = Calendar.merge_calendars(cal1, cal2)
    assert merged_cal1.is_equal(merged_cal2), 'calendars are not equal'


def test_calendar_output_pretty():
    raw_output = [[900, 960], [1080, 1110]]
    cal1 = Calendar(calendar1, bound1)
    cal2 = Calendar(calendar2, bound2)
    output_calendar = Calendar.merge_calendars(cal1, cal2)
    assert output == output_calendar.pretty_free_time
    assert raw_output == output_calendar.free_time
