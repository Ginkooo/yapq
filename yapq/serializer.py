import pickle

def encode(obj):
    raw = pickle.dumps(obj)
    return raw


def decode(raw):
    return pickle.loads(raw)
