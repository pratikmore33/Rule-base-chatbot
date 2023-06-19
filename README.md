# Rule-base Chatbot

This repository contains code for a simple rule-based chatbot that extracts answers using regex patterns. The chatbot is designed to work with Korean text inputs and includes a Dockerfile and an API created with FastAPI.

## Workflow

The code follows a straightforward workflow:

1. The chatbot receives a Korean text input as a question. These questions are typically static and fall under the category of Frequently Asked Questions (FAQs).

2. The text input is sent to the chatbot via the API.

3. The chatbot uses regex patterns to search for matching patterns in the question.

4. If a pattern match is found, the chatbot returns the corresponding answer for the question via the API.

This workflow allows users to interact with the chatbot by sending questions and receiving answers through the API. 

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Make sure you have Docker installed on your system.
3. Build the Docker image using the provided Dockerfile.
4. Run the Docker container with the appropriate configuration.
5. Use the API by sending Korean text inputs as questions and receiving answers.

The API is hosted on `0.0.0.0` and uses port `8000` by default. You can modify the host and port configurations as needed.

Please refer to the code in this repository for further implementation details.

## Contributors

This project was developed by [Your Name]. Contributions to the project are welcome. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for personal or commercial purposes.

## Acknowledgments

We would like to acknowledge the use of FastAPI and the regex pattern matching technique, which have been instrumental in the development of this rule-based chatbot.
