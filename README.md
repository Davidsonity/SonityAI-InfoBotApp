# SonityAI
## InfoBot

![chatbot](https://github.com/Davidsonity/SonityAI-InfoBotApp/assets/96771321/1642a2c3-0d80-4c67-bd47-9721548d5b20)


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

## App Deployment

To deploy the InfoBot chat application, follow these steps:

1. Make sure you have the necessary dependencies installed, including TensorFlow, streamlit, numpy, and pickle.
2. Copy the provided code for app deployment and save it to a file named `app.py`.
3. Place the trained model (`model.h5`), tokenizer (`tokenizer.pickle`), label encoder (`label_encoder.pickle`), and rephrase dictionary (`dict_phrases.json`) in the same directory as `app.py`.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the Streamlit app using the command: `streamlit run app.py`.
6. The app will launch in your default web browser, and you can start interacting with the InfoBot chat interface.

Please note that the app requires an active internet connection to load the model and respond to user inputs.

Access the [InfoBot Deployment Site](https://infobot-sonityai.streamlit.app/) to try out the app.

Feel free to ask questions or input your queries to get instant and automated responses from the InfoBot.

## Blog

To learn more about the InfoBot project, read our blog post: [Introducing InfoBot: Your Personal Information Assistant](https://medium.com/@davidsonity/introducing-infobot-your-personal-information-assistant-a9fb8cb7da71)

## Limitations

- Limited knowledge: The chatbot can only provide responses to questions it has encountered during training. It may not handle unfamiliar or out-of-scope questions effectively.
- Scalability: This project is designed as a showcase and may require additional data, cloud resources, and computational expenses for larger-scale applications.

## Future Enhancements

- Expand the dataset: Collect a larger and more diverse dataset to improve the chatbot's performance and ability to handle a wider range of questions.
- Cloud deployment: Explore cloud-based deployment options to handle increased computational demands and ensure scalability.
- Advanced natural language processing: Implement advanced techniques such as sentiment analysis, entity recognition, or context understanding to enhance the chatbot's capabilities.

## License

This project is licensed under the [GNU Affero General Public License](LICENSE).

The AGPL license requires anyone who uses the software over a network or as a service to make the source code available to the users interacting with that software. This license ensures that modifications and improvements made to the project are also shared with the community.

## Acknowledgments

- The project was inspired by the need for a convenient and automated way to provide basic information about the project owner.
- Thanks to the contributors and open-source community for their valuable resources and libraries used in this project.
