# python_3.6_mafia
Tender hack top 1

Установка зависимостей: `pip install -e .`

Для запуска контейнеров с поднятым postgresql и superset нужно 
- Установить образы для Postgres и Superset
```shell
    docker pull postgres:14
    docker pull apache/superset
```

- запустить ./superset.sh для создания и поднятия контейнеров \
База данных на 5423 порте, Superset на 8080 port

Для входа в superset ввести admin:admin
Для подключения к superset поднятой бд postgres нужно нажать на settings -> database connections
И указать данные бд (примечание: в host: host.docker.internal)

Для проверки работоспособности postgresql в контейнере можно подключиться к ее интерфейсу:
- `psql -h 127.0.0.1 -p 5432 -U $POSTGRES_USER -d $POSTGRES_DB`
- `docker exec -it $container_id psql -U $POSTGRES_USER -d $POSTGRES_DB` (container id from `docker ps`)
