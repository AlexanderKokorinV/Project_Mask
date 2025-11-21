from functools import wraps
from typing import Any
from datetime import datetime

def log(filename: str) -> None:
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            start_message = f"Start function {func.__name__} at {start_time}" #Логируем начало выполнения функции
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(start_message + "\n") #Добавляем перенос в конце строки
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                if "Ошибка" in result or result == []:
                    raise ValueError("Ошибка")
                success_message = f"{func.__name__} ok. Result: {result}" #Логирование успешного выполнения функции
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(success_message + "\n")
                        return result
                else:
                    print(success_message)
            except Exception as e:
                error_type = type(e).__name__
                error_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}" #Логирование ошибки
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")
                else:
                    print(error_message)
            finally:
                end_time = datetime.now()
                finish_message = f"Finish function {func.__name__} at {end_time}" #Логируем завершение выполнения функции
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(finish_message)
                else:
                    print(finish_message)
        return wrapper
    return decorator
