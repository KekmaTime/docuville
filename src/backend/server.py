from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import tempfile
from main import process_image
from ocr.reader import initialize_reader

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
reader = initialize_reader()

@app.post("/api/process-document")
async def process_document(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)
        results = process_image(tmp_path, reader)
        tmp_path.unlink()
        
        names = [name["name"] for name in results["names"]]
        
        return {
            "success": True,
            "data": {
                "names": names,
                "passport_number": results["passport_number"],
                "expiry_date": results["expiry_date"]
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
