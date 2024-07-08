from unittest.mock import patch

from src.application.services.message_orchestrator_service import MessageOrchestratorService
from src.infrastructure.repositories.bank_slip_repository import BankSlipRepository
from src.infrastructure.repositories.inmemory_message_queue_repository import InMemoryMessageQueueRepository
from src.infrastructure.repositories.mail_service_repository import MailRepository
from src.domain import exceptions 

@patch.object(MailRepository, "send")
@patch.object(BankSlipRepository, "generate")
@patch.object(InMemoryMessageQueueRepository, "get_message")
def test_start_should_call_all_services_successfully(mock_get_message, mock_generate, mock_send, register_model,bank_slip_model):
    mock_get_message.return_value = register_model
    mock_generate.return_value = bank_slip_model
    MessageOrchestratorService.start()
    mock_generate.assert_called_with(register_model)
    mock_send.assert_called_with(register_model,bank_slip_model)


@patch.object(MailRepository, "send")
@patch.object(BankSlipRepository, "generate")
@patch.object(InMemoryMessageQueueRepository, "get_message")
def test_start_should_return_none_when_empty_queue_error_raised(mock_get_message, mock_generate, mock_send, register_model,bank_slip_model):
    mock_get_message.side_effect = exceptions.EmptyQueueError
    MessageOrchestratorService.start()
    mock_generate.assert_not_called()
    mock_send.assert_not_called()

@patch.object(MailRepository, "send")
@patch.object(BankSlipRepository, "generate")
@patch.object(InMemoryMessageQueueRepository, "get_message")
def test_start_should_return_none_when_bank_slip_error_raised(mock_get_message, mock_generate, mock_send, register_model,bank_slip_model):
    mock_get_message.return_value = register_model
    mock_generate.side_effect = exceptions.BankSlipGenerateError
    MessageOrchestratorService.start()
    mock_send.assert_not_called()

@patch.object(MailRepository, "send")
@patch.object(BankSlipRepository, "generate")
@patch.object(InMemoryMessageQueueRepository, "get_message")
def test_start_should_return_none_when_email_error_raised(mock_get_message, mock_generate, mock_send, register_model,bank_slip_model):
    mock_get_message.return_value = register_model
    mock_generate.return_value = bank_slip_model
    mock_send.side_effect = exceptions.EmailError
    MessageOrchestratorService.start()
    mock_send.assert_called_with(register_model,bank_slip_model)