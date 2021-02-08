from Calendar import CalendarClass

calendar1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
bound1 = [['09:00', '20:00']]
calendar2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound2 = [['10:00', '18:30']]
output = [['15:00', '16:00'], ['18:00', '18:30']]
calendar1_string = '09:00-10:30,12:00-13:00,16:00-18:00'
bound1_string = '09:00-20:00'


def test_calendar_creation():
    cal1 = CalendarClass(calendar1, bound1)
    cal2 = CalendarClass.from_string(calendar1_string, bound1_string)
    assert cal1 == cal2, 'calendars are not equal'


def test_calendar_merge():
    calendar1 = [['12:00', '13:00'], ['16:00', '18:00']]
    bound1 = [['09:00', '20:00']]
    calendar2 = [['10:00', '11:45'], ['12:30', '14:30']]
    bound2 = [['10:00', '18:30']]
    cal1 = CalendarClass(calendar1, bound1)
    cal2 = CalendarClass(calendar2, bound2)
    output_calendar = cal1.merge_with_calendar(cal2)
    assert output_calendar.raw_calendar ==\
           [['10:00', '11:45'], ['12:00', '13:00'], ['12:30', '14:30'], ['16:00', '18:00']]
    assert output_calendar.bounds ==\
           [['10:00', '18:30']]


def test_get_possible_events_with():
    cal1 = CalendarClass(calendar1, bound1)
    cal2 = CalendarClass(calendar2, bound2)
    free_time1 = cal1.merge_with_calendar(cal2).get_free_time_pretty()
    free_time3 = cal1.get_possible_events_with(cal2)
    assert free_time1 == free_time3, 'calendars are not equal'


def test_get_free_time__with_param():
    calendar1 = [['09:00', '10:30'], ['11:00', '13:00'], ['16:00', '18:00']]
    bound1 = [['09:00', '20:00']]
    cal1 = CalendarClass(calendar1, bound1)
    assert cal1.get_free_time_pretty(181) == []
    assert cal1.get_free_time_pretty(121) == [['13:00', '16:00']]
    assert cal1.get_free_time_pretty(60) == [['13:00', '16:00'], ['18:00', '20:00']]
    assert cal1.get_free_time_pretty(30) == [['10:30', '11:00'], ['13:00', '16:00'], ['18:00', '20:00']]
    assert cal1.get_free_time_pretty() == [['10:30', '11:00'], ['13:00', '16:00'], ['18:00', '20:00']]
