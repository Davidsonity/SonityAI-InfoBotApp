# ChatBot Project

This project involves the development of a chatbot using text classification, LSTM, and machine learning techniques. The chatbot is designed to provide automated responses to common questions about the project owner. It aims to assist individuals who cannot directly reach the project owner by offering basic information in a convenient and accessible manner.

## Features

- Automated responses: The chatbot utilizes machine learning algorithms and natural language processing techniques to generate automated replies to user questions.
- Dataset generation: A dataset was created by collecting questions from various individuals and categorizing them into different reply categories.
- Training and model accuracy: The dataset was used to train the model, achieving an accuracy of up to 84%.
- Deployment: A Streamlit app was developed for deploying the chatbot and providing a user-friendly interface for interaction.

## Getting Started

### Prerequisites

- Python 3.x
- TensorFlow
- scikit-learn
- pandas
- numpy
- Streamlit

### Installation

1. Clone the repository: `git clone https://github.com/yourusername/chatbot-project.git`
2. Install the required dependencies: `pip install -r requirements.txt`

### Usage

1. Ensure that the dataset file (`updated.csv`) is available in the project directory.
2. Run the data preprocessing and model training script: `python train_model.py`
3. Once the model is trained, start the Streamlit app: `streamlit run app.py`
4. Access the chatbot interface through the provided URL.

## Limitations

- Limited knowledge: The chatbot can only provide responses to questions it has encountered during training. It may not handle unfamiliar or out-of-scope questions effectively.
- Scalability: This project is designed as a showcase and may require additional data, cloud resources, and computational expenses for larger-scale applications.

## Future Enhancements

- Expand the dataset: Collect a larger and more diverse dataset to improve the chatbot's performance and ability to handle a wider range of questions.
- Cloud deployment: Explore cloud-based deployment options to handle increased computational demands and ensure scalability.
- Advanced natural language processing: Implement advanced techniques such as sentiment analysis, entity recognition, or context understanding to enhance the chatbot's capabilities.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project was inspired by the need for a convenient and automated way to provide basic information about the project owner.
- Thanks to the contributors and open-source community for their valuable resources and libraries used in this project.
