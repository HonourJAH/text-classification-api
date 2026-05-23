from pydantic import BaseModel, Field
from fastapi import FastAPI
import joblib

app = FastAPI()


class TextInput(BaseModel):
    text: str = Field(
        min_length=10,
        description="The text to classify must be at least 10 characters long.",
    )


data = joblib.load("model.joblib")
pipeline = data["pipeline"]
categories = data["categories"]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(input: TextInput):
    result = pipeline.predict([input.text])
    predicted_category = categories[result[0]]
    return {"predicted_category": predicted_category}
