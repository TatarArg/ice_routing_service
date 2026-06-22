# Ice Routing Service
Сервис моделирования и оптимизации маршрутов судов с учётом ледовой обстановки.

> **Внимание:** `git clone` может занять продолжительное время(5-10 минут), т.к вместе с репозиторием подгружается база данных SQLite с AIS-данными.

## Запуск через Docker
```bash
git clone https://github.com/TatarArg/ice_routing_service
cd ice_routing_service
docker compose up --build
```
Открыть в браузере: http://localhost:8000

## Запуск без Docker
```bash
git clone https://github.com/TatarArg/ice_routing_service
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```
Открыть в браузере: http://localhost:8000

## Быстрый старт

1. Выберите акваторию **Тест** из списка. (см. скриншот ниже).
2. Нажмите чекбокс "Показать курсы судов" в левой панели снизу.
3. Установите начальную и конечную точки маршрута на карте (см. скриншот ниже).
4. Выберите тип судна и нажмите **Построить маршрут**.

![Выбор акватории](https://private-user-images.githubusercontent.com/159607587/611284621-a241ae6d-da35-4671-892e-2e2836ba7796.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODIxNDIxNDksIm5iZiI6MTc4MjE0MTg0OSwicGF0aCI6Ii8xNTk2MDc1ODcvNjExMjg0NjIxLWEyNDFhZTZkLWRhMzUtNDY3MS04OTJlLTJlMjgzNmJhNzc5Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYyMlQxNTI0MDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MDE5ZTIxMmJiYjg3ZTU2ZTA5MjUyYzgxMDU4ZTc5Y2I2YWYwY2QxYjQ4NTdiMjdlMjU4NzUyNGIzYmFmMmViJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.1f9Bz68iaERhz7nxWS5xt5uT6QwVpV1Jk_LL3rEG7kA)

![Выбор точек маршрута](https://private-user-images.githubusercontent.com/159607587/611288563-7aaa4983-88b9-40a6-9df3-51f1dda6d86f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODIxNDIzMDEsIm5iZiI6MTc4MjE0MjAwMSwicGF0aCI6Ii8xNTk2MDc1ODcvNjExMjg4NTYzLTdhYWE0OTgzLTg4YjktNDBhNi05ZGYzLTUxZjFkZGE2ZDg2Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYyMlQxNTI2NDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kN2U1ZDRlYjZjMjM5ODBiOTRhMGE1NjZjNmRkMDU2NjA1ZjRlM2ViZDk5OWEyMmY2NWIzMWRjMmRiNmUwODc3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.O3Sfex1k7z1ekqmtYTlJXEmReZFuU5Kx3LmrSiLuhMU)

Примечание: маршрут не всегда строится с изгибами - это зависит от расположения точек. Для наглядного результата рекомендуется выбирать точки как на скриншоте или добавить ледовую обстановку поперек маршруту: алгоритм проложит маршрут в обход ледовых зон.
