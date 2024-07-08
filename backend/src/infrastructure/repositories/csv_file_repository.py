import asyncio
import csv
from io import StringIO
from typing import Callable

from fastapi import UploadFile

from src.domain.repositories.file_repository import FileRepository

class CSVFileRepository(FileRepository):
  @classmethod
  async def read_upload_file(cls, file: UploadFile, callback: Callable = None) ->list[dict] | int:
    content = await file.read()
    csv_content = StringIO(content.decode("utf-8"))
    reader = csv.DictReader(csv_content)

    if callback and callable(callback):
      tasks = [callback(row) for row in reader]
      await asyncio.gather(*tasks)
      return len(tasks)
    
    return [dict(row) for row in reader]
