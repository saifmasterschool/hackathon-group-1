import schedule
import time


class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, time_str, task_func, channel, phone_number):
        task_id = f"{phone_number}_{channel}"
        task = schedule.every().day.at(time_str).do(task_func)

        self.tasks[task_id] = task
        print(f"Task {task_id} scheduled for {time_str}")

        return task_id

    def remove_task(self, task_id):
        if task_id in self.tasks:
            schedule.cancel_job(self.tasks[task_id])
            del self.tasks[task_id]
            print(f"Task {task_id} removed")
        else:
            print(f"Task {task_id} not found")

    @staticmethod
    def run_pending():
        while True:
            schedule.run_pending()
            time.sleep(1)
