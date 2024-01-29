import pickle
import re
from pathlib import Path
from fastapi import HTTPException, status


__version__ = "0.1"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/murat_grid-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


def predict_pipeline(text):

    if not text.strip() or text == "吉祥" or "@" in text or re.match(r'^\d+$', text):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Please input proper text")

    text = text.lower()
    pred = model.predict([text])
    return pred[0]