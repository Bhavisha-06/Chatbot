# QnA-App

A Question Answering application using PyQt5 for the frontend and a Flask server for the backend, powered by a pre-trained transformer model. This project allows users to input a question and context to receive answers from the model.

## Features

- Input a question and context to get answers from the model.
- Simple and intuitive UI using PyQt5.
- Backend server to handle model inference using Flask.

## Requirements

- Python 3.6 or higher
- PyQt5
- Requests
- Transformers (Hugging Face)
- Flask
- PyTorch (or TensorFlow, depending on the model)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/QnA-App.git
    cd QnA-App
    ```

2. **Install the required libraries**:
    ```bash
    pip install pyqt5 requests transformers flask torch
    ```

3. **Ensure your pre-trained model files are placed in the correct directory** (e.g., `models`).

## Usage

1. **Start the backend server**:
    ```bash
    python app.py
    ```

2. **In a new terminal, run the PyQt5 application**:
    ```bash
    python qa_app.py
    ```

3. **Use the UI** to input a question and context, then click "Get Answer" to see the response.

## Example Questions and Contexts

### Example 1: General Knowledge Question

**Context**:
France is a beautiful city with Paris as its capital.
**Question**:
What is the capital of France?
**Response**:
Paris

### Example 2: Scientific Question

**Context**:
Artificial intelligence (Al) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. These intelligent systems can perform tasks such as speech recognition, decision-making, and language translation. Al is divided into two types: narrow Al, which is designed for specific tasks, and general Al, which can perform any intellectual task that a human can do.
**Question**:
What are the two types of artificial intelligence?
**Response**:
narrow ai, which is designed for specific tasks, and general ai


## Fine-Tuning and Training

For fine-tuning the model and additional training, refer to the following resources:

- [Intel Repository for Fine-Tuning](https://github.com/intel/intel-extension-for-transformers/blob/main/intel_extension_for_transformers/neural_chat/docs/notebooks/build_chatbot_on_spr.ipynb): This notebook provides detailed instructions on how to fine-tune a transformer model using Intel's extensions.

- **build_Chatbot Book**: This notebook was made by me as a part of the project-Fine-tune an LLM model to create a custom chatbot.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.

