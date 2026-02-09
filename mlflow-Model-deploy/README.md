A production-ready machine learning model deployment pipeline using FastAPI for serving and MLflow for model management. This project demonstrates how to containerize and deploy a digit classification model with monitoring, health checks, and batch prediction support.

🚀 Features
FastAPI REST API with Swagger/OpenAPI documentation

MLflow Model Registry for versioning and staging

Docker Containerization for easy deployment

Production-ready endpoints with health checks

Batch prediction support

Model monitoring and latency tracking

Automatic model loading from MLflow registry

📁 Project Structure
text
mlflow-deployment/
├── app/
│   ├── main.py              # FastAPI application
│   ├── model_loader.py      # MLflow model loading logic
│   └── config.py            # Configuration settings
├── Dockerfile               # Container configuration
├── requirements.txt         # Python dependencies
├── model_training.py        # Training and registering model
└── README.md               # This file
🛠️ Quick Start
Prerequisites
Python 3.9+

Docker (optional)

MLflow tracking server

1. Install Dependencies
bash
pip install -r requirements.txt
2. Start MLflow Tracking Server
bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlartifacts \
    --host 0.0.0.0 \
    --port 5000
3. Train and Register Model
bash
python model_training.py
4. Start FastAPI Server
bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
5. Build Docker Image
bash
docker build -t ml-model-api .
docker run -p 8000:8000 ml-model-api
🌐 API Endpoints
Method	Endpoint	Description
GET	/health	Health check
GET	/model-info	Model metadata
POST	/predict	Single prediction
POST	/predict/batch	Batch predictions
Example Request
bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "features": [0.0, 0.0, 5.0, 13.0, 9.0, 1.0, 0.0, 0.0, ...]
  }'
Example Response
json
{
  "prediction": 0,
  "probabilities": [0.95, 0.01, 0.01, ...],
  "latency": 0.0032,
  "model_stage": "Production"
}
🐳 Docker Deployment
Build and Run
bash
# Build image
docker build -t digit-classifier-api .

# Run container
docker run -p 8000:8000 digit-classifier-api

# With environment variables
docker run -p 8000:8000 \
  -e MLFLOW_TRACKING_URI="http://localhost:5000" \
  digit-classifier-api
Docker Compose (Full Stack)
bash
docker-compose up -d
📊 Model Registry with MLflow
Register Model
python
mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="model",
    registered_model_name="DigitsClassifier"
)
Promote to Production
python
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="DigitsClassifier",
    version=1,
    stage="Production"
)
🧪 Testing
Interactive Testing
Open browser to: http://localhost:8000/docs

Automated Tests
bash
# Run test script
python test_predictions.py

# Test with curl
curl http://localhost:8000/health
📈 Monitoring
Latency tracking on every prediction

Health endpoints for Kubernetes/Docker

Model version tracking through MLflow

Error rate monitoring

🔧 Configuration
Environment variables:

bash
MLFLOW_TRACKING_URI=http://localhost:5000
MODEL_NAME=DigitsClassifier
MODEL_STAGE=Production
🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open Pull Request