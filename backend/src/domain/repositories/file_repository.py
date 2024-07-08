from typing import Callable, Protocol

from fastapi import UploadFile


class FileRepository(Protocol):
  @classmethod
  async def read_upload_file(cls, file: UploadFile, callback: Callable = None):
    raise NotImplementedError
  