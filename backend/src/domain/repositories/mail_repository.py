from typing import Protocol

from src.domain.models.bank_slip import BankSlip
from src.domain.models.register import Register

class MailRepositoryProtocol(Protocol):
  @classmethod
  def send(cls, register:Register, bank_slip: BankSlip) -> None:
    raise NotImplementedError