docker network create app_net
docker volume create my-data

docker run -d --net=app_net -p 5432:5432 --name postgresql \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydb \
  -v my-data:/var/lib/postgresql/data \
  postgres:14

docker run -d --net=app_net -p 80:8088 --name superset \
  -e SUPERSET_SECRET_KEY=4546yyvnerij3inrgreeoj5jg0jr0ivj5440v40fjr30fj0fjwr \
  -e SUPERSET_FEATURE_EMBEDDED_SUPERSET=True \
  -e PUBLIC_ROLE_LIKE_GAMMA=True \
  -e ENABLE_IFRAME_EMBED=True \
  -e APP_FEATURE_FLAGS='{"ENABLE_REACT_CRUD_VIEWS": True, "CSV_TO_DATABASE_ALLOWED": True, "EMBEDDED_SUPERSET": True}' \
  -e HTTP_HEADERS='{"X-Frame-Options": "ALLOWALL"}' \
   apache/superset


docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init