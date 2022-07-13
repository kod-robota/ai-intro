# Natural Language processing

## Подготовка среды

В miniconda prompt (как администратор) создайте новую среду и установите требуемые пакеты:

```bash
conda create -n nlpenv ipykernel
conda activate nplenv
conda install gensym
```

## Клонирование (копирование) репозитория

В minicinda prompt исзмените директорию на домашнюю (C:\Users\440 или какая там) и дайте следующую команду:

```bash
git clone https://github.com/kod-robota/ai-intro.git
```

теперь в вашей домашней директории появилась папка ai-intro, в подпапке lesson2 надите файлы `*.ipynb` и другие нужные для практической части.

## word2vec - обучение модели

Скачайте какой-нибудь корпус. Например, роман Льва Толстого Анна Каренина.

Для удобства, текст уже в репозитории, по [ссылке](anna-karenina.txt).

Создайте новую тетрадку Jupyter со средой nlpenv (Kernel->Change) или запустите тетрадку [word2vec-train.ipynb](word2vec-train.ipynb) из репо.


## word2vec - предобученная модель

Создайте новую тетрадку Jupyter со средой nlpenv (Kernel->Change)

## NER, склонения

Установите в среду nlpenv дополнительные пакеты:

```bash
pip install natasha petrovich click requests jinja2
```

посмотрите программу `parse_fio.py`, `natasha_wrap.py`, файл с шаблонами `templates_summer22.txt` и запустите ее:

```bash
python parse_fio.py -t templates_summer22.txt  fio_phones-aa-aa
```

она выдаст сообщения, с шаблонами в соответствующем падеже. Посмотрите строки в файле с клиентами, из которых он не смог вытащить имена.

## Генерация текста

Откройте в колабе:

### ruGPT-3 маленькая модель

https://colab.research.google.com/github/ai-forever/ru-gpts/blob/master/examples/Generate_text_with_RuGPTs_HF.ipynb

### ruGPT-3 XL

https://colab.research.google.com/github/ai-forever/ru-gpts/blob/master/examples/ruGPT3XL_generation.ipynb

### ruGPT-3 c подстройками

https://colab.research.google.com/github/ai-forever/ru-gpts/blob/master/examples/ruGPT3XL_finetune_example.ipynb

### Больше примеров

https://github.com/ai-forever


