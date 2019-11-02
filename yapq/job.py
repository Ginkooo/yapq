import uuid

from yapq import result

class Job:

    def __init__(self, func, *args, **kwargs):
        self.uuid = str(uuid.uuid4())
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.func(*self.args, **self.kwargs)
