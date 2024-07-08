from typing import Protocol

from src.domain.models.register import Register

class MessageQueueRepository(Protocol):
  @classmethod
  def send_message(cls, register: Register) -> None:
      raise NotImplementedError

  @classmethod
  def get_message(cls) -> Register:
      raise NotImplementedError
  
  @classmethod
  def clean_queue(cls) -> None:
     raise NotImplementedError
  
  @classmethod
  def count_messages(cls) -> int:
     raise NotImplementedError
  