import queue

class TaskQueue:
    jobs = queue.Queue()

    def put(self, job):
        return self.jobs.put(job)

    def get(self):
        return self.jobs.get()
