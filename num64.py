class Stack:

    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def push(self, val):
        if self.isFull():
            print('Стэк переполнен!')
            exit(-1)

        print(f'Добавление {val} в стек')
        self.top = self.top + 1
        self.arr[self.top] = val

    def pop(self):
        if self.isEmpty():
            print('Стэк переполнен!')
            exit(-1)

        print(f'Удаление {self.peek()} из стэка')

        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity


if __name__ == '__main__':

    stack = Stack(2)

    stack.push(1)
    stack.push(2)
    # stack.push(3)

    stack.pop()
    stack.pop()

    stack.push(3)

    print('Верхний элемент стека: ', stack.peek())
    print('Размер стека: ', stack.size())

    stack.pop()

    if stack.isEmpty():
        print('Стэк пуст')
    else:
        print('Стек ожидает дальнейших действий')
