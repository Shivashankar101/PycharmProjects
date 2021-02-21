from locust import HttpUser, TaskSet, task

'''
https://twitter.com/sessions
redirect_after_login: /
remember_me: 1
authenticity_token: df672670737111ebbbc2afa620e45ccf
wfa: 1
ui_metrics: {"rf":{"a169cd3abe064af47694f0f082baea41e8bd955962137f2a00ab95fb0e786f1d":110,"c381f71304e464d888439f5f4f8d2b79164b2533f14db91e91992c852e56fa9e":-14,"a981bcaf30545ecab94d13a89d0e7cc72c37940b5ffb7f3c78899b823445dbef":-97,"a49483c132848442955c13ca5bdcaf25cf760d1fc85eb7624e02befa29c3bca4":-103},"s":"bCIJRZCa6EaZdSXUdbw-QG-H_chY26W2tTPXPKsPWLs1-1tUIh0vsw5V_1MclpoH0z4RVvAwl4uZfZ48GeqNgYM2t9JSkf8FStVXVHiCMvQ41NeUUaM4-Ss1xc1m9qFwg52zNZX6Q2BifTtEL9mZO4Gx-u1z6prS7nkUohtmE4A2le-K_UzZ1BnY63SNA6IFarwZg5f0E88_3nj5FcAj-O2v1IrROJ81_GxVLyfk0SDvgHjlPPAczXld1gEjD-qm7bhNa1u8Uctm-v7ZoQ6TsFAA97hAAo1GEbgKjcv_BuGshplbNHQm4BpJ8i-PL2hhg035jiq09yHBesx8n2ffKAAAAXe_RyiD"}
session[username_or_email]: Shivash11232321
session[password]: pgpgpgagj
'''
UserName = [
    ("qamile1@gmail.com", "qamile1"),
    ("Shivashankarawati@gmail.com", "Pgpgpgagj100."),
    ("qamile2@gmail.com", "qamile2"),
    ("qamile3@gmail.com", "qamile3"),
    ("qamile4@gmail.com", "qamile4"),
    ("qamile5@gmail.com", "qamile5")
 ]


class UserBehavior(TaskSet):

    def on_start(self):
        self.username = "Not_exist"
        self.password = "Not_exist"
        if len(UserName) > 0:
            self.username, self.password = UserName.pop()

    @task
    # @task(1) # to give weightage
    def login_twitter(self):
        print(self.username)
        resp = self.client.post("/login/sessions/",
                         {"redirect_after_login": '/',
                          "remember_me": 1,
                          "authenticity_token": 'df672670737111ebbbc2afa620e45ccf',
                          "wfa": 1,
                          "ui_metrics": {"rf": {"a169cd3abe064af47694f0f082baea41e8bd955962137f2a00ab95fb0e786f1d": 110, "c381f71304e464d888439f5f4f8d2b79164b2533f14db91e91992c852e56fa9e": -14, "a981bcaf30545ecab94d13a89d0e7cc72c37940b5ffb7f3c78899b823445dbef": -97, "a49483c132848442955c13ca5bdcaf25cf760d1fc85eb7624e02befa29c3bca4": -103}, "s":"bCIJRZCa6EaZdSXUdbw-QG-H_chY26W2tTPXPKsPWLs1-1tUIh0vsw5V_1MclpoH0z4RVvAwl4uZfZ48GeqNgYM2t9JSkf8FStVXVHiCMvQ41NeUUaM4-Ss1xc1m9qFwg52zNZX6Q2BifTtEL9mZO4Gx-u1z6prS7nkUohtmE4A2le-K_UzZ1BnY63SNA6IFarwZg5f0E88_3nj5FcAj-O2v1IrROJ81_GxVLyfk0SDvgHjlPPAczXld1gEjD-qm7bhNa1u8Uctm-v7ZoQ6TsFAA97hAAo1GEbgKjcv_BuGshplbNHQm4BpJ8i-PL2hhg035jiq09yHBesx8n2ffKAAAAXe_RyiD"},
                          "session[username_or_email]": self.username,
                          "session[password]": self.password})
        print(resp.text)
        # print(resp.status_code)
        # print(resp.headers)
        # print(resp.request.headers)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # the wait between each task of simulated user -- > in the range of  5 to 15 seconds
    min_wait = 5000
    max_wait = 15000
    host = "https://twitter.com/login/sessions/"