import threading


class Worker:

    def __init__(self, task_queue):
        self.task_queue = task_queue
        thread = threading.Thread(target=self.execution_loop)
        thread.start()

    def execution_loop(self):
        while True:
            job = self.task_queue.get()
            job()
