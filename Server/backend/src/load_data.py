from pathlib import Path
import joblib
import tensorflow as tf

BASE_DIR=Path(__file__).resolve().parent.parent
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
