# Manga Story and Image Generator

This repository provides a comprehensive tool for generating a manga comic strip from a user-defined prompt. It uses AI-powered APIs for story generation and image creation, then combines these into a polished PDF output. 

## Features
- **Story Generation**: Generate a story outline in a manga format using AI.
- **Image Generation**: Automatically create manga-style illustrations based on scene descriptions.
- **PDF Creation**: Compile the generated images and story into a high-quality manga PDF.
  
## Requirements
- Python 3.7+
- Install the required libraries by running:
  ```bash
  pip install requests Pillow reportlab
  ```

## Setup

### API Tokens
You will need API tokens to access the services for story generation and image generation. Replace the placeholders with your actual API keys:

1. **PHI3_TOKEN**: Token for story generation (text-based API).
2. **FLUX_TOKEN**: Token for image generation (AI image generation API).

Set these tokens in the `main` function of `main.py`:

```python
PHI3_TOKEN = "your_phi3_token_here"
FLUX_TOKEN = "your_flux_token_here"
```

### Fonts
Ensure the manga-style fonts are available in your project directory. These fonts are necessary for generating dialogue and title text with a manga style.

- **Manga Font** (`mangat.ttf`)
- **Dialogue Font** (`Dialogue-A-Light-Italic.ttf`)

Place the fonts in the `/Fonts` directory.

## Usage

To generate a manga, simply run the `main.py` script:

```bash
python main.py
```

### Customize the Prompt

You can modify the `prompt` in the `main` function to generate a manga based on any storyline you wish. Example prompt:

```python
prompt = "In a distant future, two factions clash for control over the galaxy's most coveted resource: Aetherium..."
```

### Output

Once the script runs successfully, it will generate a manga in the form of a PDF, which will be saved in the `manga_output` directory.

## Structure

### `MangaStoryGenerator`
This class handles the story generation using an AI API. It generates a manga story outline based on the provided prompt.

### `MangaImageGenerator`
This class interacts with the Flux API to generate manga-style images based on the generated story scenes. It saves the images in the output directory.

### `MangaPDFGenerator`
This class compiles the generated images and story into a PDF, applying manga-style layouts and formatting.

### `MangaGenerator`
The main class that ties everything together. It generates a story, generates images, and then produces the final PDF.

### Example

```python
from manga_generator import MangaGenerator

# Initialize the manga generator with your tokens
manga_generator = MangaGenerator(PHI3_TOKEN, FLUX_TOKEN)

# Define the prompt for the manga
prompt = "A young warrior embarks on a journey to save the world from an ancient curse..."

# Generate the manga PDF
manga_pdf = manga_generator.generate_manga(prompt)

# Output the generated PDF path
if manga_pdf:
    print(f"Manga PDF generated: {manga_pdf}")
```

### Customization

- **Number of Chapters**: Modify the `max_chapters` parameter to control how many chapters the manga should contain.
- **Scene Descriptions**: You can adjust the generated scene descriptions and tweak the image generation parameters to achieve different visual styles.

## Contributing

Feel free to open issues or pull requests if you'd like to contribute. Any improvements in text processing, image generation, or PDF styling are welcome.

