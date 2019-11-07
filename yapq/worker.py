import multiprocessing
import time

from yapq import result
from yapq import task_registry


class Worker:

    def __init__(self, task_registry_dict, commands_dict, result_dict, lock):
        self.thread = multiprocessing.Process(
            target=Worker.execution_loop,
            args=(task_registry_dict, commands_dict, result_dict, lock)
        )
        self.thread.start()

    @staticmethod
    def execution_loop(task_registry_dict, commands_dict, result_dict, lock):
        task_registry_ = task_registry.TaskRegistry(
            task_registry_dict,
            commands_dict,
            result_dict,
            lock,
        )

        while True:
            if task_registry_.commands.get('terminate'):
                break
            job = task_registry_.get()
            if not job:
                continue
            if isinstance(job, result.Result):
                continue
            value = job()
            task_registry_.put_result(value, job.uuid)

    def join(self):
        self.thread.join()
