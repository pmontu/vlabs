# vlabs

create track
`POST http://127.0.0.1:8001/tracks/ {"name": "Computer Science"}`

view all tracks
`GET http://127.0.0.1:8001/tracks/`
output
```
[
    {
        "id": 1,
        "name": "Computer Science"
    },
    {
        "id": 3,
        "name": "Maths"
    }
]
```

delete track
`DELETE http://127.0.0.1:8001/tracks/1/`

update track
`PATCH http://127.0.0.1:8001/tracks/1 {"name": "Science"}`

create question
`POST http://127.0.0.1:8001/tracks/1/questions/ {"question_text": "Who is the father of Computer Science?"}`

view questions of a track
`GET http://127.0.0.1:8001/tracks/1/questions/`
output
```
[
    {
        "id": 1,
        "question_text": "Who is the father of computer science",
        "pub_date": null,
        "created_date": "2019-03-11T09:05:23.277818Z",
        "track": 1
    }
]
```

create choice
`POST http://127.0.0.1:8001/tracks/1/questions/1/choices/ {"choice_text": "Albert Einstein"}`
`POST http://127.0.0.1:8001/tracks/1/questions/1/choices/ {"choice_text": "Charles Babbage", "correct": true}`

view choices output
```
[
    {
        "id": 1,
        "choice_text": "Albert Einstein",
        "votes": 2,
        "correct": false,
        "question": 1
    },
    {
        "id": 2,
        "choice_text": "Charles Babbage",
        "votes": 1,
        "correct": true,
        "question": 1
    }
]
```

answer
`POST http://127.0.0.1:8001/tracks/1/questions/1/choices/1/votes/`
`POST http://127.0.0.1:8001/tracks/1/questions/1/choices/2/votes/`

view total correct and wrong replies for a question
`GET http://127.0.0.1:8001/tracks/1/questions/1/analysis/`
output
```{
    "right": 1,
    "wrong": 2
}```
