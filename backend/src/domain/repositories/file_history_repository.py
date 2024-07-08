from typing import Protocol

from src.domain.models.file_history import FileHistory

class FileHistoryRepositoryProtocol(Protocol):
  @classmethod
  def add(cls, file_history: FileHistory) -> None:
    raise NotImplementedError
  
  @classmethod
  def list_history(cls) -> list[FileHistory]:
    raise NotImplementedError
