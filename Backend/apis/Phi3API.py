import requests


class Phi3API:
    @staticmethod
    def generate_explanation(topic, learning_style, token):
        """
        Generate educational explanation using Phi3 API

        :param topic: Learning topic
        :param learning_style: Preferred learning style
        :param token: Authentication token
        :return: Generated explanation
        """
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        prompt = f"Explain {topic} in a way that suits a {learning_style} learner. Break down complex concepts into simple, understandable parts."

        payload = {
            "inputs": f"<|system|>\nYou are an educational AI assistant that provides clear, adaptive explanations.\n<|end|>\n<|user|>\n{prompt}<|end|>\n<|assistant|>",
            "parameters": {
                "max_new_tokens": 300,
                "temperature": 0.6
            }
        }

        response = requests.post(
            "https://cu-vertical-dimensional-continuity.trycloudflare.com/phi3/generate",
            headers=headers,
            json=payload
        )

        return response.json().get('generated_text', 'Unable to generate explanation')