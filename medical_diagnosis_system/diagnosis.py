# medical_diagnosis_system/diagnosis.py

def diagnosis(symptoms):
    """
    Function to diagnose the disease based on symptoms.
    
    Args:
        symptoms (set): A set of symptoms provided by the user.
    
    Returns:
        set: A set of diagnoses matching the symptoms.
    """
    rules = [
        ({"fever", "cough"}, "flu"),
        ({"sore throat", "fever"}, "strep throat"),
        ({"headache", "sensitivity to light"}, "migraine"),
        ({"rash", "fever"}, "chickenpox"),
        ({"shortness of breath", "wheezing"}, "asthma"),
    ]
    
    possible_diagnoses = set()
    
    for conditions, conclusion in rules:
        if conditions.issubset(symptoms):
            possible_diagnoses.add(conclusion)
    
    return possible_diagnoses
