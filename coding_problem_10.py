import time
from collections import deque
class Task:
    def __init__(self,cb,when):
        self.cb = cb
        self.when = when
    def run(self,time):
        if time >= self.when:
            self.cb()
            return True
        return False
class Manager:
    def __init__(self):
        self.tasks = deque()
    def add(self,cb,delay):
        now = int(round(time.time() * 1000.0))
        when = now + delay
        task = Task(cb,when)
        self.tasks.append(task)
    def run(self):
        while len(self.tasks) > 0:
            now = int(round(time.time() * 1000.0))
            task = self.tasks.popleft()
            if not task.run(now):
                self.tasks.append(task)
                

def task_to_run():
    print("Hello World")
m = Manager()
m.add(task_to_run,2000)
m.run()

