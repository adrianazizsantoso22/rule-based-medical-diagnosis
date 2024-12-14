import unittest
from medical_diagnosis_system import diagnosis

class TestAdditionalMedicalDiagnosis(unittest.TestCase):
    
    def test_multiple_conditions(self):
        symptoms = {"fever", "cough", "sore throat"}
        self.assertIn("flu", diagnosis(symptoms))
        self.assertIn("strep throat", diagnosis(symptoms))

    def test_single_symptom(self):
        symptoms = {"fever"}
        self.assertEqual(diagnosis(symptoms), set())  # No diagnosis should match just fever

    def test_unrecognized_symptom(self):
        symptoms = {"headache", "nausea"}
        self.assertEqual(diagnosis(symptoms), set())  # No diagnosis should match this combination

    def test_combination_with_extra_symptoms(self):
        symptoms = {"fever", "cough", "headache"}
        self.assertIn("flu", diagnosis(symptoms))  # Should identify flu

    def test_empty_symptoms(self):
        symptoms = set()
        self.assertEqual(diagnosis(symptoms), set())  # No symptoms should yield no diagnosis

if __name__ == '__main__':
    unittest.main()