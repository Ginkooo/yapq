import pickle


class Result:

    def __init__(self, uuid=None, result_dict=None):
        self.uuid = uuid
        self.result_dict = result_dict

    value = None

    def get(self):
        while self.uuid not in self.result_dict:
            pass
        value = pickle.loads(self.result_dict[self.uuid]).value
        del self.result_dict[self.uuid]
        return value
