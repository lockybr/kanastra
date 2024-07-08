from typing import Protocol

from src.domain.models.bank_slip import BankSlip
from src.domain.models.register import Register

class BankSlipRepositoryProtocol(Protocol):
  @classmethod
  def generate(cls, register:Register) -> BankSlip:
    raise NotImplementedError