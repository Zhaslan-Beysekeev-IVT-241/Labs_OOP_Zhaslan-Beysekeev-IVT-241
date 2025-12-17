from typing import TypeVar, List, Tuple, Optional, Any

T = TypeVar('T')

# Типы для функционального подхода
Stack = List[T]
Queue = List[T]

# Операции со стеком
def create_stack() -> Stack[Any]:
    """Создать пустой стек"""
    return []

def push(stack: Stack[T], item: T) -> Stack[T]:
    """Добавить элемент в стек"""
    return stack + [item]  # Возвращаем новый список

def pop(stack: Stack[T]) -> Tuple[Optional[T], Stack[T]]:
    """Извлечь элемент из стека"""
    if not stack:
        return None, stack
    return stack[-1], stack[:-1]  # Возвращаем элемент и новый стек

def peek(stack: Stack[T]) -> Optional[T]:
    """Посмотреть верхний элемент"""
    if not stack:
        return None
    return stack[-1]

def is_stack_empty(stack: Stack[T]) -> bool:
    """Проверить, пуст ли стек"""
    return len(stack) == 0

def stack_size(stack: Stack[T]) -> int:
    """Получить размер стека"""
    return len(stack)

# Операции с очередью
def create_queue() -> Queue[Any]:
    """Создать пустую очередь"""
    return []

def enqueue(queue: Queue[T], item: T) -> Queue[T]:
    """Добавить элемент в очередь"""
    return queue + [item]  # Возвращаем новый список

def dequeue(queue: Queue[T]) -> Tuple[Optional[T], Queue[T]]:
    """Извлечь элемент из очереди"""
    if not queue:
        return None, queue
    return queue[0], queue[1:]  # Возвращаем элемент и новую очередь

def front(queue: Queue[T]) -> Optional[T]:
    """Посмотреть первый элемент"""
    if not queue:
        return None
    return queue[0]

def is_queue_empty(queue: Queue[T]) -> bool:
    """Проверить, пуста ли очередь"""
    return len(queue) == 0

def queue_size(queue: Queue[T]) -> int:
    """Получить размер очереди"""
    return len(queue)


# Пример использования функционального стиля:
if __name__ == "__main__":
    print("\n=== Функциональный стиль ===")
    
    # Работа со стеком
    stack = create_stack()
    stack = push(stack, 10)
    stack = push(stack, 20)
    stack = push(stack, 30)
    print(f"Стек: {stack}")
    
    top, stack = pop(stack)
    print(f"Извлечен элемент: {top}")
    print(f"Стек после извлечения: {stack}")
    
    # Работа с очередью
    queue = create_queue()
    queue = enqueue(queue, "первый")
    queue = enqueue(queue, "второй")
    queue = enqueue(queue, "третий")
    print(f"\nОчередь: {queue}")
    
    first, queue = dequeue(queue)
    print(f"Извлечен элемент: {first}")
    print(f"Очередь после извлечения: {queue}")
