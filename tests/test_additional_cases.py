import unittest
from medical_diagnosis_system.diagnosis import diagnosis

class TestAdditionalCases(unittest.TestCase):
    def test_overlapping_conditions(self):
        symptoms = {"fever", "cough", "rash", "sore throat"}
        result = diagnosis(symptoms)
        self.assertIn("flu", result)
        self.assertIn("chickenpox", result)

    def test_empty_input(self):
        symptoms = set()
        self.assertEqual(diagnosis(symptoms), [])

    def test_unrelated_symptoms(self):
        symptoms = {"anxiety", "stress"}
        self.assertEqual(diagnosis(symptoms), [])

if __name__ == "__main__":
    unittest.main()
