# muratdemiralay222
	Choice of Model:

	Chose Naive Bayes for its performance with CountVectorizer, giving the best F1 macro metric during trials.
	Due to different classes, prioritized F1 macro over accuracy to account for varying label proportions.

	Data Stratification:

	Key strategy: stratified dataset split during both initial data split and within grid search.
	Ensured proportional representation of different classes in the training and validation sets.

	Sentence Length Considerations:

	Opted for longer sentences due to the limited impact of CountVectorizer on longer text.
	Noted that more sophisticated models (LSTM, BERT) might require attention to padding and potential training time issues for longer sentences.

	Model Serialization:

	Saved the best model in pickle form after completing the modeling phase.

	FastAPI Development:

	Chose FastAPI for building the web service.
	Implemented a versioned API.
	Incorporated HTTPException in the predict pipeline to handle cases where certain rows were eliminated during training (e.g., full blanks, @hotmail URLs).

	API Endpoints:

	Created a health check for the main endpoint.
	Implemented the predict pipeline function for the prediction endpoint.

	Dockerization:

	Used a Python 3.9 image for Docker.
	Utilized the requirements.txt file in the run command.
	Copied the local app directory to /app/ in the Docker image to include the application's source code.

	Docker Image Building and Running:

	Built the Docker image using the command docker build -t visable_app .
	Ran the Docker image with docker run -p 80:80 visable_app.
For the /docs endpoint I can use predict method.


https://private-user-images.githubusercontent.com/55508480/300470507-b29c4da7-7dfc-419a-a227-2f37df032df9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY1MzQ1MTcsIm5iZiI6MTcwNjUzNDIxNywicGF0aCI6Ii81NTUwODQ4MC8zMDA0NzA1MDctYjI5YzRkYTctN2RmYy00MTlhLWEyMjctMmYzN2RmMDMyZGY5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTI5VDEzMTY1N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNkYzUxNzhiZTAyMjI5NzUwZTZmOTAzNDMwNDdhOGUyOWMzMWVmNzM1MWM5MTZiZWIzYTA4NDliODkwYTJiMTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Im3WxdW9fF3iTZNNmn92T8c-f-mU8pZkmduiBq0naX0
