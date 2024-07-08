from io import BytesIO
from unittest.mock import patch

import pytest

from src.infrastructure.repositories.file_history_repository import FileHistoryRepository
from src.infrastructure.repositories.inmemory_message_queue_repository import InMemoryMessageQueueRepository


@pytest.mark.asyncio
async def test_upload_csv_should_return_200_when_file_is_successfully_processed(client, csv_content):
  file = BytesIO(csv_content.encode("utf-8"))
  files = {"file": ("test.csv", file, "text/csv")}

  response = client.post("/v1/file", files=files)
  response_json = response.json()

  assert response.status_code == 200
  assert response_json.get("total_registers") == 2
  assert len(FileHistoryRepository.history) == 1


@pytest.mark.asyncio
@patch.object(InMemoryMessageQueueRepository, "send_message")
async def test_upload_csv_should_return_400_when_some_error_is_raised(
  mock_send_message,
  client,
  csv_content
):
  mock_send_message.side_effect = Exception("Mocked Error")

  file = BytesIO(csv_content.encode("utf-8"))
  files = {"file": ("test.csv", file, "text/csv")}

  response = client.post("/v1/file", files=files)

  assert response.status_code == 400
  assert response.json() == {
    "error_message": "Error when processing file"
  }
