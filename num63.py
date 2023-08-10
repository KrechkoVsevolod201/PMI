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

    def find(self, value):
        if self.isEmpty():
            print('Очередь пуста!')
            exit(-1)
        return self.queue.index(value) + 1

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
    q = Queue(3)
    search_element = 6
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(f'Элемент {search_element} в очереди под номером: ', q.find(search_element))
    # q.enqueue(4)
    print('Размер очереди: ', q.size())
    print('Передний элемент в очереди: ', q.peek())
    q.dequeue()
    print('Передний элемент в очереди: ', q.peek())

    q.dequeue()
    q.dequeue()

    if q.isEmpty():
        print('Очередь пуста')
    else:
        print('Очередь в ожидании действий')