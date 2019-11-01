from yapq import worker
from yapq import job
from yapq import task_queue

class Pool:

    def __init__(self, size=4):
        self.size = size
        self.task_queue = task_queue.TaskQueue()

    def start(self):
        self.workers = [worker.Worker(self.task_queue) for _ in range(self.size)]

    def stop(self):
        self.task_queue.put(None)

    def enqueue(self, func, *args, **kwargs):
        job_ = job.Job(func, *args, **kwargs)
        self.task_queue.put(job_)
        return job_.result

