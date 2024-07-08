import time

from fastapi import UploadFile
from fastapi.responses import JSONResponse

from src.logging import logger
from src.domain.repositories.file_repository import FileRepository
from src.domain.models.register import Register
from src.domain.repositories.file_history_repository import FileHistory
from src.infrastructure.repositories.inmemory_message_queue_repository import InMemoryMessageQueueRepository
from src.infrastructure.repositories.file_history_repository import FileHistoryRepository


class CSVFileService:

    @classmethod
    async def process_file(cls, file: UploadFile, file_repository: FileRepository) -> JSONResponse:
        try:
            start_time = time.time()
            amount_registers = await file_repository.read_upload_file(file, cls._process_row)
            end_time = time.time()

            cls._send_file_history(file, amount_registers)

            response = {
                "time": str(end_time - start_time),
                "total_registers": InMemoryMessageQueueRepository.count_messages()
            }
            
            return JSONResponse(status_code=200, content=response)
        except Exception as e:
            msg = "Error when processing file"
            logger.info(f"{msg} - Error: {str(e)}")
            return JSONResponse(status_code=400, content={"error_message": msg})

    @classmethod
    async def _process_row(cls, row: dict) -> None:
        register = Register(
            name=row.get("name"),
            government_id=int(row.get("governmentId")),
            email=row.get("email"),
            debt_amount=int(row.get("debtAmount")),
            debt_due_date=row.get("debtDueDate"),
            debt_id=row.get("debtId")
        )

        cls._send_register_to_queue(register)

    @classmethod
    def _send_register_to_queue(cls, register: Register) -> None:
        InMemoryMessageQueueRepository.send_message(register)
    
    @classmethod
    def _send_file_history(cls, file: UploadFile, amount_registers: int) -> None:
        file_history = FileHistory(
            filename=file.filename,
            size=file.file._max_size,
            amount_registers=amount_registers
        )

        FileHistoryRepository.add(file_history)
