import multiprocessing
import pickle
import random
import uuid

from yapq import result
from yapq import serializer

class TaskRegistry:

    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.task_registry = self.manager.dict()
        self.commands = self.manager.dict()

    def put(self, job):
        self.task_registry[str(uuid.uuid4())] = serializer.encode(job)

    def get(self, key=None):
        if key is None:
            key = random.choice(self.task_registry.keys())

        if not self.task_registry.keys():
            return None

        if not self.task_registry.get(key):
            return None

        return serializer.decode(self.task_registry[key])

    def send_terminate_task(self):
        self.commands['terminate'] = serializer.encode(True)


    def put_result(self, value, uuid):
        result_ = result.Result()
        result_.value = value
        self.task_registry[uuid] = serializer.encode(result_)

    def stop(self):
        self.manager.shutdown()
        self.manager.join()
