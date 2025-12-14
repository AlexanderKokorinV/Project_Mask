from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Декоратор. Оборачивает функцию для добавления логирования ее выполнения,
        результатов или ошибок в файл, указанный во внешней функции `log`.
        В качестве параметра принимает func: декорируемую функцию.
        Возвращает обернутую функцию `wrapper` с добавленным логированием."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка для декорированной функции.
            Логирует время начала и окончания выполнения функции `func`,
            ее результаты (при успехе) или тип ошибки (при исключении).
            Логирование осуществляется в файл, указанный в замыкании внешней
            функции `log`, либо в стандартный вывод (консоль).
            Принимает аргументы:
                *args: Позиционные аргументы декорируемой функции.
                **kwargs: Именованные аргументы декорируемой функции.
            Возвращает результат выполнения декорируемой функции `func`.
            """
            start_time = datetime.now()
            start_message = f"Start function {func.__name__} at {start_time}"  # Логируем начало выполнения функции
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(start_message + "\n")  # Добавляем перенос в конце строки
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                if "Ошибка" in result or result == []:  # Проверка типа возвращаемого значения
                    raise ValueError("Ошибка")  # Имитируем исключение, чтобы оно попало в блок except
                success_message = f"{func.__name__} ok. Result: {result}"  # Логирование успешного выполнения функции
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(success_message + "\n")
                        return result
                else:
                    print(success_message)
            except Exception as e:
                error_type = type(e).__name__
                error_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"  # Логирование ошибки
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
            finally:
                end_time = datetime.now()
                finish_message = (
                    f"Finish function {func.__name__} at {end_time}"  # Логируем завершение выполнения функции
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(finish_message)
                else:
                    print(finish_message)

        return wrapper

    return decorator
