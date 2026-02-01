from pathlib import Path
import pandas as pd
import joblib

CAR_PRICE_API_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = CAR_PRICE_API_DIR / "models/random_forest_model.pkl"
COLS_PATH = CAR_PRICE_API_DIR / "models/feature_columns.pkl"
print(COLS_PATH)
_model = None
_feature_columns = None

def load_artifacts():
    global _model, _feature_columns
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)

def preprocess(payload: dict) -> pd.DataFrame:
    """
    Converts raw input into the SAME one-hot encoded column structure used in training.
    """
    df = pd.DataFrame([payload])

    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    for col in _feature_columns: # type: ignore
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[_feature_columns]

    return df_encoded # type: ignore


def predict_price(payload: dict) -> float:
    load_artifacts()
    X = preprocess(payload)
    pred = _model.predict(X)[0] # type: ignore
    return float(pred)
