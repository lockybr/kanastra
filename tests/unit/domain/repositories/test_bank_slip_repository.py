import pytest

from src.domain.repositories.bank_slip_repository import BankSlipRepositoryProtocol

def test_generate_should_raise_not_implemented_error(register_model):
  with pytest.raises(NotImplementedError):
    BankSlipRepositoryProtocol.generate(register_model)
