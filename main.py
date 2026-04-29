from collections import deque
from typing import Optional


class FIFO:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue: deque[int] = deque()

    def add(self, val: int):
        if len(self.queue) == self.capacity:
            raise Exception("Already full")
        self.queue.append(val)

    def fetch(self) -> Optional[int]:
        if not self.queue:
            return None
        return self.queue.popleft()

def main():
    fifo_queue = FIFO(10)
    for i in range(1, 11):
        fifo_queue.add(i)
    while fifo_queue.queue:
        print(fifo_queue.fetch())

if __name__ == "__main__":
    main()
