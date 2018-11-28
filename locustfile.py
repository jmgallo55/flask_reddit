from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login/", {"csrf_token":"IjJlOTI5NWQ5NDU1NWYxM2FkNGUxZTk5NDhmYmU1MTgxZDBkOTU2ZWMi.W_t7pA.Lj6cNczwvTK_9KvwGQX6qbSNTfw", "next":"/", "email":"jmgallo55@gmail.com", "password":"cloud176"})

def logout(l):
    l.client.get("/logout")

def post(l):
    l.client.post("/apis/comments/submit/", {"parent_id":"", "thread_id":"3", "comment_text":"testcommandline"})

class UserBehavior(TaskSet):
    tasks = {post: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
