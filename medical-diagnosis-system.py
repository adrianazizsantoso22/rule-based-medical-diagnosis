# Rule-Based Medical Diagnosis System

from medical_diagnosis_system.diagnosis import diagnosis

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
    symptoms_input = input("Enter the patient's symptoms (comma-separated): ").strip()
    
    # Handle empty input
    if not symptoms_input:
        print("\nNo symptoms entered. Please try again.")
        return
    
    # Process input into a set of symptoms
    symptoms = {symptom.strip().lower() for symptom in symptoms_input.split(",")}
    
    if not symptoms:
        print("\nInvalid input. Please enter at least one symptom.")
        return

    # Perform diagnosis
    results = diagnosis(symptoms)
    
    # Display results
    if results:
        print("\nBased on the symptoms provided, the possible diagnoses are:")
        for diag in results:
            print(f"- {diag}")
    else:
        print("\nNo matching diagnosis found. Please consult a medical professional.")

if __name__ == "__main__":
    main()
