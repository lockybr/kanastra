import pytest
from io import BytesIO

from fastapi import UploadFile

from src.infrastructure.repositories.csv_file_repository import CSVFileRepository


@pytest.mark.asyncio
async def test_read_upload_file_should_return_list_of_elements_when_there_is_no_callback(csv_content):
  upload_file = UploadFile(filename="test.csv", file=BytesIO(csv_content.encode("utf-8")))

  result = await CSVFileRepository.read_upload_file(upload_file)

  expected_result = [
      {
        "name": "Elijah Santos",
        "governmentId": "9558",
        "email": "janet95@example.com",
        "debtAmount": "7811",
        "debtDueDate": "2024-01-19",
        "debtId": "ea23f2ca-663a-4266-a742-9da4c9f4fcb3"
      },
      {
        "name": "Samuel Orr",
        "governmentId": "5486",
        "email": "linmichael@example.com",
        "debtAmount": "5662",
        "debtDueDate": "2023-02-25",
        "debtId": "acc1794e-b264-4fab-8bb7-3400d4c4734d"
      }
  ]
  assert result == expected_result


@pytest.mark.asyncio
async def test_read_upload_file_should_return_number_of_rows_when_there_is_callback(csv_content):
  upload_file = UploadFile(filename="test.csv", file=BytesIO(csv_content.encode("utf-8")))

  processed_rows = []

  async def callback(row):
      processed_rows.append(row)

  result = await CSVFileRepository.read_upload_file(upload_file, callback)

  assert result == 2
  expected_processed_rows = [
      {
        "name": "Elijah Santos",
        "governmentId": "9558",
        "email": "janet95@example.com",
        "debtAmount": "7811",
        "debtDueDate": "2024-01-19",
        "debtId": "ea23f2ca-663a-4266-a742-9da4c9f4fcb3"
      },
      {
        "name": "Samuel Orr",
        "governmentId": "5486",
        "email": "linmichael@example.com",
        "debtAmount": "5662",
        "debtDueDate": "2023-02-25",
        "debtId": "acc1794e-b264-4fab-8bb7-3400d4c4734d"
      }
  ]
  assert processed_rows == expected_processed_rows


@pytest.mark.asyncio
async def test_read_upload_file_should_return_list_of_elements_when_callback_is_invalid(csv_content):
  upload_file = UploadFile(filename="test.csv", file=BytesIO(csv_content.encode("utf-8")))

  invalid_callback = "not a function"

  result = await CSVFileRepository.read_upload_file(upload_file, invalid_callback)

  expected_result = [
      {
        "name": "Elijah Santos",
        "governmentId": "9558",
        "email": "janet95@example.com",
        "debtAmount": "7811",
        "debtDueDate": "2024-01-19",
        "debtId": "ea23f2ca-663a-4266-a742-9da4c9f4fcb3"
      },
      {
        "name": "Samuel Orr",
        "governmentId": "5486",
        "email": "linmichael@example.com",
        "debtAmount": "5662",
        "debtDueDate": "2023-02-25",
        "debtId": "acc1794e-b264-4fab-8bb7-3400d4c4734d"
      }
  ]
  assert result == expected_result


@pytest.mark.asyncio
async def test_read_upload_file_should_raise_exception_when_callback_raise_some_exception(csv_content):
  upload_file = UploadFile(filename="test.csv", file=BytesIO(csv_content.encode("utf-8")))

  async def callback(_row):
    raise Exception("Mocked Exception :)")

  with pytest.raises(Exception) as e:
    await CSVFileRepository.read_upload_file(upload_file, callback)

  assert str(e.value) == "Mocked Exception :)"
