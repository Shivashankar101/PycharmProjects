from locust import HttpUser, TaskSet


def task1():
    print("i am logged in")

def task2():
    print("I am Logged out")

# class UserBehavior(TaskSet):
#     # tasks = [task1, task2]
#     tasks = {task1: 3, task2: 1}  ### giving weightage to tasks

class WebsiteUser(HttpUser):
    tasks = {task1: 3, task2: 1}
