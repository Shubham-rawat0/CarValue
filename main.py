from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema import CarFeatures , PredictionResponse
from model import predict_price, load_artifacts

app=FastAPI(title="Car price prediction")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    load_artifacts()

@app.get("/health")
def test():
    return JSONResponse(status_code=200,content={"success":True,"message":"app running"})

@app.post("/predict")
def predict(features:CarFeatures):
    price= predict_price(features.model_dump())
    return {"prediction": price}
