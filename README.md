# Text Classification API

A machine learning API for text classification that you can use to predict the category a texts belong to.


## Project Structure

```text
text-classification-api/
│
├── app/
    ├── main.py -------------------API route operation file
├── predict.py --------------------Some predictions to test the working of the model/pipeline
├── README.md ---------------------For API documentations
├── requirements.txt --------------Contains packages to be installed
└── train.py ----------------------Contains the code for the model. You need to run this file to train the model
```

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

/path/to/your/project/venv/bin/python
```

Install all the packages in the requirements file
```bash
$ pip install -r requirements.txt
```

Train the model
```bash
$ python3 train.py
```


Start the server
```bash
$ fastapi dev
```


## Running with Docker
```bash
docker build -t text-classification-api .
docker run -p 8000:8000 text-classification-api
```


## API Docs

I advise you use the fastapi swagger ui for a better experience in this case.
Visit the [Swagger UI](http://127.0.0.1:8000/docs)


## Example Request & Response

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


## CI/CD

This project uses GitHub Actions to automatically build and health check the Docker image on every push.
