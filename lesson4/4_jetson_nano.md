# Jetson Nano

## Запись образа

Скачать с официального сайта:

* [Jetson Nano 2GB Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-2gb-sd-card-image)
* [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image)

### Windows

Официальное руководство рекомендует [SD Memory Card Formatter for Windows](https://www.sdcard.org/downloads/formatter_4/eula_windows/).

### Linux, MAC

```bash
/usr/bin/unzip -p jetson-nano-2gb-jp46-sd-card-image.zip | sudo /bin/dd of=/dev/mmcblk0 bs=4M status=progress
```

## Первая загрузка

Конфигурация, пользователь и т д

kod:kod123

## Проверка работы с камерой

`nvgstcapture-1.0`

должна запуститься трансляция с камеры на экран. Документация пишет, что можно нажать j для снимка и q для выхода, но у меня получалось только ctrl-с.

Для USB-камеры,

nvgstcapture-1.0 --camsrc=0 --cap-dev-node=0

Последний 0 - это из /dev/video0 - проверьте.

Если камера не работает, что-то не то, проверьте подключение, перезагрузите етс.

## Установка среды для работы с моделями ИИ

Склонируйте репозиторий 

```bash
git clone --recursive https://github.com/dusty-nv/jetson-inference
```

Зайдите в него и запустите

```bash
sudo apt-get update
sudo docker/run.sh
```

Если все прошло хорошо, то он запустит диалог для выбора моделей для скачивания. Оставьте как есть, но прокрутите вниз и выберите обе модель суперразрешения.

Этот инструмент можно запустить и позже:

```bash
cd jetson-inference/tools
./download-models.sh
```

Далее он загрузит контейнер в интерактивном режиме. Выход из него - Ctrl-D.

## Что это за docker?

```bash 
sudo docker pull hello-world
sudo docker run hello-world
```

## Разпознавание

```bash
cd build/aarch64/bin
./imagenet images/jellyfish.jpg images/test/jellyfish.jpg
```

Опции для распознавания

## Детекция

```bash
./detectnet images/peds_0.jpg images/test/peds_0.jpg
```

Это все программы на С++, а еще там еcть на питоне. посмотрите в той же папке.

Опции для детекции.

## Запуск контейнера в пакетном режиме - неинтерактивном

```bash
sudo docker/run.sh -r detectnet mages/peds_0.jpg images/test/peds_0.jpg
```

## Сборка своего контейнера

Например, свою программу.

