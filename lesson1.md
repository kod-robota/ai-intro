# Занятие 1


## Демонстрации

![RuDALL-e сайт](https://rudalle.ru/)

[@sber_rudalle_xl_bot](http://t.me/sber_rudalle_xl_bot)

[AI да Пушкин](https://ai-pushkin.content.tinkoff.ru/)

[Балабоба - сервис недоступен с марта](https://yandex.ru/lab/yalm)

## Работа с Jupyter

## Скачать miniconda

### Запустить консоль и установить требуемые пакеты

```bash
$ conda install notebook nb_conda_kernels git
```

### Запуск Jupyter

В меню системы выберите Все Программы->Anaconda->Jupyter Notebook

Появляется окно с запуском команды и вкладка в браузере. Для остановки интерпретатора питона надо остановить процесс в окне командой Ctrl-C, потом закрыть вкладку в браузере.

### Простые задания в "тетрадке"

В правом внрхнем углу найдите New и выберите Python 3.

Напишите одну или несколько строчек в ячейке и нажмите Ctrl-Enter.

Пример: 

```python
2+2
```

```python
a = ["apples", "oranges"]
print(f"You are mixing {a[0]} and {a[1]} here!")
```

### Запуск тетрадки с примерами FaceLib 

В окне Anaconda Prompt 

Скачайте (склонируйте) репозиторий с кодом FaceLib

```bash
git clone https://github.com/datamove/FaceLib.git
```

cоздайте среду питона для запуска FaceLib

```bash
$ conda create -n faceenv ipykernel git
```

Установите требуемые пакеты:

```bash
conda activate faceenv
pip install -r FaceLib\requirements.txt
```

Во вкладке с каталогом найдите FaceLib, азйдите в нее и кликните на `examples.ipynb` 

## Работа с Colab



