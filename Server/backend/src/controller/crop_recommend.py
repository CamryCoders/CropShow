from flask import Flask,request,jsonify
from pathlib import Path
import tensorflow as tf
import joblib
import numpy as np

BASE_DIR=Path(__file__).resolve().parent.parent.parent
print("Base_dir",BASE_DIR)
MODEL_PATH = BASE_DIR / "models" / "crop_model.keras"

print("Path:", MODEL_PATH)
print("Exists:", MODEL_PATH.exists())
print("Size:", MODEL_PATH.stat().st_size, "bytes")

model = tf.keras.models.load_model(
    BASE_DIR/"models"/"crop_model.keras"
)
scaler = joblib.load(
    BASE_DIR/"models"/"scaler.pkl"
)

label_encoder = joblib.load(
    BASE_DIR/"models"/"label_encoder.pkl"
)

def cropRecommend():
    data=request.get_json()

    input_data=np.array([
        [data.get("N"),
         data.get("P"),
         data.get("K"),
         data.get("temperature"),
         data.get("humidity"),
         data.get("ph"),
         data.get("rainfall"),]
    ])

    input_scaled=scaler.transform(input_data,)
    probabilities = model.predict(input_scaled, verbose=0)[0]
    predicted_index = np.argmax(probabilities)
    crop = label_encoder.inverse_transform(
        [predicted_index]
    )[0]

    confidence = probabilities[predicted_index] * 100

    print("Recommended Crop:", crop)
    print("Confidence:", round(confidence, 2), "%")



    return crop,confidence