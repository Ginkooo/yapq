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

    def put(self, job):
        self.task_list.append(serializer.encode(job))

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
