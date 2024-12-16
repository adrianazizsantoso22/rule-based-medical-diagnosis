def diagnosis(symptoms):
    """
    Fungsi untuk menentukan diagnosis berdasarkan gejala.
    
    Args:
        symptoms (set): Set gejala yang dimasukkan pengguna.
    
    Returns:
        list: Daftar kemungkinan diagnosis berdasarkan gejala.
    """
    # Aturan diagnosis
    rules = {
        "cold": {"fever", "cough", "sore throat"},
        "flu": {"fever", "cough", "sore throat", "body ache"},
        "chickenpox": {"fever", "rash", "fatigue"},
        "measles": {"fever", "rash", "cough", "conjunctivitis"},
    }

    # Mengecek gejala yang cocok dengan setiap aturan
    results = []
    for condition, condition_symptoms in rules.items():
        if symptoms & condition_symptoms == condition_symptoms:
            results.append(condition)

    return results