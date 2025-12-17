from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    """Очередь (FIFO) в ООП стиле"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def enqueue(self, item: T) -> None:
        """Добавить элемент в очередь"""
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        """Извлечь элемент из очереди"""
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self) -> Optional[T]:
        """Посмотреть первый элемент без извлечения"""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь"""
        return len(self._items) == 0

    def size(self) -> int:
        """Получить размер очереди"""
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue({self._items})"


class Stack(Generic[T]):
    """Стек (LIFO) в ООП стиле"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Добавить элемент в стек"""
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Извлечь элемент из стека"""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        """Посмотреть верхний элемент без извлечения"""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Проверить, пуст ли стек"""
        return len(self._items) == 0

    def size(self) -> int:
        """Получить размер стека"""
        return len(self._items)

    def __str__(self) -> str:
        return f"Stack({self._items})"


# Пример использования:
if __name__ == "__main__":
    # Тестирование Queue
    print("=== Тестирование Queue ===")
    q = Queue[int]()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Очередь: {q}")
    print(f"Первый элемент: {q.peek()}")
    print(f"Извлекаем: {q.dequeue()}")
    print(f"Очередь после извлечения: {q}")
    print(f"Размер: {q.size()}")
    print(f"Пустая? {q.is_empty()}")

    # Тестирование Stack
    print("\n=== Тестирование Stack ===")
    s = Stack[str]()
    s.push("A")
    s.push("B")
    s.push("C")
    print(f"Стек: {s}")
    print(f"Верхний элемент: {s.peek()}")
    print(f"Извлекаем: {s.pop()}")
    print(f"Стек после извлечения: {s}")
    print(f"Размер: {s.size()}")
    print(f"Пустой? {s.is_empty()}")
