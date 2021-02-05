from calendar import Calendar


class Calendar:

    def __init__(self, raw_calendar: list, bounds: list):
        self.raw_calendar = raw_calendar
        self.bounds = bounds

        self.calendar = self.__format_input()
        self.free_time = self.__get_free_time()

        self.pretty_cal = self.__format_output(self.calendar)
        self.pretty_free = self.__format_output(self.free_time)

    @classmethod
    def merge_calendars(cls, cal1: Calendar, cal2: Calendar):
        cale = sorted(cal1.raw_calendar + cal2.raw_calendar)
        bou = [[max(cal1.bounds[0][0], cal2.bounds[0][0]), min(cal1.bounds[0][1], cal2.bounds[0][1])]]
        return cls(cale, bou)

    @classmethod
    # testability improvement
    def from_string(cls, calendar_string, bound_string):
        return cls(cls.extract_time(calendar_string), cls.extract_time(bound_string))

    def extract_time(input_string):
        result = []
        for time_frame in input_string.split(','):
            result.append(time_frame.split('-'))
        return result

    def __format_input(self) -> list:
        result = []
        inp_list = [['00:00', self.bounds[0][0]]] + self.raw_calendar + [[self.bounds[0][1], '24:00']]
        for i in inp_list:
            h, m = i[0].split(':')
            h1, m1 = i[1].split(':')
            result.append([int(h) * 60 + int(m), int(h1) * 60 + int(m1)])
        return sorted(result)

    def __get_free_time(self) -> list:
        result = []
        for i in range(0, len(self.calendar) - 1, 1):
            if self.calendar[i + 1][0] - self.calendar[i][1] >= 30:
                result.append([self.calendar[i][1], self.calendar[i + 1][0]])
        return result

    def __format_time(self, time):
        time = str(time)
        if len(str(time)) == 1: time = '0' + time
        return time

    def __f_hour(self, hour):
        return self.__format_time((hour // 60))

    def __f_min(self, minute):
        return self.__format_time((minute % 60))

    def __format_output(self, calendar_type) -> list:
        result = []
        for i in calendar_type:
            result.append(
                [self.__f_hour(i[0]) + ':' + self.__f_min(i[0]), self.__f_hour(i[1]) + ':' + self.__f_min(i[1])])
        return result

    def get_free_time(self) -> list:
        result = []
        for i in range(0, len(self.calendar) - 1, 1):
            if self.calendar[i + 1][0] - self.calendar[i][1] >= 30:
                result.append([self.calendar[i][1], self.calendar[i + 1][0]])
        return self.__format_output(result)


calendar1 = [['09:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
bound1 = [['09:00', '20:00']]
calendar2 = [['10:00', '11:45'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
bound2 = [['10:00', '18:30']]
cal = Calendar(calendar1, bound1)
cal2 = Calendar(calendar2, bound2)

cal3 = Calendar.merge_calendars(cal, cal2)
print(cal3.get_free_time())

calendar1 = '9:00-10:30,12:00-13:00,16:00-18:00'
bound1 = '9:00-20:00'
cal4 = Calendar.from_string(calendar1, bound1)
print(cal4.raw_calendar)
print(cal4.bounds)
