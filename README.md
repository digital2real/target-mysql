# target-mysql

:warning: This target is PRE-ALPHA 

It is based on the MeltanoLabs/target-sqlite implementation, with sqlalchemy backend.

This is a [Singer](https://singer.io) target that reads JSON-formatted data
following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md)
and loads them to MYSQL.


## Installation

1. Create and activate a virtualenv
2. `pip install -e '.[dev]'`  


## 

## Configuration of target-sqlite

**config.json**

```json
{
  "database": "test_target_mysql",
  "host":     "127.0.0.1",
  "user": "test_target_mysql",
  "password": "CHANGE_ME"
  "batch_size": "How many records are loaded to SQLite at a time? Default=50",
  "timestamp_column": "Name of the column used for recording the timestamp when Data are loaded to SQLite. Default=__loaded_at"
}
```

## Creating a test Database

```sql
create database test_target_mysql default charset utf8mb4 ;
grant all on test_target_mysql.* to `test_target_mysql`@`127.0.0.1` identified by "CHANGE_ME" ;
```

## Simple test run

If you want to quickly test that your setup is properly configured, you can:

`pytest -vv tests/ --config config.json`


This includes a set of simple tests to check that the connection to SQLite is properly set and that all the required SQLite operations work as expected.

During the tests we create a test tables, populate them with simple data, assert that both the schema and the data loaded are as expected and in the end we destroy them.


## Implementation Notes

see: https://github.com/MeltanoLabs/target-sqlite#user-content-implementation-notes

