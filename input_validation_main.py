def main():
    print("Selamat datang di Sistem Diagnosis Medis!")
    print("Masukkan gejala Anda, pisahkan dengan koma (misalnya: fever, cough, rash).")
    symptoms_input = input("Gejala Anda: ").strip()

    # Input validation
    if not symptoms_input:
        print("Tidak ada gejala yang dimasukkan. Silakan coba lagi.")
        return
    # Add more input validation logic as needed