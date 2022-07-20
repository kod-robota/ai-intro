# Raspberry pi

## Установка

При создании аккаунта, введите название аккаунта kod и пароль kod123.

## Подключение

## Знакомство с системой


Определите ваш IP-адрес

```bash
ip a
```
и запишите его.

## ssh

### Установка

```bash
$ sudo apt install openssh-server
$ sudo systemctl start ssh
```

(так же можно воспользоваться raspi-config)

### Проверка

```bash
ssh pi@localhost
```

введите пароль (raspberry)

Если все прошло хорошо, то переключите дисплей и клавиатуру назад на кромпьютер и попробуйте набрать команду в терминале Windows:

```bash
ssh pi@xx.xx.xx.xx
``` 

где xx - это ваш Ip-адрес.

# Camera

`raspistill -o newpic.jpg -n`

# Telegram bot

## Подготовка

* /newbot - короткое описание, никнейм_bot. Запишите токен
* или воспользуйтесь моим (удалите пробелы): 5547185149 : AAEwdOAD-pSAvNwcjsl4Km_pwEcwN1c9DdY
* найдите ваш бот в телефоне, нажмите start. 
* или мой бот:  t.me/kr_photo_bot
* Найдите ваш Id
* или возьмите мой (будете мне присылать): 476691449

## getupdates

`curl https://api.telegram.org/botTOKEN/getUpdates`

## sendMessage

`curl -X POST --data "chat_id=11122233" --data "text=hello from bot" "https://api.telegram.org/bot<token>/sendMessage"`

## sendphoto

`curl https://api.telegram.org/botTOKEN/sendphoto -F chat_id=11112222333 -F photo=@newpic.jpg`

# Автоматизация

## скрипт для получения ip-адреса

## запуск скрипта при загрузке

`crontab -e`

редактируем:

`@reboot /home/pi/myip.sh`

## запуск по расписанию

В 0,15,30,45 минут каждого часа с 9 до 18 каждый день 25-29 июля.

`0,15,30,45 9-18 25-29 7 * /home/pi/takepic.sh`

