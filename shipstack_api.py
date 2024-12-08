# API endpoints
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from service import get_clusters
import uvicorn
import json

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Models --------------------------------------
class ClusterRequest(BaseModel):
    desintations:str
    origin_point:str

# Endpoints -----------------------------------
@app.get("/")
def root():
    pass

@app.post("/uploadAddr")
def upload_addresses(cluster_req:dict):
    dests= cluster_req["destinations"].split("|")
    clusters = get_clusters(cluster_req["origin"],dests)
    
    json_clusters= json.dumps(clusters)
    print(json_clusters) 
    return json_clusters