# python_3.6_mafia
Tender hack top 1

Установка зависимостей: `pip install -e .`

Работа с postgresql контейнером:
- запуск контейнера в фоновом режиме: `docker-compose up -d`
- подключение к контейнеру:
  - `psql -h 127.0.0.1 -p 5432 -U $POSTGRES_USER -d $POSTGRES_DB`
  - `docker exec -it $container_id psql -U $POSTGRES_USER -d $POSTGRES_DB` (container id from `docker ps`)
- очистить значения добавленные в базу и удалить контейнер:
  - `docker-compose down --volumes`

To run locally upload csv files in statistics/tabels from `https://disk.yandex.ru/d/5_L-WhPOnz4zZw`