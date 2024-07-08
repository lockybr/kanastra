import json
from unittest.mock import patch, Mock

import pytest

from src.application.services.file_service import CSVFileService
from src.domain.repositories.file_repository import FileRepository
from src.infrastructure.repositories.inmemory_message_queue_repository import InMemoryMessageQueueRepository
from src.infrastructure.repositories.file_history_repository import FileHistoryRepository


@pytest.mark.asyncio
@patch.object(FileHistoryRepository, "add")
@patch.object(FileRepository, "read_upload_file")
@patch.object(InMemoryMessageQueueRepository, "count_messages")
async def test_process_file_should_return_200_when_file_is_processed_successfully(
  mock_count_messages,
  mock_read_upload_file,
  spy_add
):
  mock_read_upload_file.return_value = 500
  mock_count_messages.return_value = 400
  
  response = await CSVFileService.process_file(Mock(), FileRepository)
  response_body = json.loads(response.body.decode("utf-8"))

  assert response.status_code == 200
  assert response_body["total_registers"] == 400
  spy_add.assert_called_once()


@pytest.mark.asyncio
@patch.object(FileRepository, "read_upload_file")
@patch.object(InMemoryMessageQueueRepository, "count_messages")
async def test_process_file_should_return_400_when_read_upload_file_raise_some_exception(
  spy_count_messages,
  mock_read_upload_file,
):
  mock_read_upload_file.side_effect = Exception("Ohhh nooo!!!")
  
  response = await CSVFileService.process_file(Mock(), FileRepository)
  response_body = json.loads(response.body.decode("utf-8"))

  assert response.status_code == 400
  assert response_body == {"error_message": "Error when processing file"}
  spy_count_messages.assert_not_called()


@pytest.mark.asyncio
@patch.object(InMemoryMessageQueueRepository, "send_message")
async def test_process_row_should_create_register_and_send_to_queue(
  spy_send_message,
  register_dict
):
  await CSVFileService._process_row(register_dict)

  spy_send_message.assert_called_once()


@pytest.mark.asyncio
@patch.object(InMemoryMessageQueueRepository, "send_message")
async def test_process_row_should_raise_exception_when_send_register_raise_some_exception(
  mock_send_message,
  register_dict
):
  mock_send_message.side_effect = Exception("Error Again :(")
  
  with pytest.raises(Exception) as e:
    await CSVFileService._process_row(register_dict)

  mock_send_message.assert_called_once()
  assert str(e.value) == "Error Again :("
