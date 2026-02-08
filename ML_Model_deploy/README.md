🚀 ML Model Deployment with FastAPI & Docker

This project demonstrates an end-to-end Machine Learning deployment pipeline, covering everything from model training to production-ready API serving and containerization.

It showcases real-world MLOps practices such as model serialization, API-based inference, logging, latency measurement, and Docker-based deployment.

📌 Project Overview

The workflow implemented in this project:

ML Model → FastAPI Service → Docker Container

Train a machine learning model using scikit-learn

Save the trained model as a reusable artifact

Serve the model using a FastAPI REST API

Add health checks, logging, and latency monitoring

Containerize the application using Docker

This setup is designed to be scalable and easily extendable to Kubernetes, GPU inference, and model versioning tools like MLflow.

🧠 Features

✅ Machine learning model training and serialization

✅ REST API for real-time inference

✅ Input validation using Pydantic

✅ Health check endpoint for monitoring

✅ Structured logging and inference latency tracking

✅ Dockerized application for portability and reproducibility

🛠 Tech Stack

Language: Python

Machine Learning: scikit-learn

API Framework: FastAPI

Validation: Pydantic

Server: Uvicorn

Containerization: Docker

📂 Project Structure
.
├── app.py                 # FastAPI application
├── train.py               # ML model training script
├── model.pkl              # Trained ML model
├── logging_config.py      # Logging configuration
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
└── README.md

⚙️ How It Works
1️⃣ Train the Model
python train.py


This generates a trained model saved as model.pkl.

2️⃣ Run the API Locally
uvicorn app:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

3️⃣ Make a Prediction

POST /predict

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}


Response

{
  "prediction": 0,
  "latency": 0.0023
}

4️⃣ Health Check
GET /health


Response:

{
  "status": "ok"
}

🐳 Docker Deployment
Build Image
docker build -t ml-model-api .

Run Container
docker run -p 8000:8000 ml-model-api


Access:

http://localhost:8000/docs

📈 Logging & Monitoring

Logs prediction results and inference latency

Ready for integration with monitoring tools such as Prometheus and Grafana

Health endpoint enables container orchestration readiness checks

🔮 Future Enhancements

🔁 Model versioning with MLflow

☸️ Kubernetes deployment

⚡ GPU-based inference

🔐 Authentication and rate limiting

📊 Advanced monitoring and metrics

👨‍💻 Author

Muhammad Aleem Raza
Machine Learning / MLOps Enthusiast