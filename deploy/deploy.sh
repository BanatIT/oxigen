cd /root/oxigen_api
git pull
docker-compose -f production.yml build
docker-compose -f production.yml down
docker-compose -f production.yml up -d

