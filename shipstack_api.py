# API endpoints
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from service import calculate_distances
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Models --------------------------------------
class Destinations(BaseModel):
    addresses:list

class Origin(BaseModel):
    location:str

class ClusterRequest():
    desintations:Destinations
    origin_point:Origin

# Endpoints -----------------------------------
@app.post("/uploadAddresses")
def upload_addresses(cluster_req:ClusterRequest):
    # calculate_distances(cluster_req.origin_point,cluster_req.desintations)
    return {cluster_req}