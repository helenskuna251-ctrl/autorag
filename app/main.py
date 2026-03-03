from fastapi import FastAPI
from app.services.parser import parse_file

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test-parser")
def test_parser():
    # 这里测试读取 README.md
    content = parse_file("README.md")
    return {"length": len(content)}