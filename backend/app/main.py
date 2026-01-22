from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.fridge import router as fridge_router

app = FastAPI(title="AI Fridge Chef")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fridge_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok"}
