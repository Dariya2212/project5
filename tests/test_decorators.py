from decorators import my_function


# Тестируем корректность работы декоратора
def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


# Тестируем правиьность работы декоратора при введении строовых значений
def test_log_str():
    try:
        my_function("1", 2)
    except TypeError:
        # читаем лог
        with open("mylog.txt", "r", encoding="utf-8") as f:
            log_content = f.read().strip()
        # Проверяем наличие сообщения об ошибке
        assert "error: TypeError" in log_content
        assert "Inputs: ('1', 2), {}" in log_content


# Тесть работы декоратора при введении нецелого числа
def test_log_float(capsys):
    my_function(1.2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
