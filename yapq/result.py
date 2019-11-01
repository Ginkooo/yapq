class Result:
    value = None
    ready = False

    def get(self):
        while not self.ready:
            pass
        return self.value
