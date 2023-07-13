# First time installation

```sh
python -m venv .venv
```

### On Linux

```sh
source ./.venv/bin/activate
```

### On Windows

```sh
.\.venv\Scripts\activate.bat
```

## Install dependencies

```sh
pip install requirements.txt
```

## Run localhost the first time

### On windows

```sh
docker-compose up -d

docker exec -u 0 -it AdventureWorksDashboardSQLServer bash -c "apt-get update && cd /var/opt/mssql/data && wget -O AdventureWorksDW2019.bak https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW2019.bak && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P my_ShittyPassword123 -Q 'CREATE DATABASE AdventureWorksDW2019;RESTORE DATABASE AdventureWorksDW2019 FROM DISK = \"AdventureWorksDW2019.bak\" WITH MOVE \"AdventureWorksDW2019\" TO \"/var/opt/mssql/data/AdventureWorksDW2019.mdf\", MOVE \"AdventureWorksDW2019_log\" TO \"/var/opt/mssql/data/AdventureWorksDW2019_log.ldf\",REPLACE;'"
```

### On linux

```
docker-compose up -d

./restore-db
```

# Run localhost

```sh
# Run
docker-compose up -d

# Stop
docker-compose stop
```

Go to http://localhost:8501/
