from fastapi import FastAPI

app = FastAPI(
    title="AI Delivery Intelligence System",
    description="Early warning system for project delivery risks",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
