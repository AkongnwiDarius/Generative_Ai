
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Loading the sentiment pretrained model from hugginface 
sentiment_model = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

# Getting info from the user
@app.get("/sentiment/{text}")
def analyze_sentiment(text: str):

    if text.strip() == "":
        return {"data": "No text provided"}

    else:
        # Perform sentiment analysis on the text
        result = sentiment_model(text)[0]

        return {
            "Text": text,
            "Sentiment": result["label"]
        }
