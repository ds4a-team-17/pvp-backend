from fastapi import FastAPI
from predictor import Predictor, Prediction
from config import Settings


app = FastAPI(docs_url="/", title="Parcel Volume Prediction")
settings = Settings()
predictor = Predictor(settings.model_file, settings.tokenizer_file)


@app.get("/predict", response_model=Prediction)
def predict(description: str):
    """
    Predicts the cubic weight of a parcel from its description.
    """
    return predictor.predict(description)
