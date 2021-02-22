import random
import time
from locust import User, task, between
from test_e2e.utilities.step import measured_step


class FrequentUser(User):
    weight = 5
    wait_time = between(1, 1)

    @task(2)
    def frequent_task(self):
        self.task_step2()

    @task(1)
    def rare_task(self):
        self.task_step()

    @measured_step("step 1")
    def task_step(self):
        sleep = random.random()
        print("step 1 "+str(sleep))
        time.sleep(random.random())

    @measured_step("step 2")
    def task_step2(self):
        print("step 2")
