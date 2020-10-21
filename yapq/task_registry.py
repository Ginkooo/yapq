import multiprocessing
import pickle
import random
import uuid

from yapq import job
from yapq import result

class TaskRegistry:

    def __init__(self, task_list, commands_dict, result_dict, lock):
        self.task_list = task_list
        self.commands = commands_dict
        self.result_dict = result_dict
        self.lock = lock
        self.internals = task_list, commands_dict, result_dict, lock

    def put(self, job):
        self.task_list.append(job.as_pickle())

    def get_tasks_info(self):
        return [job.Job.from_pickle(job_).as_dict() for job_ in self.task_list]

    def find_task_index(self, uuid):
        for i, job_ in enumerate(self.task_list):
            job_ = job.Job.from_pickle(job_)
            if job_.uuid == uuid:
                return i
        return None

    def swap_tasks(self, left_uuid, right_uuid):
        with self.lock:
            left_idx = self.find_task_index(left_uuid)
            right_idx = self.find_task_index(right_uuid)

            (
                self.task_list[left_idx],
                self.task_list[right_idx],
            ) = (
                self.task_list[right_idx],
                self.task_list[left_idx],
            )

    def get(self, key=None):
        with self.lock:
            try:
                return job.Job.from_pickle(self.task_list.pop())
            except IndexError:
                return None

    def send_terminate_task(self):
        self.commands['terminate'] = True


    def put_result(self, value, uuid):
        result_ = result.Result()
        result_.value = value
        self.result_dict[uuid] = pickle.dumps(result_)
