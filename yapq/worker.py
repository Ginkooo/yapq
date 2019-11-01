import threading


class Worker:

    def __init__(self, task_queue):
        self.task_queue = task_queue
        self.thread = threading.Thread(target=self.execution_loop)
        self.thread.start()

    def execution_loop(self):
        while True:
            job = self.task_queue.get()
            if job is None:
                self.task_queue.put(None)
                break
            job()
