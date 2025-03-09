## 🩺 Body Performance Prediction using Random Forest
📌 Overview
This project predicts body performance based on physiological attributes such as age, weight, body fat percentage, and flexibility. The model is built using Random Forest and deployed as an API using FastAPI.

📂 Project Structure
The project consists of a FastAPI backend for predictions, a PostgreSQL database for storing data, and a machine learning model trained using Random Forest. The structure includes directories for API code, data, model training notebooks, and Docker configurations.

🛠️ Setup & Installation
To set up the project, clone the repository, create a virtual environment, install dependencies, and run the FastAPI server. The API is accessible via a local URL, with endpoints for health checks and predictions.

🐳 Running with Docker
The project includes a Docker setup with a FastAPI container and a PostgreSQL database. Using Docker Compose, users can build and run the entire system with a single command. Stopping and removing containers is also supported.

📊 Model Training (Random Forest)
The Random Forest model is trained using body performance data, considering input features such as age, gender, weight, body fat, blood pressure, flexibility, sit-up count, and broad jump distance. The trained model is stored and used for API inference.

🖥️ API Endpoints
The API provides endpoints for checking server health and making predictions. A POST request with body performance attributes returns a prediction of performance level categories (A, B, C, or D).

🛢️ Database (PostgreSQL)
The project uses PostgreSQL for storing body performance data. Users can interact with the database using SQL queries to retrieve stored records.

📜 License
This project is open-source and available under the MIT License.

🤝 Contributing
Contributions are welcome. The process involves forking the repository, creating a new branch, making changes, and submitting a pull request.

📩 Contact
For any questions or suggestions, users can reach out via email or GitHub.

This README provides a structured overview of the project, making it easy for users to understand and set up. Let me know if you need any modifications! 🚀