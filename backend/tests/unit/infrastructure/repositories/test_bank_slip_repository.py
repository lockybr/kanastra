from unittest.mock import patch

import pytest

from src.domain.exceptions import BankSlipGenerateError
from src.infrastructure.repositories.bank_slip_repository import BankSlipRepository
from src.domain.models.bank_slip import BankSlip


def test_generate_should_return_bank_slip_when_bank_slip_is_created_successfully(
  register_model
):
  BankSlip.last_number = 0
  response = BankSlipRepository.generate(register_model)

  assert isinstance(response, BankSlip)
  assert response.due_date == register_model.debt_due_date
  assert response.payer_name == register_model.name
  assert response.value == register_model.debt_amount
  assert response.number == 1

  response = BankSlipRepository.generate(register_model)

  assert isinstance(response, BankSlip)
  assert response.due_date == register_model.debt_due_date
  assert response.payer_name == register_model.name
  assert response.value == register_model.debt_amount
  assert response.number == 2


@patch.object(BankSlip, "__init__")
def test_generate_should_return_raise_bank_slip_generate_error_when_some_exception_is_raised(
  mock_init,
  register_model
):
  mock_init.side_effect = Exception("Afff")

  with pytest.raises(BankSlipGenerateError) as e:
    BankSlipRepository.generate(register_model)
  
  assert str(e.value) == f"Error when generating bank slip for {register_model.name}"
  mock_init.assert_called_once_with(
    register_model.debt_amount, register_model.debt_due_date, register_model.name
  )
