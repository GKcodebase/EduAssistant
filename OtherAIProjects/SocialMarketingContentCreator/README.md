# Marketing AI Post Generator

This project combines multiple AI-powered APIs to create marketing posts for social media platforms. It analyzes brand assets, generates marketing copy, and creates visuals tailored to the brand’s identity and post objectives. The solution integrates the following functionalities:

- **Brand Asset Analysis:** Extract insights from a brand logo and description.
- **Marketing Copy Generation:** Create compelling marketing text using brand insights.
- **Visual Content Generation:** Generate custom social media visuals based on brand identity and theme.
- **Overlaying Text on Visuals:** Overlay brand insights or other text on generated visuals for final posts.

## Features

- **Brand Analysis**: Analyzes visual and textual elements of brand assets (logo and description) to extract key insights.
- **Marketing Copy Generation**: Automatically creates marketing posts, tailored for different social media platforms (e.g., Instagram, Twitter) using AI.
- **Visual Content Generation**: Generates high-quality, branded visuals that align with the analyzed brand insights and visual themes.
- **Text Overlay on Image**: Adds text (e.g., brand message or insights) onto the generated visuals for final post preparation.

## Requirements

To run this project, you’ll need:
- Python 3.x
- The following Python packages:
  - `requests`
  - `Pillow`
  - `io`
  - `base64`

You can install the dependencies by running:
```bash
pip install requests Pillow
```

## Setup

1. **API Tokens:**
   - You will need valid API tokens for the following services:
     - **LLava API** (for brand asset analysis)
     - **Phi3 API** (for marketing copy generation)
     - **Flux API** (for visual content generation)

2. **Configure Your Tokens:**
   Replace the `PHI3_TOKEN`, `FLUX_TOKEN`, and `LLAVA_TOKEN` in the `main()` function of the code with your actual API tokens.

3. **Run the Program:**
   The `main()` function demonstrates how to use the `MarketingAI` class to generate a complete marketing post. After running the script, it will print the generated marketing copy and display the visual.

## Example Usage

Here’s how you can use the system to create a social media marketing post:

1. **Input:**
   - Brand Name: `Dallas Fried Chicken`
   - Brand Description: `Best Fried Chicken in Texas`
   - Brand Logo Path: `./friedchicken.jpg`
   - Social Media Platform: `Instagram`
   - Post Objective: `Increase brand awareness`
   - Visual Theme: `Cinematic, friendly`

2. **Output:**
   - **Brand Insights**: Extracted visual and textual brand insights from the logo and description.
   - **Marketing Copy**: AI-generated marketing text for social media.
   - **Visual Content**: Generated visual based on brand insights and visual theme.
   - **Final Post**: The visual with overlaid text, ready for sharing.

```python
post = marketing_ai.create_post(
    brand_name="Dallas Fried Chicken",
    brand_description="Best Fried Chicken in Texas",
    brand_logo_path="./friedchicken.jpg", 
    social_media="Instagram",
    post_objective="Increase brand awareness in Instagram",
    visual_theme="Cinematic, friendly"
)
```

The generated post content will be printed, and a final image with the overlaid text will be saved as `marketing_post.png`.

## Code Walkthrough

### 1. **ImageProcessor Class**
   - **`preprocess_image(image_path, max_size)`**: Preprocesses the image to fit a specified size and converts it to a base64 string for API input.
   - **`overlay_text_on_image(image_content, overlay_text)`**: Adds text on top of an image. Used for overlaying brand insights on generated visuals.

### 2. **BrandAnalyzer Class**
   - **`analyze_brand_assets(brand_logo_path, brand_description)`**: Sends the brand logo and description to the LLava API for analysis. The result contains insights about the brand’s identity, tone, and visual characteristics.

### 3. **VisualGenerator Class**
   - **`generate_socialMedia_visual(brand_insights, visual_theme, social_media)`**: Generates high-quality visual content using the Flux API based on brand insights and the requested visual theme (e.g., Cinematic, Friendly).

### 4. **CopyGenerator Class**
   - **`generate_marketing_copy(brand_insights, post_objective, social_media)`**: Generates marketing copy using the Phi3 API, based on the brand insights, post objective, and social media platform.

### 5. **MarketingAI Class**
   - The orchestrator class that combines all the individual components: BrandAnalyzer, CopyGenerator, and VisualGenerator. It creates a full marketing post with insights, copy, and visuals.

### 6. **Main Function**
   - Demonstrates how to use the `MarketingAI` class to generate a marketing post.

## Example Output

After running the script with the provided inputs, the program generates:
1. **Brand Insights** (from logo and description).
2. **Marketing Copy** (generated using Phi3 API).
3. **Generated Visual** (based on the brand insights and visual theme).
4. A final **Image with Overlaid Text** (brand insights or other information).

```text
---------------------------------------------------------------------------------
Marketing Post Generated Successfully!

Brand Insights:
Key visual insights about the brand’s identity and characteristics.

Marketing Copy:
"Hey everyone! 🍗 Discover the best fried chicken in Texas! 😋"

Image with overlaid text saved as "marketing_post.png"
```

## Notes

- **Error Handling**: If any API fails or returns an error, the script will print an error message.
- **Customizing for Different Brands**: You can easily adapt the script for different brands by modifying the `brand_name`, `brand_description`, and other parameters.


## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

---

