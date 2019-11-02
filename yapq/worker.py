import multiprocessing
import time

from yapq import result


class Worker:

    def __init__(self, task_registry):
        self.task_registry = task_registry
        self.thread = multiprocessing.Process(target=self.execution_loop)
        self.thread.start()

    def execution_loop(self):
        while True:
            time.sleep(1)
            if self.task_registry.commands.get('terminate'):
                break
            job = self.task_registry.get()
            if not job:
                continue
            if isinstance(job, result.Result):
                continue
            value = job()
            self.task_registry.put_result(value, job.uuid)

    def join(self):
        self.thread.join()
