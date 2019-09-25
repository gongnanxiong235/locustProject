from locust import TaskSet, task, HttpLocust
import queue, requests
import time, random


class UserBehavior(TaskSet):

    @task
    def test_register(self):
        url = "http://10.100.11.91/users/addorder"
        print(self.locust.user_id)
        self.client.post(url=url, data={"user_id": self.locust.user_id, "order_no": self.locust.order_no})
        self.locust.user_id+=1
        self.locust.order_no+=1

class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    user_id = 3569615076710976
    order_no = 350908164200625888
    min_wait = 0
    max_wait = 0
