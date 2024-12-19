from apis.Phi3API import Phi3API
from apis.FluxApi import FLUXAPI
from apis.config import APIConfig


class LearningContentGenerator:
    @classmethod
    def generate_learning_content(cls, topic, learning_style='standard'):
        """
        Generate comprehensive learning content

        :param topic: Learning topic
        :param learning_style: Preferred learning style
        :return: Dictionary with text explanation and image path
        """
        # Generate text explanation
        explanation = Phi3API.generate_explanation(
            topic,
            learning_style,
            APIConfig.PHI3_TOKEN
        )

        # Generate supporting image
        image_path = FLUXAPI.generate_educational_image(
            topic,
            learning_style,
            APIConfig.FLUX_TOKEN
        )

        return {
            'explanation': explanation,
            'image_path': image_path
        }