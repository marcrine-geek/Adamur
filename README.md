## flask setup

- install virtual environment
  `pip3 install virtualenv`

- Install flask in the environment
  `python3 -m pip install Flask`

## run the server

`python3 app.py`

## Database initialization

`python3 manage.py db init`

## Migrations

`python3 manage.py db migrate`

## Commit changes to database

`python3 manage.py db upgrade`

## api endpoints

# POST

### tested

`/post/notes`

```json
requires
{
    "notes":string,
}
```

```json
response status 200
{
    "message": "Notes added successfully",
    "status": 200
}
```

# GET

## parameter id

`/get/note`

```json
requires
{
    "id":int,
}
```

```json
response status 200
{
    "data": []
}
```

# GET

## get all notes

### tested

`/get/all/notes`

```json
response status 200
{
    "data": []
}
```

# DELETE

## delete a note

`/delete/notes`

```json
response status 200
{
    "message": "Successfully deleted notes",
}
```
