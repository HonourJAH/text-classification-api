# Text Classification API

A machine learning API for text classification that you can use to predict the category a texts belong to.


## Installation Guide

Clone the repo
```bash
$ git clone git@github.com:HonourJAH/text-classification-api.git
```

Navigate to the text-classification-api directory/folder
```bash
$ cd text-classification-api
```

Create virtual environment in the project directory and activate it
```bash
$ python3 -m venv venv

$ source venv/bin/activate
```

Check if the virtual environment is active
```bash
$ which python

/home/user/code/awesome-project/.venv/bin/python
```

Install all the packages in the requirements file
```bash
$ pip install -r requirements.txt
```

Start the server
```bash
$ fastapi dev
```

## API Docs

I advise you use the fastapi swagger ui for a better experience in this case.
Visit the [Swagger UI](http://127.0.0.1:8000/docs)


## Example request respons

Request:
```json
{
  "text": "Christians and Muslims share many common values and traditions in their worship"
}
```

Response:
```JSON
{
  "predicted_category": "talk.religion.misc"
}
```
