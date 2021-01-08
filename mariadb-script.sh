#!/bin/bash


export MARIA_DB_VERSION="10.5"

docker pull "mariadb:$MARIA_DB_VERSION"
docker run  --rm -d --name thesis-app-mariadb -p 3307:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=thesisAppMariadb "mariadb:$MARIA_DB_VERSION"

