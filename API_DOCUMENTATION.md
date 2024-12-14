# API Documentation for Medical Diagnosis System

## Overview
This document outlines the API endpoints available for the medical diagnosis system.

## Endpoints

### POST /diagnose
- **Description**: Submit symptoms for diagnosis.
- **Request Body**:
  ```json
  {
      "symptoms": ["fever", "cough"]
  }