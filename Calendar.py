class Calendar:
    raw_calendar = []
    bounds = []
    calendar = []
    free_time = []
    pretty_cal = []
    pretty_free = []

    def __init__(self, raw_calendar: list, bounds: list):
        self.raw_calendar = raw_calendar
        self.bounds = bounds

        self.calendar = self.__format_input()
        self.free_time = self.__get_free_time()

        self.pretty_cal = self.__format_output(self.calendar)
        self.pretty_free_time = self.__format_output(self.free_time)

    @classmethod
    def merge_calendars(cls, cal1, cal2):
        cale = sorted(cal1.raw_calendar + cal2.raw_calendar)
        bou = [[max(cal1.bounds[0][0], cal2.bounds[0][0]), min(cal1.bounds[0][1], cal2.bounds[0][1])]]
        return cls(cale, bou)

    def merge_with_calendar(self, cal2):
        return self.merge_calendars(self,cal2)

    @classmethod
    # testability improvement
    def from_string(cls, calendar_string, bound_string):
        return cls(cls.extract_time(calendar_string), cls.extract_time(bound_string))

    @staticmethod
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

    @staticmethod
    def __format_time(time):
        time = str(time)
        if len(str(time)) == 1:
            time = '0' + time
        return time

    @staticmethod
    def __f_hour(hour):
        return Calendar.__format_time((hour // 60))

    @staticmethod
    def __f_min(minute):
        return Calendar.__format_time((minute % 60))

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

    def is_equal(self, calendar2):
        if self.raw_calendar == calendar2.raw_calendar and self.bounds == calendar2.bounds:
            return True
        return False
