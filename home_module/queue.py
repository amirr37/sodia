from typing import Iterator

class Queue:
    def __init__(self):
        self.queue = []


    def __iter__(self) -> Iterator:
        if len(self.queue)==0:
            print("queue is empty.")
            return
        data, next_item = self.head.data, self.head.next
        yield data
        while next_item is not None:
            data, next_item = next_item.data, next_item.next
            yield data

    def en_queue(self, item):
        self.queue.append(item)
        return True

    def de_queue(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]
