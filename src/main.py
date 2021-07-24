from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from predictor import Predictor, Prediction
from config import Settings

app = FastAPI(docs_url="/", title="Parcel Volume Prediction")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()
predictor = Predictor(settings.model_file, settings.tokenizer_file)


@app.get("/predict", response_model=Prediction)
def predict(description: str):
    """
    Predicts the cubic weight of a parcel from its description.
    """
    return predictor.predict(description)
