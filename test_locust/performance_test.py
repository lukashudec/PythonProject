import random
import time
from locust import User, task, between
from test_e2e.utilities.step import measured_step


class FrequentUser(User):
    weight = 5
    wait_time = between(1, 1)

    @task(1)
    def frequent_task(self):
        self.frequent_task()

    @task(1)
    def rare_task(self):
        self.sleepy_task()

    @measured_step("task with sleep, dynamic time")
    def sleepy_task(self):
        sleep = random.random()
        print("step 1 "+str(sleep))
        time.sleep(sleep)

    @measured_step("frequent_task, constant time")
    def frequent_task(self):
        print("step 2")
