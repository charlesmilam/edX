class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError

q = Queue()
print q.items
q.insert(0)
print q.items
q.insert(1)
print q.items
q.insert(3)
print q.items
q.remove()
print q.items
q.remove()
print q.items
q.remove()
print q.items
q.remove()
print q.items
