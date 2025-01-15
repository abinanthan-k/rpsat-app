from fastapi import FastAPI, UploadFile, File, Form
import time
from app.services.parser import extract_text_from_pdf, split_into_chunks
from app.services.chain import split_summaries, prepare_final_summary
from app.services.closest import return_closest_indices
from app.services.translator import translate_text
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.asgi import ASGIApp



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def process_pdf(file: UploadFile = File(...), language:str = Form(...)):
    c = time.time()
    contents = await extract_text_from_pdf(file)
    chunks = split_into_chunks(contents)
    selected_indices = return_closest_indices(chunks)
    summaries = split_summaries(selected_indices, chunks)
    result = prepare_final_summary(summaries)
    result = result["output_text"]
    result = translate_text(result, language)
    result = str(result)
    ans = time.time() - c
    return {"Summary": result, "Done in: ": ans}

# app = ASGIApp(app)
