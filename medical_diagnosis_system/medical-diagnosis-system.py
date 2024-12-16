from medical_diagnosis_system.diagnosis import diagnosis

def main():
    print("Selamat datang di Sistem Diagnosis Medis!")
    print("Masukkan gejala Anda, pisahkan dengan koma (misalnya: fever, cough, rash).")
    symptoms_input = input("Gejala Anda: ").strip()

    # Validasi input
    if not symptoms_input:
        print("Tidak ada gejala yang dimasukkan. Silakan coba lagi.")
        return

    # Proses input menjadi set gejala
    symptoms = set(symptom.strip().lower() for symptom in symptoms_input.split(","))

    # Panggil fungsi diagnosis
    results = diagnosis(symptoms)

    # Tampilkan hasil
    if results:
        print("\nBerdasarkan gejala yang Anda masukkan, berikut adalah kemungkinan diagnosis:")
        for condition in results:
            print(f"- {condition}")
    else:
        print("\nGejala yang dimasukkan tidak cocok dengan diagnosis apa pun.")
        print("Silakan konsultasikan dengan dokter untuk pemeriksaan lebih lanjut.")

if __name__ == "__main__":
    main()