
# Edu Assist: AI-Based Learning Content Generator

Edu Assist is a Python-based project that helps generate educational content using AI. The system provides text explanations and visual content (images) on various learning topics, tailored to different learning styles such as visual, auditory, and kinesthetic. The project integrates with several APIs, including LLava, Phi3, Flux, and SDXL, to generate dynamic and personalized educational materials.

## Project Structure

```
edu_assist/
├── __init__.py
├── main.py
├── apis/
│   ├── __init__.py
│   ├── llava_api.py
│   ├── phi3_api.py
│   ├── flux_api.py
│   └── sdxl_api.py
├── services/
│   ├── __init__.py
│   ├── learning_content_generator.py
│   └── image_processor.py
├── utils/
│   ├── __init__.py
│   └── config.py
└── requirements.txt
```

### Key Components:

- **apis/**: Contains the API interface classes for interacting with LLava, Phi3, Flux, and SDXL APIs.
- **services/**: Implements core functionality such as generating learning content (text explanations and educational images).
- **utils/**: Utility files for configuration and environment setup.
- **main.py**: The entry point of the application, demonstrating how to generate learning content.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/edu_assist.git
   cd edu_assist
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with API tokens. Create a `.env` file in the root directory and add the following variables:
   ```
   LLAVA_TOKEN=your_llava_token
   PHI3_TOKEN=your_phi3_token
   FLUX_TOKEN=your_flux_token
   SDXL_TOKEN=your_sdxl_token
   ```

## Usage

To generate educational content for a set of topics and learning styles, run the following command:

```bash
python main.py
```

The program will generate an explanation and an educational image for each topic and learning style combination, and display the results.

### Example Output:
```
--- Learning Content for Quantum Computing (Style: visual) ---
Explanation:
Quantum computing uses quantum bits (qubits) instead of traditional bits to perform computations. Qubits can represent both 0 and 1 simultaneously, leading to faster computations for certain types of problems.

Educational Image saved at: output/Quantum_Computing_educational_image.png
```

## APIs Used

### LLava API
- **Purpose**: Generate textual responses based on an image and a query.
- **Usage**: Used for generating answers or explanations related to a given image.
- **Endpoint**: `https://supplement-convenient-scores-forgotten.trycloudflare.com/llava/generate`

### Phi3 API
- **Purpose**: Generate educational explanations tailored to different learning styles.
- **Usage**: Used to generate a text-based explanation for a given topic and learning style.
- **Endpoint**: `https://cu-vertical-dimensional-continuity.trycloudflare.com/phi3/generate`

### SDXL API
- **Purpose**: Generate educational images based on a given topic.
- **Usage**: Used to create visual content (images) such as infographics related to educational topics.
- **Endpoint**: `https://singing-shadows-duty-loan.trycloudflare.com/imagine/generate`

## Configuration

API tokens are required to interact with the external services. They are read from a `.env` file located in the project root directory. The `APIConfig` class in `apis/config.py` loads these tokens from the environment variables.

## Development

To contribute to this project:

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/edu_assist.git
   ```
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push your changes and create a pull request.

## Requirements

- Python 3.6+
- The following Python packages are required:
  - `python-dotenv`
  - `requests`
  - `pillow`
  - `fast-api`

These are listed in the `requirements.txt` file.
