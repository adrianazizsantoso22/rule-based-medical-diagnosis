# Rule-Based Medical Diagnosis System

from diagnosis import diagnosis

# Knowledge Base: List of rules in the form of (condition, conclusion)
rules = [
    ({"fever", "cough"}, "flu"),
    ({"sore throat", "fever"}, "strep throat"),
    ({"headache", "sensitivity to light"}, "migraine"),
    ({"rash", "fever"}, "chickenpox"),
    ({"shortness of breath", "wheezing"}, "asthma"),
]

def diagnosis(symptoms):
    """Function to diagnose the disease based on symptoms."""
    possible_diagnoses = set()
    
    for rule in rules:
        conditions, conclusion = rule
        if conditions.issubset(symptoms):
            possible_diagnoses.add(conclusion)
    
    return possible_diagnoses

def main():
    """Main function to run the diagnosis system."""
    print("Welcome to the Medical Diagnosis System!")
    symptoms_input = input("Enter the patient's symptoms (comma-separated): ")
    symptoms = {symptom.strip().lower() for symptom in symptoms_input.split(",")}

    results = diagnosis(symptoms)
    
    if results:
        print("Possible diagnoses based on the symptoms provided:")
        for diagnosis in results:
            print(f"- {diagnosis}")
    else:
        print("No possible diagnoses found for the provided symptoms.")

if __name__ == "__main__":
    main()
