import pandas as pd

from src.operations import get_operations_from_csv, get_operations_from_excel


# Тестируем функцию get_operations_from_csv
def test_get_operations_from_csv(mock_csv_file_path, mock_source_data, expected_list_of_dicts, mocker):
    """Тест успешного чтения корректного CSV-файла"""
    mock_read_csv = mocker.patch("pandas.read_csv")  # Используем библиотеку pytest-mock для имитации read_csv

    # Настраиваем mock_read_csv так, чтобы при вызове он возвращал наш mock_df
    mock_df = pd.DataFrame(mock_source_data)
    mock_read_csv.return_value = mock_df

    actual_result = get_operations_from_csv(mock_csv_file_path)  # Вызываем нашу функцию с фиктивным путем

    assert actual_result == expected_list_of_dicts  # Проверка, что тестируемая функция возвращает ожидаемый результат

    mock_read_csv.assert_called_once()  # Проверка, что функция read_csv вызвана ровно один раз


def test_file_not_found_error_csv(mock_csv_file_path, mocker):
    """Тест обработки ошибки FileNotFoundError"""
    mocker.patch(
        "pandas.read_csv", side_effect=FileNotFoundError
    )  # Настраиваем mocker.patch, чтобы он выбросил FileNotFoundError при вызове
    actual_result = get_operations_from_csv(mock_csv_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке


def test_value_error_scv(mock_csv_file_path, mocker):
    """Тест обработки ошибки ValueError (например, пустой или некорректный файл)"""
    mocker.patch(
        "pandas.read_csv", side_effect=ValueError
    )  # Настраиваем mocker.patch, чтобы он выбросил ValueError при вызове
    actual_result = get_operations_from_csv(mock_csv_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке


def test_exception_scv(mock_csv_file_path, mocker):
    """Тест обработки любых других непредвиденных исключений"""
    mocker.patch(
        "pandas.read_csv", side_effect=Exception
    )  # Настраиваем mocker.patch, чтобы он выбросил общее Exception при вызове
    actual_result = get_operations_from_csv(mock_csv_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке


# Тестируем функцию get_operations_from_excel
def test_get_operations_from_excel(mock_excel_file_path, mock_source_data, expected_list_of_dicts, mocker):
    """Тест успешного чтения корректного excel-файла"""
    mock_read_excel = mocker.patch("pandas.read_excel")  # Используем библиотеку pytest-mock для имитации read_excel

    # Настраиваем mock_read_excel так, чтобы при вызове он возвращал наш mock_df
    mock_df = pd.DataFrame(mock_source_data)
    mock_read_excel.return_value = mock_df

    actual_result = get_operations_from_excel(mock_excel_file_path)  # Вызываем нашу функцию с фиктивным путем

    assert actual_result == expected_list_of_dicts  # Проверка, что тестируемая функция возвращает ожидаемый результат

    mock_read_excel.assert_called_once()  # Проверка, что функция read_excel вызвана ровно один раз


def test_file_not_found_error_excel(mock_excel_file_path, mocker):
    """Тест обработки ошибки FileNotFoundError"""
    mocker.patch(
        "pandas.read_excel", side_effect=FileNotFoundError
    )  # Настраиваем mocker.patch, чтобы он выбросил FileNotFoundError при вызове
    actual_result = get_operations_from_excel(mock_excel_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке


def test_value_error_excel(mock_excel_file_path, mocker):
    """Тест обработки ошибки ValueError (например, пустой или некорректный файл)"""
    mocker.patch(
        "pandas.read_excel", side_effect=ValueError
    )  # Настраиваем mocker.patch, чтобы он выбросил FileNotFoundError при вызове
    actual_result = get_operations_from_excel(mock_excel_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке


def test_exception_excel(mock_excel_file_path, mocker):
    """Тест обработки любых других непредвиденных исключений"""
    mocker.patch(
        "pandas.read_excel", side_effect=Exception
    )  # Настраиваем mocker.patch, чтобы он выбросил общее Exception при вызове
    actual_result = get_operations_from_excel(mock_excel_file_path)  # Вызываем тестируемую функцию
    assert actual_result == []  # Ожидаем, что функция вернет пустой список при ошибке
