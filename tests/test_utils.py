import unittest
from unittest.mock import Mock, mock_open, patch
import json
from src.utils import get_transactions_from_json

class TestGetTransactionsFromJson(unittest.TestCase):
        MOCK_DATA = [                # Mock-данные, которые мы будем использовать в тестах
            {"id": 123, "amount": 10},
            {"id": 345, "amount": 20}
        ]
        MOCK_JSON_STR = json.dumps(MOCK_DATA) ## Строковое представление mock-данных для имитации содержимого файла
        @patch("builtins.open", new_callable=mock_open)
        def test_get_transactions_from_json(self, mock_file_open):
            """
            Тест успешного чтения корректного JSON-файла
            """
            mock_file_open.return_value.read.return_value = self.MOCK_JSON_STR #Настраиваем Mock-объект так, чтобы он "читал" наши данные
            result = get_transactions_from_json("fake/path/to/operations.json") #Вызываем нашу функцию с фиктивным путем

            self.assertEqual(result, self.MOCK_DATA) #Проверка, что тестируемая функция возвращает ожидаемый результат
            mock_file_open.assert_called_once_with("fake/path/to/operations.json", encoding="utf-8") #Проверка, что функция пыталась открыть файл с нужными параметрами

        @patch("builtins.open", new_callable=mock_open)
        def test_file_not_found(self, mock_file_open):
            """
            Тест обработки ситуации, когда файл не найден (FileNotFoundError).
            """
            mock_file_open.side_effect = FileNotFoundError #Заставляем mock_open выбросить FileNotFoundError при попытке открыть файл
            result = get_transactions_from_json("non/existent/file.json")

            self.assertEqual(result, []) # Ожидаем пустой список в случае ошибки
            mock_file_open.assert_called()  #Проверяем, что open вызывался

        @patch("builtins.open'", new_callable=mock_open)
        def test_invalid_json_format(self, mock_file_open):
            """
            Тест обработки ситуации, когда JSON файл поврежден (json.JSONDecodeError).
            """
            mock_file_open.return_value.read.return_value = "Это невалидный JSON" #Имитируем файл, содержащий невалидный JSON
            result = get_transactions_from_json("invalid/file.json")

            self.assertEqual(result, []) #Ожидаем пустой список в случае ошибки декодирования
            mock_file_open.assert_called()

        @patch("builtins.open", new_callable=mock_open)
        def test_empty_file_handling(self, mock_file_open):
            """
            Тест обработки пустого файла, который вызывает ValueError или JSONDecodeError.
            """
            mock_file_open.return_value.read.return_value = "" #Имитируем пустой файл
            result = get_transactions_from_json("empty/file.json")

            self.assertEqual(result, []) # Ожидаем пустой список
            mock_file_open.assert_called()
