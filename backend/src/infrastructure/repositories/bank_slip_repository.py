from src.logging import logger
from src.domain.exceptions import BankSlipGenerateError
from src.domain.models.bank_slip import BankSlip
from src.domain.models.register import Register
from src.domain.repositories.bank_slip_repository import BankSlipRepositoryProtocol


class BankSlipRepository(BankSlipRepositoryProtocol):
  @classmethod
  def generate(cls, register: Register) -> BankSlip:
    try: 
      logger.info(f"Generating bank slip for '{register.name}'")

      bank_slip = BankSlip(register.debt_amount, register.debt_due_date, register.name)

      logger.info(f"Generated bank slip for '{register.name}' - number: {bank_slip.number}")
      return bank_slip
    except Exception as e:
      msg = f"Error when generating bank slip for {register.name}"
      logger.info(f"{msg} - error: {e}")
      raise BankSlipGenerateError(msg)
