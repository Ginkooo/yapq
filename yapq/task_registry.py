import multiprocessing
import pickle
import random
import uuid

from yapq import result
from yapq import serializer

class TaskRegistry:

    def __init__(self, task_list, commands_dict, result_dict, lock):
        self.task_list = task_list
        self.commands = commands_dict
        self.result_dict = result_dict
        self.lock = lock
        self.internals = task_list, commands_dict, result_dict, lock

    def put(self, job):
        self.task_list.append(serializer.encode(job))

    def get_tasks_info(self):
        return [pickle.loads(job).as_dict() for job in self.task_list]

    def find_task_index(self, uuid):
        for i, job in enumerate(self.task_list):
            job = pickle.loads(job)
            if job.uuid == uuid:
                return i
        return None

    def swap_tasks(self, left_uuid, right_uuid):
        with self.lock:
            left_idx = self.find_task_index(left_uuid)
            right_idx = self.find_task_index(right_uuid)

            print(self.get_tasks_info())
            (
                self.task_list[left_idx],
                self.task_list[right_idx],
            ) = (
                self.task_list[right_idx],
                self.task_list[left_idx],
            )
            print()
            print(self.get_tasks_info())

    def get(self, key=None):
        with self.lock:
            try:
                return serializer.decode(self.task_list.pop())
            except IndexError:
                return None

    def send_terminate_task(self):
        self.commands['terminate'] = serializer.encode(True)


    def put_result(self, value, uuid):
        result_ = result.Result()
        result_.value = value
        self.result_dict[uuid] = serializer.encode(result_)
