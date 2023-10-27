from fastapi import FastAPI
from core.routes import router as core_routes
from authentication.routes import routes as authentication_routes

app = FastAPI()
app.include_router(router=core_routes, prefix="")
app.include_router(router=authentication_routes, prefix="")


@app.get("/api/library")
def root():
    return {"message": "Welcome to FastAPI with Pymongo"}
