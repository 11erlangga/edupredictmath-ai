# from contextlib import asynccontextmanager

# import tensorflow as tf
from fastapi import FastAPI

from routers import predict

app = FastAPI()

app.include_router(predict.router)


@app.get("/")
def root():
    return {"message": "AI Service is running"}


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     try:
#         ml_model["dkt"] = tf.saved_model.load("./saved_model/dkt")
#     except Exception as e:
#         print(f"Gagal load model: {e}")
#         # server tetap jalan tapi prediksi tidak tersedia
#     yield
#     ml_model.clear()
