from yapq import result

class Job:

    def __init__(self, func, *args, **kwargs):
        self.result = result.Result()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        value = self.func(*self.args, **self.kwargs)
        self.result.value = value
        self.result.ready = True
