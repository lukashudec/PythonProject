from locust import User, task, between, events


class FrequentUser(User):
    weight = 5
    ftn = 0
    rtn = 0

    @task(2)
    def frequent_task(self):
        self.ftn += 1
        print("fu ft "+str(self.ftn))
        events.request_success.fire(request_type="step",
                                    name="fu ft",
                                    response_time=1000,
                                    response_length=0)
    wait_time = between(1, 1)

    @task(1)
    def rare_task(self):
        self.rtn += 1
        print("fu rt "+str(self.rtn))
        events.request_success.fire("step", "fu rt", 1000, 0)
    wait_time = between(1, 1)


class RareUser(User):
    weight = 1

    @task
    def task1(self):
        print("ru rt")
    wait_time = between(1, 1)