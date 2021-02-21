from locust import HttpUser, TaskSet, task




class UserBehavior(TaskSet):

    @task
    # @task(1) # to give weightage
    def task1(self):
        print("i am logged in")

    @task
    # @task(2) # to give weightage
    def task2(self):
        print("I am Logged out")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
