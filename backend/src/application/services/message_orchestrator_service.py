from src.logging import logger
from src.domain import exceptions
from src.infrastructure.repositories.bank_slip_repository import BankSlipRepository
from src.infrastructure.repositories.inmemory_message_queue_repository import InMemoryMessageQueueRepository
from src.infrastructure.repositories.mail_service_repository import MailRepository


class MessageOrchestratorService:

    @classmethod
    def start(cls) -> None:

        try:
            register = InMemoryMessageQueueRepository.get_message()
        except exceptions.EmptyQueueError as e:
            logger.info(f"Error message: {str(e)}")
            return

        try:
            bank_slip = BankSlipRepository.generate(register)
        except exceptions.BankSlipGenerateError as e:
            # TODO: criar uma fila de erro para controlar melhor as retentativas
            InMemoryMessageQueueRepository.send_message(register)
            logger.info(f"Error message: {str(e)}")
            return

        try:
            MailRepository.send(register, bank_slip)
        except exceptions.EmailError:
            # TODO: criar uma fila de erro para controlar melhor as retentativas
            InMemoryMessageQueueRepository.send_message(register)
            logger.info(f"Error message: {str(e)}")
            
            