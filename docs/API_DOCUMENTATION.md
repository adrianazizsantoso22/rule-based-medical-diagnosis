# API Documentation for Medical Diagnosis System

## Overview
This document outlines the API endpoints available for the Medical Diagnosis System. The API allows users to submit symptoms and receive potential diagnoses based on predefined rules. It is designed to assist healthcare professionals and individuals in understanding possible medical conditions based on reported symptoms.

## Base URL
The base URL for all API requests is:

## Endpoints

### POST /diagnose
- **Description**: Submit symptoms for diagnosis.
- **Request Body**:
  ```json
  {
      "symptoms": ["fever", "cough"]
  }
