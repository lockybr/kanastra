from queue import Queue

from src.domain.exceptions import EmptyQueueError
from src.domain.models.register import Register
from src.domain.repositories.message_queue_repository import MessageQueueRepository

class InMemoryMessageQueueRepository(MessageQueueRepository):
  queue = Queue()

  @classmethod
  def send_message(cls, register: Register) -> None:
    cls.queue.put(register)

  @classmethod
  def get_message(cls) -> Register:
    if cls.queue.empty():
      raise EmptyQueueError("The queue is empty.")
    
    return cls.queue.get()
    
  @classmethod
  def count_messages(cls) -> int:
    return cls.queue.qsize()
