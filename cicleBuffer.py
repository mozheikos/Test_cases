from collections import deque
"""Реализовал циклический буфер без переполнения (теряющий данные при добавлении в полный буфер).
Вариант 1 будет выигрывать по скорости в случае, когда операций чтения больше чем операций записи, так как поиск
элемента в ячейке памяти, представляющей собой 'середину' буфера (когда было добавлено одно знчение, а взято несколько)
проще в словаре. В случае, если буфер наполняется быстрее чем считывается - выйграет 2 вариант (очередь быстрее работает
с крайними элементами)"""


class CircleBuffer:
    
    def __init__(self, length):
        self.length = length
        self.buffer = dict.fromkeys(range(self.length))
        self.fill = 0
        self.head = 0
        self.tail = 0
        
    def write(self, data):
        self.buffer[self.head] = data
        if self.head == self.tail and self.fill == self.length:
            self.tail = self.head + 1
        self.head = self.head + 1 if self.head + 1 < self.length else 0
        if self.fill < self.length:
            self.fill += 1

    def read(self):
        data = self.buffer[self.tail]
        self.tail = self.tail + 1 if self.tail + 1 < self.length else 0
        return data

    def __str__(self):
        string = ''
        for i in range(self.length):
            if self.buffer[i]:
                string += str(self.buffer[i])
            else:
                string += '-'
        return string


class CircleBufferVar2:

    def __init__(self, length):
        self.length = length
        self.buffer = deque(maxlen=self.length)
        self.tail = 0

    def write(self, data):
        if self.tail and len(self.buffer) == self.length:
            self.tail -= 1
        self.buffer.append(data)

    def read(self):
        data = self.buffer[self.tail]
        self.tail = self.tail + 1 if self.tail + 1 < self.buffer.maxlen else 0
        return data

    def __str__(self):
        return ''.join(list(map(str, self.buffer)))
