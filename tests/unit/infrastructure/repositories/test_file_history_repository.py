from src.infrastructure.repositories.file_history_repository import FileHistoryRepository

def test_add_should_add_a_file_history_successefully(file_history_model):
    FileHistoryRepository.add(file_history_model)
    assert FileHistoryRepository.history == [file_history_model]

    
def test_list_history_should_return_a_history_successefully(file_history_model):
    FileHistoryRepository.history = []
    FileHistoryRepository.history = [file_history_model, file_history_model]
    response = FileHistoryRepository.list_history()
    assert len(response) == 2
    assert response == FileHistoryRepository.history