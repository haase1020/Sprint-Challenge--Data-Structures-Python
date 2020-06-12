from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if the list is completely full
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head  # check where head is initialized
        else:
            if not self.current.next:
                self.current.value = item
                self.current = self.storage.head
            else:
                self.current.value = item
                self.current = self.current.next

    def get(self):
        ring_buffer_content = []

        current = self.storage.head
        while current:
            ring_buffer_content.append(current.value)
            current = current.next
        return ring_buffer_content
