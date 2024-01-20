from fastapi import FastAPI
from dotenv import load_dotenv
from mypackage.presentation import startups

load_dotenv()

app = FastAPI()
app.include_router(startups.router)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=38080)