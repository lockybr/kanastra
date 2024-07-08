import pytest

from src.domain.repositories.file_history_repository import FileHistoryRepositoryProtocol

def test_add_must_raise_not_implemented_error(file_history_model):
  with pytest.raises(NotImplementedError):
    FileHistoryRepositoryProtocol.add(file_history_model)


def test_list_history_must_raise_not_implemented_error():
  with pytest.raises(NotImplementedError):
    FileHistoryRepositoryProtocol.list_history()
