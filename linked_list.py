"""Custom singly linked list used as the primary in-memory DSA structure."""
from dataclasses import dataclass
from typing import Any, Optional, Iterable


@dataclass
class Node:
    data: dict
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0

    def __len__(self):
        return self._size

    def insert_end(self, data: dict) -> None:
        """Insert a record at the tail. O(n), or O(1) with a maintained tail."""
        node = Node(dict(data))
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def search(self, record_id: int) -> Optional[Node]:
        """Linear search by record ID. O(n)."""
        current = self.head
        while current is not None:
            if current.data["id"] == record_id:
                return current
            current = current.next
        return None

    def delete(self, record_id: int) -> bool:
        """Delete the first matching record. O(n)."""
        previous = None
        current = self.head
        while current is not None:
            if current.data["id"] == record_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return True
            previous, current = current, current.next
        return False

    def update(self, record_id: int, new_data: dict) -> bool:
        node = self.search(record_id)
        if node is None:
            return False
        node.data = dict(new_data)
        return True

    def traverse(self) -> list:
        records = []
        current = self.head
        while current is not None:
            records.append(dict(current.data))
            current = current.next
        return records

    def clear(self) -> None:
        self.head = None
        self._size = 0

    @classmethod
    def from_iterable(cls, records: Iterable[dict]):
        linked = cls()
        for record in records:
            linked.insert_end(record)
        return linked
