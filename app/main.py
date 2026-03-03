from fastapi import FastAPI

app = FastAPI(title="AutoRAG - 汽车售后知识库")

@app.get("/health")
def health():
    return {"status": "ok"}