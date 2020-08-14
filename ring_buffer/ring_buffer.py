from doubly_linked_list import DoublyLinkedList


# class RingBuffer:
# def __init__(self, capacity):
#     self.capacity = capacity
#     self.current = None
#     self.storage = DoublyLinkedList()

# def append(self, item):
#     # check to see if the list is completely full
#     if len(self.storage) < self.capacity:
#         self.storage.add_to_tail(item)
#         self.current = self.storage.head
#     else:
#         if not self.current.next:
#             self.current.value = item
#             self.current = self.storage.head
#         else:
#             self.current.value = item
#             self.current = self.current.next

# def get(self):
#     ring_buffer_content = []

#     current = self.storage.head
#     while current:
#         ring_buffer_content.append(current.value)
#         current = current.next
#     return ring_buffer_content


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = []

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        # If we reach the capacity of the buffer
        # set the current pointer back to the beginning
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return [x for x in self.storage if x is not None]
