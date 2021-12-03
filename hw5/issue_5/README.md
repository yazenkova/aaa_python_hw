Для запука требуется установка pytest, pytest-cov:

`$ pip install -U pytest`

`$ pip install pytest-cov`

Запуск из терминала (предварительно перейдя в нужную директорию issue_5) с информацией о покрытии:

`$ python -m pytest --cov`

Чтобы получить html отчет о покрытии:

`$ python -m pytest --cov --cov-report html`