from fastapi import FastAPI

app = FastAPI(title="CRM")

@app.get("/")
def read_root():
    return{"message": "CRM backend is running"}