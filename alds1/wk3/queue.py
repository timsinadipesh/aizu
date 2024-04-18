"""
a program which simulates the round-robin scheduling
"""

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


n, q = map(int, input().split(" "))
queue = Queue()

for i in range(n):
    line = input().split(" ")
    name, time = line[0], int(line[1])
    queue.enqueue([name, time])

total_time = 0
while queue.size():
    name, time = queue.dequeue()
  
    if time <= q:
        total_time += time
        print(name, total_time)
    else:
        queue.enqueue((name, time - q))
        total_time += q


    

    

    