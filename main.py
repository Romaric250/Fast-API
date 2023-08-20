from fastapi import FastAPI

fast = FastAPI()


@fast.get("/")
async def root():
    return {"hellow world"}