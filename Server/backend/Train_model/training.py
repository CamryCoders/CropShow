import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

import tensorflow as tf
from keras import Sequential
from keras.layers import Dense, Input


df = pd.read_csv(
    "Crop_recommendation.csv"
)
X = df[
    [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
]

y = df["label"]


label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)
model = Sequential([
    Input(shape=(7,)),
    Dense(
        128,
        activation="relu"

    ),
    Dense(
        64,
        activation="relu"

    ),
    Dense(
        32,
        activation="relu"
    ),

    Dense(
        len(label_encoder.classes_),
        activation="softmax"
    )

])


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train_scaled,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2
)
test_loss, test_accuracy = model.evaluate(
    X_test_scaled,
    y_test
)

print(
    "Test Accuracy:",
    test_accuracy
)
os.makedirs(
    "../models",
    exist_ok=True
)
model_path=os.path.abspath(
    "../models/crop_model.keras"
)
scaler_path=os.path.abspath(
    "../models/scaler.pkl"
)
label_path=os.path.abspath(
"../models/label_encoder.pkl"
)
print(model_path)
print(scaler_path)
print(label_path)


model.save(
    model_path
)
joblib.dump(
    scaler,
    scaler_path
)

joblib.dump(
    label_encoder,
    label_path
    
)
print(
    "Model, scaler and label encoder saved successfully."
)