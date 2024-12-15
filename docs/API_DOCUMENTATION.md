# API Documentation for Medical Diagnosis System

## Overview
This document outlines the API endpoints available for the Medical Diagnosis System. The API allows users to submit symptoms and receive potential diagnoses based on predefined rules. It is designed to assist healthcare professionals and individuals in understanding possible medical conditions based on reported symptoms.

## Base URL
The base URL for all API requests is:

## Endpoints

### 1. POST /diagnose
- **Description**: Submit symptoms for diagnosis.
- **Request Body**:
  ```json
  {
      "symptoms": ["fever", "cough"]
  }
  ```
- **Responses**:
  - **Success (200 OK)**:
  ```json
  {
    "diagnoses": ["flu", "common cold"]
  }
  ```
  - **Error Responses**:
    - **400 Bad Request**: If the request body is malformed contains unrecognized symptoms.
      - **Response Body**:
      ```json
      {
        "error": "Invalid symptom provided."
      }
      ```
    - **422 Unprocessable Entity**: If the symptoms submitted are not sufficient for diagnosis.
      - **Response Body**:
      ```json
      {
        "error": "Insufficient symptoms for diagnosis."
      }

### 2. GET /symptoms
- **Description**: Retrieve a list of recognized symptoms.
- **Response**:
  - **Success (200 OK)**:
  ```json
  {
    "symptoms": ["fever", "cough", "sore throat", "headache", "nausea"]
  }
  ```
  - **Error Responses**:
    - **500 Internal Server Error**: If there is an issue retrieving symptoms.
      - **Response Body**:
      ```json
      {
        "error": "Unable to retrieve symptoms."
      }
      ```

### 3. GET /diagnoses
- **Description**: Retrieve a list of possible diagnoses based on a set of symptoms.
- **Request Parameters** (query):
  - ```symptoms```: A comma-separated list of symptoms (e.g., ```fever,cough```).
- **Response**:
  - **Success (200 OK)**:
  ```json
  {
    "diagnoses": ["flu", "common cold"]
  }
  ```
  - **Error Responses**:
    - **400 Bad Request**: If the symptoms parameter is missing or invalid.
      - **Response Body**:
      ```json
      {
        "error": "Invalid or missing symptoms parameter."
      }
      ```
      
### 4. POST /feedback
- **Description**: Submit feedback about the diagnosis accuracy.
- **Request Parameters** (query):
  ```json
  {
    "diagnosis": "flu",
    "correct": true,
    "comments": "The diagnosis was accurate."
  }
  ```
- **Response**:
  - **Success (201 Created)**:
  ```json
  {
    "message": "Feedback submitted successfully."
  }
  ```
  - **Error Responses**:
    - **400 Bad Request**: If the request body is malformed.
      - **Response Body**:
      ```json
      {
        "error": "Invalid feedback data."
      }
      ```

### 5. GET /feedback
- **Description**: Retrieve feedback on diagnosis accuracy.
- **Response**:
  - **Success (200 OK)**:
  ```json
  {
      "feedback": [
          {
              "diagnosis": "flu",
              "correct": true,
              "comments": "The diagnosis was accurate."
          },
          {
              "diagnosis": "strep throat",
              "correct": false,
              "comments": "The diagnosis was incorrect."
          }
      ]
  }
  ```
  - **Error Responses**:
    - **500 Internal Server Error**: If there is an issue retrieving feedback.
      - **Response Body**:
      ```json
      {
        "error": "Unable to retrieve feedback."
      }
      ```

### 6. GET /conditions
- **Description**: Retrieve a list of medical conditions that can be diagnosed.
- **Response**:
  - **Success (200 OK)**:
  ```json
  {
      "conditions": ["flu", "strep throat", "migraine", "chickenpox", "asthma"]
  }
  ```
  - **Error Responses**:
    - **500 Internal Server Error**: If there is an issue retrieving conditions.
      - **Response Body**:
      ```json
      {
          "error": "Unable to retrieve conditions."
      }
      ```

### 7. GET /condition/{name}
- **Description**: Retrieve details about a specific medical condition.
- **Path Parameters**:
  - ```name```: The name of the condition (e.g., ```flu```).
  - **Success (200 OK)**:
  ```json
  {
      "name": "flu",
      "symptoms": ["fever", "cough", "sore throat"],
      "treatment": "Rest, hydration, and over-the-counter medications."
  }
  ```
  - **Error Responses**:
    - **404 Not Found**: If the condition does not exist.
      - **Response Body**:
      ```json
      {
          "error": "Condition not found."
      }
      ```

## Authentication
- The API does not currently require authentication. Future versions may implement token-based authentication for enhanced security and access control.

## Rate Limiting
- The API allows up to 100 requests per hour per user. Exceeding this limit will result in a ```429 Too Many Requests``` response. Users are encouraged to implement efficient request strategies.

## Examples

### 1. Example Request for Diagnosis
To diagnose symptoms, you can use the following cURL command:
```json
curl -X POST http://api.yourdomain.com/diagnose \
-H "Content-Type: application/json" \
-d '{"symptoms": ["fever", "cough"]}'
```

### 2. Example Success Response
When the request is successful, the response will look like this:
```json
{
    "diagnoses": ["flu", "common cold"]
}
```

### 3. Example Error Request
If you submit an invalid symptom, you might send:
```json
curl -X POST http://api.yourdomain.com/diagnose \
-H "Content-Type: application/json" \
-d '{"symptoms": ["unknown symptom"]}'
```

### 4. Example Request for Symptoms
To retrieve the list of symptoms:
```json
curl -X GET http://api.yourdomain.com/symptoms
```

### 5. Example Symptoms Response
```json
{
    "symptoms": ["fever", "cough", "sore throat", "headache", "nausea"]
}
```

### 6. Example Request for Feedback
To submit feedback:
```json
curl -X POST http://api.yourdomain.com/feedback \
-H "Content-Type: application/json" \
-d '{"diagnosis": "flu", "correct": true, "comments": "The diagnosis was accurate."}'
```

### 7. Example Feedback Response
```json
{
    "message": "Feedback submitted successfully."
}
```

## Conclusion
This API provides a straightforward interface for diagnosing medical conditions based on symptoms. It aims to assist users in understanding potential health issues efficiently and effectively. For any questions or issues, please contact my email adrianazizsantoso@gmail.com.
