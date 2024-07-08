import time

from src.logging import logger
from src.domain.exceptions import EmailError
from src.domain.models.bank_slip import BankSlip
from src.domain.models.register import Register
from src.domain.repositories.mail_repository import MailRepositoryProtocol


class MailRepository(MailRepositoryProtocol):
  @classmethod
  def send(cls, register: Register, bank_slip: BankSlip) -> None:
    try:
      logger.info(f"Sending email for {register.email} due to bank slip {bank_slip.number}")

      time.sleep(2)

      logger.info(f"Sent email for {register.email} due to bank slip {bank_slip.number}")
    except Exception as e:
      msg = f"Error when sending email for {register.name}"
      logger.info(f"{msg} - error: {e}")
      raise EmailError(msg)
