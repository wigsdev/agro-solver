from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Agro-Solver API",
    description="Backend API for Agro-Solver platform",
    version="0.1.0"
)

# TODO: SEGURIDAD - Restringir orígenes antes de producción
# Actualmente se permite '*' para facilitar el desarrollo local.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Root endpoint to verify API availability.
    """
    return {"message": "Agro-Solver API is running", "version": "0.1.0"}
