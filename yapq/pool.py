import multiprocessing
import uuid

from yapq import worker
from yapq import job
from yapq import result
from yapq import task_registry

class Pool:

    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.task_registry_dict = self.manager.dict()
        self.lock = self.manager.Lock()
        self.commands_dict = self.manager.dict()
        self.task_registry = task_registry.TaskRegistry(
            self.task_registry_dict,
            self.commands_dict,
            self.lock,
        )

    def start(self, size=multiprocessing.cpu_count()):
        self.workers = [worker.Worker(
            self.task_registry_dict,
            self.commands_dict,
            self.lock,
            ) for _ in range(size)]

    def stop(self):
        self.task_registry.send_terminate_task()
        for w in self.workers:
            w.join()
        self.manager.shutdown()
        self.manager.join()

    def enqueue(self, func, *args, **kwargs):
        job_ = job.Job(func, *args, **kwargs)
        self.task_registry.put(job_)
        return result.Result(job_.uuid, self.task_registry)
