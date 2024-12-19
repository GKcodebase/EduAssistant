# Educational Content Generator

## Overview
This application generates educational content for various topics, adapting to different learning styles.

## Prerequisites
- Python 3.9+
- Node.js 18+
- npm or yarn

## Backend Setup
1. Clone the repository
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install backend dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables (optional, defaults are in the code)
```bash
export LLAVA_TOKEN=your_token
export PHI3_TOKEN=your_token
export FLUX_TOKEN=your_token
export SDXL_TOKEN=your_token
```

5. Run the FastAPI server
```bash
uvicorn main:app --reload
```

## Frontend Setup
1. Navigate to the frontend directory
```bash
cd frontend
npm install
npm start
```

## Usage
- Access the web application at `http://localhost:3000`
- Select a topic and learning style
- Click "Generate Content" to get an explanation and educational image

## API Endpoints
- `/generate-content` (POST): Generate learning content
  - Request body: `{ "topic": string, "learning_style": string }`
  - Returns: `{ "explanation": string, "image_path": string }`

## Technologies
- Backend: FastAPI, Python
- Frontend: React, Tailwind CSS
- AI APIs: LLaVA, Phi3, FLUX

## Notes
- Ensure you have valid API tokens for the AI services
- Images are temporarily stored in the `output/` directory
