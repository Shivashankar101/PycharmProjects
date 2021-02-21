from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):

    # @task
    @task(1) # to give weightage
    def launch_url(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # the wait between each task of simulated user -- > in the range of  5 to 15 seconds
    min_wait = 5000
    max_wait = 15000
    host = "http://demo.guru99.com/test/newtours/"