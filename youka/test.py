from locust import TaskSet, task, HttpLocust
import queue, requests
import time, random


class UserBehavior(TaskSet):

    @task
    def test_register(self):
        # url = "http://10.100.1.190:8888/users/addorder"
        url = "http://10.100.11.91:8888/users/addorder"
        self.client.get(url=url)


class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
