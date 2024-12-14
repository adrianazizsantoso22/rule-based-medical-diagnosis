def diagnosis(symptoms):
    diagnoses = set()

    if {"fever", "cough"}.issubset(symptoms):
        diagnoses.add("flu")
    if {"sore throat", "fever"}.issubset(symptoms):
        diagnoses.add("strep throat")
    if {"headache", "sensitivity to light"}.issubset(symptoms):
        diagnoses.add("migraine")
    if {"rash", "fever"}.issubset(symptoms):
        diagnoses.add("chickenpox")
    if {"shortness of breath", "wheezing"}.issubset(symptoms):
        diagnoses.add("asthma")

    return diagnoses