import unittest
from medical_diagnosis_system.diagnosis import diagnosis

class TestMedicalDiagnosis(unittest.TestCase):
    def test_exact_match(self):
        symptoms = {"fever", "cough", "sore throat"}
        self.assertEqual(diagnosis(symptoms), ["cold"])

    def test_multiple_conditions(self):
        symptoms = {"fever", "rash", "cough", "fatigue", "conjunctivitis"}
        result = diagnosis(symptoms)
        self.assertIn("measles", result)
        self.assertIn("chickenpox", result)

    def test_no_match(self):
        symptoms = {"headache", "nausea"}
        self.assertEqual(diagnosis(symptoms), [])

    def test_partial_match(self):
        symptoms = {"fever", "cough"}
        self.assertEqual(diagnosis(symptoms), [])

if __name__ == "__main__":
    unittest.main()