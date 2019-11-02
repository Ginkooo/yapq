class Result:

    def __init__(self, uuid=None, task_registry=None):
        self.uuid = uuid
        self.task_registry = task_registry

    value = None

    def get(self):
        while not isinstance(self.task_registry.get(self.uuid), self.__class__):
            pass
        return self.task_registry.get(self.uuid).value
