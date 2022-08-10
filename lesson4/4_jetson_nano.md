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

`nvgstcapture-1.0 --camsrc=0 --cap-dev-node=0`

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

[Мини-тюториал](4_docker.md)


## Разпознавание

```bash
cd build/aarch64/bin
./imagenet images/jellyfish.jpg images/test/jellyfish.jpg
```

Посмотрите в проводнике, в jetson-inference/data/images/test.


## Опции для распознавания

Запуск без аргументов включает стрим с камеры, в угу пишет все, что нашел.

* --network=resnet-18 
* --width, --height - размеры изображения с камеры
* --headless - без вывода изображения на экран

## Детекция

```bash
./detectnet images/peds_0.jpg images/test/peds_0.jpg
```

Это все программы на С++, а еще там еcть на питоне. посмотрите в той же папке.

Опции для детекции.

* --network SSD-Mobilenet-v2
* --overlay=box,labels,conf  где box можно заменить на lines
* --alpha 120 - некое значение насыщенности наложения прямоугольника
* --threshold 0.5 - порог распознавания

Можно распознавать сразу много фото:

`./detectnet "images/peds_*.jpg" images/test/peds_output_%i.jpg`

Можно так же распознавать на роликах:

```bash
wget https://nvidia.box.com/shared/static/veuuimq6pwvd62p9fresqhrrmfqz0e2f.mp4 -O pedestrians.mp4
./detectnet pedestrians.mp4 images/test/pedestrians_ssd.mp4
```

### Сети

| Model                   | CLI argument       | NetworkType enum   | Object classes       |
| ------------------------|--------------------|--------------------|----------------------|
| SSD-Mobilenet-v1        | `ssd-mobilenet-v1` | `SSD_MOBILENET_V1` | 91 COCO classes      |
| SSD-Mobilenet-v2        | `ssd-mobilenet-v2` | `SSD_MOBILENET_V2` | 91 COCO classes      |
| SSD-Inception-v2        | `ssd-inception-v2` | `SSD_INCEPTION_V2` | 91 COCO classes      |
| DetectNet-COCO-Dog      | `coco-dog`         | `COCO_DOG`         | dogs                 |
| DetectNet-COCO-Bottle   | `coco-bottle`      | `COCO_BOTTLE`      | bottles              |
| DetectNet-COCO-Chair    | `coco-chair`       | `COCO_CHAIR`       | chairs               |
| DetectNet-COCO-Airplane | `coco-airplane`    | `COCO_AIRPLANE`    | airplanes            |
| ped-100                 | `pednet`           | `PEDNET`           | pedestrians          |
| multiped-500            | `multiped`         | `PEDNET_MULTI`     | pedestrians, luggage |
| facenet-120             | `facenet`          | `FACENET`          | faces                |

* [COCO classes](https://github.com/dusty-nv/jetson-inference/blob/master/data/networks/ssd_coco_labels.txt)

## Сегментация

Это - классификация для каждого пиксела, так что получается заполненный контур вместо прямоугольника.

```bash
./segnet --network=fcn-resnet18-cityscapes images/city_0.jpg images/test/output.jpg
```

## Определение позы

Для USB-камеры, а для CSI не надо аргумента

```bash
./posenet /dev/video0
```

| Model                   | CLI argument       | NetworkType enum   | Keypoints |
| ------------------------|--------------------|--------------------|-----------|
| Pose-ResNet18-Body      | `resnet18-body`    | `RESNET18_BODY`    | 18        |
| Pose-ResNet18-Hand      | `resnet18-hand`    | `RESNET18_HAND`    | 21        |
| Pose-DenseNet121-Body   | `densenet121-body` | `DENSENET121_BODY` | 18        |

## Глубина сцены с однообъективной камеры

```bash
./depthnet "images/room_*.jpg" images/test/depth_room_%i.jpg
```

## Дообучение сети

Выгодно учить сеть не с нуля, а доучивать на своих фото.
Можно и на Jetson Nano, но очень долго.

| Type | Dataset   | Size  |  Classes | Training Images | Time per Epoch* | Training Time** |
|:-----------:|:-----------:|:-------:|:----------:|:-----------------:|:-----------------:|:-----------------:|
| Classification | [`Cat/Dog`](pytorch-cat-dog.md)   | 800MB |    2    |      5,000      |  ~7-8 minutes   |    ~4 hours     |
| Classification | [`PlantCLEF`](pytorch-plants.md) | 1.5GB |   20    |     10,475      | ~15 minutes     |    ~8 hours     |
| Detection | [`Fruit`](pytorch-ssd.md) | 2GB |   8    |     6,375      | ~15 minutes     |    ~8 hours     |





## Запуск контейнера в пакетном режиме - неинтерактивном

```bash
sudo docker/run.sh -r build/aarch64/bin/detectnet build/aarch64/bin/images/peds_0.jpg build/aarch64/bin/images/test/peds_batch_0.jpg
```

## Сборка своего контейнера

Например, свою программу.

## Ссылки

* Официальная документация https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-docker.md
* Система распознавания лиц https://habr.com/ru/company/skillfactory/blog/544430/

