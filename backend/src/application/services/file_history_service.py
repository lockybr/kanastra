from fastapi.responses import JSONResponse

from src.logging import logger
from src.domain.repositories.file_history_repository import FileHistoryRepositoryProtocol


class FileHistoryService:
  @classmethod
  def get_history(cls, file_history_repository: FileHistoryRepositoryProtocol) -> JSONResponse:
    try:
      list_history = file_history_repository.list_history()

      response = [history.to_dict for history in list_history]

      return JSONResponse(status_code=200, content=response)
  
    except Exception as e:
      msg = "Error when getting file history"
      logger.info(f"{msg} - Error: {str(e)}")
      return JSONResponse(status_code=400, content={"error_message": msg})
