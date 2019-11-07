import multiprocessing
import uuid

from yapq import worker
from yapq import job
from yapq import result
from yapq import task_registry

class Yapq:

    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.task_list = self.manager.list()
        self.lock = self.manager.Lock()
        self.commands_dict = self.manager.dict()
        self.result_dict = self.manager.dict()
        self.task_registry = task_registry.TaskRegistry(
            self.task_list,
            self.commands_dict,
            self.result_dict,
            self.lock,
        )

    def start(self, size=multiprocessing.cpu_count()):
        self.workers = [worker.Worker(
            self.task_registry,
            ) for _ in range(size)]

    def stop(self):
        self.task_registry.send_terminate_task()
        for w in self.workers:
            w.join()
        self.manager.shutdown()
        self.manager.join()

    def get_tasks_info(self):
        return self.task_registry.get_tasks_info()

    def swap(self, left_uuid, right_uuid):
        return self.task_registry.swap_tasks(left_uuid, right_uuid)

    def enqueue(self, func, *args, **kwargs):
        job_ = job.Job(func, *args, **kwargs)
        self.task_registry.put(job_)
        return result.Result(job_.uuid, self.result_dict)
