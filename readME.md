# setup/Teardown

## 1. build

`docker-compose up --build`

- mongodb goes through a health check before docker starts the fastAPI container.
- once fastAPI starts, it initiates a db init function which will:

    1. create the collections, while applying the the json schema validators.
    2. parse csv's from old DBMS.
    3. run aggregates on the collections to finalize db migration to `MongoDB`
    4. Once done, it will create an empty txt file as a flag to indicate that we no longer need to setup the db (if we relaunch the app)


## 2. Restarting

`docker-compose up`

Resetting the database requires a few sets.

1. delete `db/data` folder - this will reset persisted database info
2. delete `config/processed`
3. launch containers

## 3. tear down

`docker-compose down`


# Structure
```
-- app
|   |-- __init__.py
|   |-- config
|   |-- controllers
|   |-- dockerfile
|   |-- main.py
|   |-- models
|   |-- requirements.txt
|   |-- routes
|   |-- schemas
|   |-- tests
|   `-- utils
|-- db
|   |-- Dockerfile
|   |-- config
|   `-- data
|-- db_schema.json
|-- docker-compose.yml
`-- readME.md
```
## App
### config
- aggregate pipelines
- csv's from old database 
- Database singleton

### controllers
- the three basic controllers `student`, `teacher`, `class`

### models
- json schema validtors for each of our tables

```
-- models
|   |-- class_.py
|   |-- grade.py
|   |-- schema.py
|   |-- student.py
|   |-- subject.py
|   |-- teacher.py
|   `-- trimester.py
```
### routes

Basic crud for:
1. `student`
2. `teacher`
3. `class`

### schemas
- pydantic models for our mongoDb documents

### tests
- tests for `student`, `teacher` & `class`

### utils

- csv module
- types for `ObjectId` serialization
- `common.py` for common variables shared across the application  


## DB

- `Dockerfile` for configuration
- `data` for docker volume