from fastapi import FastAPI

app = FastAPI(
    title="Personal statistics"
)


@app.get("/")
def main_page():
    return "hello world"
