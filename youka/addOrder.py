from locust import TaskSet, task, HttpLocust
import queue, requests
import time, random


class UserBehavior(TaskSet):

    @task
    def test_register(self):
        # url = "http://10.100.1.190:8888/users/addorder"
        url = "http://10.100.11.91:8887/users/addorder"
        try:
            user_id = self.locust.user_id_queue.get()
            order_no = self.locust.order_no_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        print(user_id)
        self.client.post(url=url, data={"user_id": user_id, "order_no": order_no})


class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    user_id_queue = queue.Queue()
    order_no_queue = queue.Queue()
    user_id = 2369615076710976
    order_no = 290908164200625888
    for i in range(10000000):
        user_id += 1
        order_no += 1
        user_id_queue.put_nowait(user_id)
        order_no_queue.put_nowait(order_no)
    min_wait = 0
    max_wait = 0
