from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from presentation.routers import audio



app = FastAPI(title="API", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=audio.router)

# import uvicorn
# uvicorn.run(app=app, host="0.0.0.0", port=8000)