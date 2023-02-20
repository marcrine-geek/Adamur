## api endpoints

# POST

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
