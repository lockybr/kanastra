import json
from unittest.mock import patch

from src.application.services.file_history_service import FileHistoryService
from src.domain.repositories.file_history_repository import FileHistoryRepositoryProtocol


@patch.object(FileHistoryRepositoryProtocol, "list_history")
def test_get_history_should_return_200_when_list_history_returns_successfully(
  mock_list_history,
  file_history_model
):
  mock_list_history.return_value = [file_history_model]
  
  response = FileHistoryService.get_history(FileHistoryRepositoryProtocol)

  expected_response_body = [{**file_history_model.to_dict}]

  assert response.status_code == 200
  assert json.loads(response.body.decode("utf-8")) == expected_response_body


@patch.object(FileHistoryRepositoryProtocol, "list_history")
def test_get_history_should_return_400_when_list_history_raise_some_exception(
  mock_list_history
):
  mock_list_history.side_effect = Exception("Oopppssss!!!")

  response = FileHistoryService.get_history(FileHistoryRepositoryProtocol)

  assert response.status_code == 400
  assert json.loads(response.body.decode("utf-8")) == {"error_message": "Error when getting file history"}