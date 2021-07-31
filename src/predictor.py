import pickle
import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from dataclasses import dataclass

MAX_LENGTH = 300


@dataclass(init=False)
class Prediction:
    probabilities: dict
    predictionCubicWeight: str
    cubicWeightUnit: str
    predictionVolume: str
    volumeUnit: str

    def __init__(self, probabilities: dict, predictionCubicWeight: str, cubicWeightUnit: str, predictionVolume: str, volumeUnit: str):
        self.probabilities = probabilities
        self.predictionCubicWeight = predictionCubicWeight
        self.cubicWeightUnit = cubicWeightUnit
        self.predictionVolume = predictionVolume
        self.volumeUnit = volumeUnit

class Predictor:
    def __init__(self, model_file: str, tokenizer_file: str) -> Prediction:
        self.labels = [0, 300, 500, 750, 1000, 1250, 1500, 2000, 2500, 3000]
        self.model = keras.models.load_model(model_file)

        with open(tokenizer_file, "rb") as handle:
            self.tokenizer = pickle.load(handle)

    def get_label(self, index: int):
        # convert from grams to kg.
        return self.labels[index] / 1000.0

    def predict(self, description: str):
        seq = self.tokenizer.texts_to_sequences([description])
        final_sequence = pad_sequences(seq, maxlen=MAX_LENGTH)

        predictions = self.model.predict(final_sequence)[-1]
        probabilities = {
            self.get_label(i): predition.astype(float)
            for i, predition in enumerate(predictions)
        }
        prediction_label = max(probabilities, key=probabilities.get)

        prediction_volume = (prediction_label * 1000) / (0.166) # converting from cubic weight(kg) to volume(cm3)

        return Prediction(probabilities, prediction_label, "kg", prediction_volume, "cm3")
