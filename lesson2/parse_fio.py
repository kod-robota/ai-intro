#!/usr/bin/env python

import click
import re
import requests
import random
import sys
import time

from natasha_wrap import get_names
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender
from jinja2 import Template


@click.command()
@click.option('-t', default=None, help='Templates file')
@click.option('--send', is_flag=True, default=False, help='Do send flag')
@click.option('--seen', default="seen_numbers.txt", help='File with seen numbers')
@click.argument('clients_fn') #, help="File with client names and numbers")
def main(t, send, seen, clients_fn):

 #
 # Для того, чтобы не отфильтровать номера, которым уже посылали сообщение
 #
 seen_numbers = []
 re_phone = re.compile('8\d{10}')

 try: 
  with open(seen, "r") as seenfd:
   for line in seenfd:
    found = re_phone.search(line)
    if found is None: continue
    seen_numbers.append(found.group(0))
    print(f"FOUND {found.group(0)} in {line.strip()}")
 except:
  print(f"Can not open {seen}")
 #sys.exit()

 #
 # Загрузка шаблонов
 #
 templates = []
 with open(t, "r") as tmplf:
   for line in tmplf:
     line = line.strip()
     if not line: continue
     templates.append(Template(line))
   #templates = tmplf.readlines()

 #
 # Склонения
 #
 p = Petrovich()
 # cased_lname = p.lastname(u'Алексеев', Case.GENITIVE, Gender.MALE)
 #print cased_lname  # > Алексеева


 # read and process clients
 clients={}

 #
 # Работа с файлом клиентов
 #
 with open(clients_fn, "r") as fio:

  for line in fio:
    if not "\t" in line:
        continue
    line = line.strip()
    # в файле имя и номер разделены знаком табуляции
    name, phone = line.split("\t")
 
    # отфильтровываем неправильные номера
    if not phone.startswith("8"):
        continue

    # дубликат
    if phone in clients or phone in seen_numbers:
        continue

    # Прводим имена к заглавным буквам
    name = name.strip().title()

    print(f"PHONE {phone} NAME {name} ", end='')

    #
    # Найдем имена в колонке имен. Нас интересует только имя (first name)
    #
    first = ""

    # Воспользуемся библиотекой natasha для NER, см. natasha_wrap.py

    # В поле имеми есть пробелы, наверняка там может быть и фамилия и другое
    if ' ' in name: 
       names = get_names(name)
       # если нашлось имя
       if "first" in names:
          first = names['first']
    # Если в поле имени только одно слово из букв
    # то предположим, что это и есть имя
    elif name.isalpha():
       first = name

    #
    # Просклоняем это имя для заданных падежей
    #
    client_decl = {}
    # винительный, родительный, дательный
    cases = ["ACCUSATIVE", "GENITIVE", "DATIVE"]
    for case in cases:
     if first:
       client_decl[f"first_{case[:3].lower()}"] = p.firstname(first, eval(f"Case.{case}"))
     else:
       # но если имени нет то так и оставляем пустое место
       client_decl[f"first_{case[:3].lower()}"] = ""

    print(f"FIRST {first} FIRST-DEC {client_decl}") # FIRST-G {first_acc}")
    
    clients[phone] = client_decl
      
      
 #
 # Отсылаем
 #
 for phone,first_decl in clients.items():

   # выбираем случайным образом шаблон письма из считанных из файла
   template_id = random.randint(0, len(templates)-1)
   #print(f"TEMPLATE ID {template_id} TEAMPLATES {len(templates)}")

   # Подставляем в шаблон имя в подходящем падеже
   text = templates[template_id].render(**first_decl)

   # это урл для сервиса cvc-визитка
   #url=f"{api_base}?api_key={api_key}&to={phone}&text={text}"
   print(text)

   continue

   # если в командной строке флаг --send
   # то делаем запрос к сервису и печатаем код ответа для контроля
   if not send:
     continue

   res = requests.get(url)
   print(res.status_code)

   # задержка, чтобы не нагружать сервис.
   time.sleep(random.randint(5, 9))


 #main
 return

if __name__ == "__main__":
    main()

