from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import shutil
import os

import pickle

from audio_processing import audio

app = FastAPI()

class AudioProcessRequest(BaseModel):
    audio_file: bytes

class AudioProcessResponse(BaseModel):
    prediction: str

@app.post("/api/process_audio")
async def process_audio(audio_file: UploadFile = File(...)):
    try:
        
        with open(audio_file.filename, "wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)

        
        prediction = process_audio_file(audio_file.filename)  
        
        return JSONResponse(content={"prediction": prediction}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

def process_audio_file(filename):
   
    aud=audio()
    df=aud.audio_extraction(filename)
    
    with open("/content/DecisionTree_model.pkl","rb") as file:
        dt_model=pickle.load(file)

    label=dt_model.predict(df)
    
    
    return label[0]




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5173)
