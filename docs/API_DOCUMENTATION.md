# API Documentation for Medical Diagnosis System

## Overview
This document outlines the API endpoints available for the Medical Diagnosis System. The API allows users to submit symptoms and receive potential diagnoses based on predefined rules. It is designed to assist healthcare professionals and individuals in understanding possible medical conditions based on reported symptoms.

## Base URL
The base URL for all API requests is:

## Endpoints

### 1. POST /diagnose
- **Description**: The ```POST /diagnose``` endpoint allows users to submit a list of symptoms for analysis. Upon receiving the symptoms, the system processes the input and applies its internal rule-based logic to determine potential medical diagnoses. This endpoint is crucial for users seeking guidance on possible health conditions related to their reported symptoms, facilitating timely medical decisions.
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
- **Description**: The ```GET /symptoms``` endpoint retrieves a comprehensive list of recognized symptoms that the medical diagnosis system can process. This resource is valuable for users to understand which symptoms are acknowledged by the system, helping them accurately report their health issues. The endpoint returns a structured response containing all available symptoms in a user-friendly format.
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
- **Description**: The ```GET /diagnoses``` endpoint allows users to query possible diagnoses based on a specified set of symptoms. Users can input a comma-separated list of symptoms, and the system responds with a set of potential medical conditions that align with the provided symptoms. This endpoint enhances user engagement by providing tailored diagnostic information and supporting informed health decisions.
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
- **Description**: The ```POST /feedback``` endpoint enables users to submit feedback regarding the accuracy of the diagnoses they received. By providing information on whether the diagnosis was correct, along with comments, users contribute to the ongoing improvement of the system’s diagnostic capabilities. This feedback mechanism is essential for refining the system's algorithms based on real-world user experiences.
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
- **Description**: The GET /feedback endpoint allows authorized users or administrators to retrieve a collection of feedback submissions from users regarding the system's diagnostic accuracy. This endpoint serves as a valuable tool for analyzing user responses, identifying trends in diagnosis accuracy, and making informed adjustments to the system based on user experiences and suggestions.
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
- **Description**: The ```GET /conditions``` endpoint provides a list of medical conditions that the diagnosis system can identify based on user-reported symptoms. This resource helps users understand the breadth of conditions that can be diagnosed, empowering them with knowledge about potential health issues. The response includes a structured list of conditions that the system recognizes and can diagnose.
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
- **Description**: The ```GET /condition/{name}``` endpoint offers detailed information about a specific medical condition identified by its name. Users can query this endpoint to obtain insights into the symptoms associated with the condition, recommended treatments, and any relevant information that can aid in understanding the condition better. This endpoint is an essential resource for users seeking to learn more about specific health issues.
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
The request for diagnosis example demonstrates how users can interact with the ```POST /diagnose``` endpoint by submitting a JSON payload containing their reported symptoms. This example illustrates the required request format, making it easier for users to understand how to structure their input data when seeking a diagnosis from the system.

To diagnose symptoms, you can use the following cURL command:
```json
curl -X POST http://api.yourdomain.com/diagnose \
-H "Content-Type: application/json" \
-d '{"symptoms": ["fever", "cough"]}'
```

### 2. Example Success Response
The success response example showcases the expected output from the ```POST /diagnose``` endpoint when a user submits valid symptoms. It illustrates the structured JSON response that includes the potential diagnoses identified by the system, providing users with clear and actionable information based on their reported symptoms

When the request is successful, the response will look like this:
```json
{
    "diagnoses": ["flu", "common cold"]
}
```

### 3. Example Error Request
The error request example illustrates a scenario where a user submits invalid symptoms to the ```POST /diagnose``` endpoint. This description highlights how the system responds with an error message, showcasing the importance of input validation and helping users understand what constitutes a valid request.

If you submit an invalid symptom, you might send:
```json
curl -X POST http://api.yourdomain.com/diagnose \
-H "Content-Type: application/json" \
-d '{"symptoms": ["unknown symptom"]}'
```

### 4. Example Request for Symptoms
The request for symptoms example demonstrates how users can utilize the ```GET /symptoms``` endpoint to obtain a list of recognized symptoms. This example highlights the simplicity of the request and sets the stage for users to understand the available symptoms they can report when seeking a diagnosis.

To retrieve the list of symptoms:
```json
curl -X GET http://api.yourdomain.com/symptoms
```

### 5. Example Symptoms Response
The symptoms response example presents the expected output when users successfully query the ```GET /symptoms``` endpoint. It showcases the structured list of symptoms available in the system, allowing users to easily reference and select the symptoms they wish to report for diagnosis.

```json
{
    "symptoms": ["fever", "cough", "sore throat", "headache", "nausea"]
}
```

### 6. Example Request for Feedback
The request for feedback example illustrates how users can submit their feedback regarding the accuracy of the diagnoses they received through the ```POST /feedback``` endpoint. This example provides clarity on the format required for submitting feedback, empowering users to contribute to the improvement of the system's diagnostic accuracy.

To submit feedback:
```json
curl -X POST http://api.yourdomain.com/feedback \
-H "Content-Type: application/json" \
-d '{"diagnosis": "flu", "correct": true, "comments": "The diagnosis was accurate."}'
```

### 7. Example Feedback Response
The feedback response example demonstrates the expected output when a user successfully submits feedback through the ```POST /feedback``` endpoint. It illustrates the confirmation message returned by the system, indicating that the feedback has been received and processed, thus reinforcing the value of user contributions to the system’s evolution.

```json
{
    "message": "Feedback submitted successfully."
}
```

These descriptions provide clarity and context for each endpoint and example, helping users understand their functionalities and interactions with the API. If you need further modifications or additions, feel free to ask!

## Conclusion
This API provides a straightforward interface for diagnosing medical conditions based on symptoms. It aims to assist users in understanding potential health issues efficiently and effectively. For any questions or issues, please contact my email adrianazizsantoso@gmail.com.
