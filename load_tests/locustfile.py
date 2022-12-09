from locust import HttpUser, task, between

class Pages(HttpUser):
    wait_time = between(2, 3)

    @task(2)
    def main_page(self):
        self.client.get("/")

    @task
    def review_page(self):
        self.client.get("/cases")


# export PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:$PATH"