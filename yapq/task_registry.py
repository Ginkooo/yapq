import multiprocessing
import pickle
import random
import uuid

from yapq import result
from yapq import serializer

class TaskRegistry:

    def __init__(self, task_registry_dict, commands_dict, lock):
        self.task_registry = task_registry_dict
        self.commands = commands_dict
        self.lock = lock

    def put(self, job):
        self.task_registry[str(uuid.uuid4())] = serializer.encode(job)

    def get(self, key=None):
        with self.lock:
            if key is None:
                key = random.choice(self.task_registry.keys())

            if not self.task_registry.keys():
                return None

            if not self.task_registry.get(key):
                return None

            ret = serializer.decode(self.task_registry[key])
            return ret

    def send_terminate_task(self):
        self.commands['terminate'] = serializer.encode(True)


    def put_result(self, value, uuid):
        result_ = result.Result()
        result_.value = value
        self.task_registry[uuid] = serializer.encode(result_)
