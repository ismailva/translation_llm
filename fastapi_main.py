import logging
from pydantic import BaseModel
from fastapi import FastAPI, status
import uvicorn
from src import constants
from src.translation import TranslationService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class TranslationInput(BaseModel):
    targetlang : constants.SUPPORTED_LANG
    english_text : str

app = FastAPI()
ts = TranslationService()

@app.get('/health', status_code=status.HTTP_200_OK)
async def perform_healthcheck():
    return {"health":"good!"}

@app.get("/translate")
@app.post("/translate")
async def translate(input:TranslationInput):
    res=ts.translate(input.targetlang,input.english_text)
    return {"translated_text": res}

if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="0.0.0.0", port=8080)
