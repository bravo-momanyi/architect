from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import uvicorn
from model_utils import generate_image_from_sketch, vectorize_sketch, answer_question
import tempfile
import os

app = FastAPI()

@app.post("/generate")
async def generate(prompt: str = Form(...), file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    output_path = generate_image_from_sketch(tmp_path, prompt)
    return FileResponse(output_path)

@app.post("/vectorize")
async def vectorize(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    svg_path = vectorize_sketch(tmp_path)
    return FileResponse(svg_path, media_type="image/svg+xml")

@app.post("/qa")
async def qa(question: str = Form(...)):
    answer = answer_question(question)
    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
