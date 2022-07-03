#!/bin/bash
cd backend/data-integration
./build.sh
cd ../..
cd frontend/thdl
./build.sh
cd ../..
docker-compose up -d
until curl -X GET -s -f -o /dev/null "localhost:9200"
do
  sleep 5
done
cd convert-data-es/
./build.sh