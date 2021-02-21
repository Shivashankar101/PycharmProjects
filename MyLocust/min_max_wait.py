from locust import HttpUser, TaskSet, task



class UserBehavior(TaskSet):

    # @task
    @task(1) # to give weightage
    def task1(self):
        print("i am logged in")

    # @task
    @task(3) # to give weightage
    def task2(self):
        print("I am Logged out")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # the wait between each task of simulated user -- > in the range of  5 to 15 seconds
    min_wait = 5000
    max_wait = 15000