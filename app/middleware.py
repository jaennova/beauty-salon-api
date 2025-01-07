from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    origins = ["*"]  # Permite todos los orígenes

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )