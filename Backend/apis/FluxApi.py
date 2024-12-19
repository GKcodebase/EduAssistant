import requests
import os


class FLUXAPI:
    @staticmethod
    def generate_educational_image(topic,style, token, img_size=1024):
        """
        Generate an educational image using SDXL-Lightning API

        :param topic: Topic for image generation
        :param token: Authentication token
        :param img_size: Size of the image
        :return: Path to the generated image
        """
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = {
            "prompt": f"Educational infographic about {topic}, clean design,{style} informative illustration, academic style",
            "img_size": img_size,
            "guidance_scale": 7.5,
            "num_inference_steps": 50
        }

        response = requests.post(
            "https://maintained-thai-filter-four.trycloudflare.com/imagine/generate",
            headers=headers,
            json=payload
        )

        # Create output directory if it doesn't exist
        os.makedirs('output', exist_ok=True)

        # Save the image
        output_path = f'output/{topic.replace(" ", "_")}{style.replace(" ", "_")}_educational_image.png'

        with open(output_path, 'wb') as f:
            f.write(response.content)

        return output_path