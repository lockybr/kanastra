import pytest

from fastapi.testclient import TestClient

from main import app
from src.domain.models.register import Register
from src.domain.models.file_history import FileHistory
from src.domain.models.bank_slip import BankSlip


@pytest.fixture
def client():
  return TestClient(app)


@pytest.fixture
def register_dict():
  return {
    "name": "mocked register name",
    "governmentId": 1234,
    "email": "mocked_register_email@test.com",
    "debtAmount": 8057,
    "debtDueDate": "2024-07-07",
    "debtId": 254782
  }


@pytest.fixture
def register_model(register_dict):
  return Register(
    name=register_dict.get("name"),
    government_id=register_dict.get("governmentId"),
    email=register_dict.get("email"),
    debt_amount=register_dict.get("debtAmount"),
    debt_due_date=register_dict.get("debtDueDate"),
    debt_id=register_dict.get("debtId")
  )

@pytest.fixture
def file_history_model():
  return FileHistory(
    filename="mocked_filename",
    size=25,
    amount_registers=100000
  )


@pytest.fixture
def csv_content():
  content = "name,governmentId,email,debtAmount,debtDueDate,debtId\nElijah Santos,9558,janet95@example.com,7811,2024-01-19,ea23f2ca-663a-4266-a742-9da4c9f4fcb3\nSamuel Orr,5486,linmichael@example.com,5662,2023-02-25,acc1794e-b264-4fab-8bb7-3400d4c4734d\n"
  return content

@pytest.fixture
def bank_slip_model(register_model):
  bank_slip = BankSlip(due_date=register_model.debt_due_date,value=register_model.debt_amount,payer_name=register_model.name)
  bank_slip.last_number = 1
  return bank_slip