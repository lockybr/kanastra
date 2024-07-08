from fastapi import APIRouter, UploadFile, File

from src.application.services.file_service import CSVFileService
from src.application.services.file_history_service import FileHistoryService
from src.infrastructure.repositories.csv_file_repository import CSVFileRepository
from src.infrastructure.repositories.file_history_repository import FileHistoryRepository

router = APIRouter()

@router.post("/v1/file/")
async def file_upload_route(file: UploadFile):
    return await CSVFileService.process_file(file, CSVFileRepository)

@router.get("/v1/file/history/")
def get_file_history_route():
    return FileHistoryService.get_history(FileHistoryRepository)
