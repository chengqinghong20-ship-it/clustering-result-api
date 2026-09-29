from pathlib import Path
import json
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Clustering Result API", version="1.0.0")
BASE_DIR = Path(__file__).resolve().parent
RESULT_FILE = BASE_DIR / "output" / "MBSE_三张输出表.json"

@app.get("/")
def root():
    return {"message": "API is running", "result_api": "/api/clustering/result", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok", "result_file_exists": RESULT_FILE.exists()}

@app.get("/api/clustering/result")
def get_clustering_result():
    if not RESULT_FILE.exists():
        raise HTTPException(status_code=404, detail="Result JSON file not found")
    try:
        with RESULT_FILE.open("r", encoding="utf-8-sig") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON: {e}")
