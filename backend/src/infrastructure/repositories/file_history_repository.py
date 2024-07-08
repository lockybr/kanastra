from src.domain.models.file_history import FileHistory
from src.domain.repositories.file_history_repository import FileHistoryRepositoryProtocol

class FileHistoryRepository(FileHistoryRepositoryProtocol):
  history = []

  @classmethod
  def add(cls, file_history: FileHistory) -> None:
    cls.history.append(file_history)

  @classmethod
  def list_history(cls) -> list[FileHistory]:
    return cls.history
