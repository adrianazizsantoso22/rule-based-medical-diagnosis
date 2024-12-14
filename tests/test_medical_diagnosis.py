import unittest
from diagnosis import diagnosis

class TestMedicalDiagnosis(unittest.TestCase):
    
    def test_flu(self):
        symptoms = {"fever", "cough"}
        self.assertIn("flu", diagnosis(symptoms))

    def test_strep_throat(self):
        symptoms = {"sore throat", "fever"}
        self.assertIn("strep throat", diagnosis(symptoms))

    def test_migraine(self):
        symptoms = {"headache", "sensitivity to light"}
        self.assertIn("migraine", diagnosis(symptoms))

    def test_chickenpox(self):
        symptoms = {"rash", "fever"}
        self.assertIn("chickenpox", diagnosis(symptoms))

    def test_asthma(self):
        symptoms = {"shortness of breath", "wheezing"}
        self.assertIn("asthma", diagnosis(symptoms))

    def test_no_diagnosis(self):
        symptoms = {"nausea"}
        self.assertEqual(diagnosis(symptoms), set())

if __name__ == '__main__':
    unittest.main()
