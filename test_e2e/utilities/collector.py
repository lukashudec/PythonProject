import pytest

''' will collect tests from unit test
this can be used to run them with locust - thus doing performance unit test'''
class TestCollector:

    def __init__(self, dir=""):
        self.collected = []
        if dir != "":
            pytest.main([dir, '--collect-only'],
                        plugins=[self])

    def collect(self, dir):
        pytest.main([dir, '--collect-only'],
                    plugins=[self])

    def pytest_collection_modifyitems(self, items):
        for item in items:
            self.collected.append(item.nodeid)

    def get_tests(self, filter) -> list:
        filtered = []
        for test in self.collected:
            if filter in test:
                filtered.append(test)
        return filtered

'''
test_collector = TestCollector('C:/Users/lenovo/PycharmProjects/calendar/test_unit/test_calendar_class.py')

for test in test_collector.collected:
    print(str(test))

print("========================")

for test in test_collector.get_tests('test_calendar_creation'):
    print(str(test))
'''