class CalendarClass:

    def __init__(self, raw_calendar: list, bounds: list):
        self.raw_calendar = raw_calendar
        self.bounds = bounds
        self.calendar = self.__format_input()

    def __eq__(self, other):
        if isinstance(other, CalendarClass):
            return self.raw_calendar == other.raw_calendar and self.bounds == other.bounds
        return False

    @classmethod
    # testability improvement
    def from_string(cls, calendar_string, bound_string):
        return cls(cls.extract_time(calendar_string), cls.extract_time(bound_string), )

    def merge_with_calendar(self, cal2):
        cale = sorted(self.raw_calendar + cal2.raw_calendar)
        bou = [[max(self.bounds[0][0], cal2.bounds[0][0]), min(self.bounds[0][1], cal2.bounds[0][1])]]
        return CalendarClass(cale, bou)

    def __format_input(self) -> list:
        result = []
        inp_list = [['00:00', self.bounds[0][0]]] + self.raw_calendar + [[self.bounds[0][1], '24:00']]
        for i in inp_list:
            h, m = i[0].split(':')
            h1, m1 = i[1].split(':')
            result.append([int(h) * 60 + int(m), int(h1) * 60 + int(m1)])
        return sorted(result)

    def get_free_time(self, min_time_frame=30) -> list:
        result = []
        for i in range(0, len(self.calendar) - 1, 1):
            if self.calendar[i + 1][0] - self.calendar[i][1] >= min_time_frame:
                result.append([self.calendar[i][1], self.calendar[i + 1][0]])
        return result

    def get_free_time_pretty(self, min_time_frame=30):
        return self.__format_output(self.get_free_time(min_time_frame))

    def get_possible_events_with(self, calendar2, min_time_frame=30):
        return self.merge_with_calendar(calendar2).get_free_time_pretty(min_time_frame)

    def __format_output(self, calendar_type) -> list:
        result = []
        for i in calendar_type:
            result.append(
                [self.__f_time(i[0] // 60) + ':' + self.__f_time(i[0] % 60),
                 self.__f_time(i[1] // 60) + ':' + self.__f_time(i[1] % 60)])
        return result

    @staticmethod
    def __f_time(time):
        time = str(time)
        if len(str(time)) == 1:
            time = '0' + time
        return time

    @staticmethod
    def extract_time(input_string):
        result = []
        for time_frame in input_string.split(','):
            result.append(time_frame.split('-'))
        return result