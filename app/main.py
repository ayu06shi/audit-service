from fastapi import FastAPI

app = FastAPI(title="GxP Audit Trail Service", version="1.0.0", description="Service to manage GxP audit trails.")

@app.get("/health")
def health():
    return {"status": "healthy"}