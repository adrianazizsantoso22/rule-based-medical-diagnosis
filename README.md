# Rule-Based Medical Diagnosis System

## Overview
This GitHub repository contains a simple rule-based medical diagnosis system that assists healthcare professionals in diagnosing common diseases based on reported symptoms. The system uses a set of if-then rules to infer possible conditions, providing a user-friendly command-line interface for input and output.

This GitHub is made by:
- Adrian Aziz Santoso (NRP 5025221229)
- Andreas Reynard Samsico (NRP 5025221020)
- Cavel Ferrari (NRP 5025211198)
- Marco Marcello Hugo (NRP 5025221102)
- Schaquille Devlin Aristanto (NRP 5025211211)

to fulfill the assignment for Knowledge-Based System Engineering - class C

## Features
- Rule-based inference engine
- Supports multiple rules for diagnosing various conditions
- User-friendly command-line interface

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adrianazizsantoso22/rule-based-medical-diagnosis-system
   ```
2. Navigate into the project directory:
   ```bash
   cd medical-diagnosis-system
   ```
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   Activate it:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the medical diagnosis system, execute the following command:
```bash
python medical-diagnosis-system.py
```
Follow the prompts to input symptoms. The system will return possible diagnoses based on the provided symptoms.

### Examples
- Input: `fever, cough`
- Output: Possible diagnoses: `flu`
  
- Input: `sore throat, fever`
- Output: Possible diagnoses: `strep throat`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact:
- Adrian Aziz Santoso: adrianazizsantoso@gmail.com
