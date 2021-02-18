from locust import HttpUser, TaskSet, task


def login():
    print("i am logged in")

def logout():
    print("I am Logged out")


class UserBehavior(TaskSet):
    task = [logout(), login()]


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]

