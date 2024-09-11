# Image Classification with MobileNetV2 and FastAPI

This project is an image classification API built using the **MobileNetV2** model and **FastAPI**. The API accepts an image input and returns the predicted class along with the confidence score. It is deployed on Heroku.

## Live API

You can access the API documentation and interact with the model via Swagger UI here:  
[https://image-classification-5d9550a8d37f.herokuapp.com/docs](https://image-classification-5d9550a8d37f.herokuapp.com/docs)

## Features

- **Model**: MobileNetV2 for image classification
- **Framework**: FastAPI for API routing
- **Deployment**: Hosted on Heroku
- **Input**: Accepts images via a POST request
- **Output**: Returns the predicted class and confidence score

## Endpoints

### `POST /predict/`

#### Request:

- **URL**: `/predict/`
- **Method**: POST
- **Content Type**: `multipart/form-data`
- **Body Parameters**:
  - `image`: An image file (JPEG, PNG, etc.)

#### Example using `curl`:

```bash
curl -X 'POST' \
  'https://image-classification-5d9550a8d37f.herokuapp.com/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@/path_to_image/image.jpg'
```

#### Response:

```json
{
  "predicted_class": "class_name",
  "confidence": 0.8145
}
```

- **predicted_class**: The label of the predicted class.
- **confidence**: The model’s confidence in the prediction.

## Setup and Installation

### Requirements

- Python 3.8+
- TensorFlow
- FastAPI
- Uvicorn

### Steps to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/dev-achintha/Image-Classification-with-Fast-API.git
   cd Image-Classification-with-Fast-API
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:

   ```bash
   uvicorn app:app --reload
   ```

4. Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the API documentation.

## Deployment

The application is deployed on Heroku. You can use the `Procfile` and `requirements.txt` for deploying your own FastAPI applications.