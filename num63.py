class Queue:

    def __init__(self, size=1000):
        self.queue = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

    def dequeue(self):
        if self.isEmpty():
            print('Очередь переполнена!')
            exit(-1)
        x = self.queue[self.front]
        print('Удаление элемента: ', x)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return x

    def enqueue(self, value):
        if self.isFull():
            print('Очередь переполнена!')
            exit(-1)
        print('Добавление элемента: ', value)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.isEmpty():
            print('Очередь пуста!')
            exit(-1)
        return self.queue[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':
    q = Queue(5)