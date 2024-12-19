from services.learning_content_generator import LearningContentGenerator


def main():
    # Example usage
    topics = [
        "Beef and Parotta"
    ]

    learning_styles = ['visual', 'auditory', 'kinesthetic']

    for topic in topics:
        for style in learning_styles:
            print(f"\n--- Learning Content for {topic} (Style: {style}) ---")

            # Generate learning content
            content = LearningContentGenerator.generate_learning_content(
                topic,
                learning_style=style
            )

            print("Explanation:")
            print(content['explanation'])
            print(f"\nEducational Image saved at: {content['image_path']}")


if __name__ == "__main__":
    main()