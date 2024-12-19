import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.learning_content_generator import LearningContentGenerator
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Educational Content Generator API")

# Add CORS middleware to allow frontend to communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount static files directory to serve generated images
app.mount("/images", StaticFiles(directory="output"), name="images")


class LearningContentRequest(BaseModel):
    topic: str
    learning_style: str = "standard"


class LearningContentResponse(BaseModel):
    explanation: str
    image_path: str


@app.post("/generate-content", response_model=LearningContentResponse)
async def generate_content(request: LearningContentRequest):
    """
    Generate educational content for a given topic and learning style
    """
    try:
        # Generate learning content
        content = LearningContentGenerator.generate_learning_content(
            request.topic,
            learning_style=request.learning_style
        )

        # Convert absolute path to relative path for frontend
        relative_image_path = os.path.basename(content['image_path'])

        return {
            "explanation": content['explanation'],
            "image_path": f"/images/{relative_image_path}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to Educational Content Generator API"}

# Run with: uvicorn main:app --reload