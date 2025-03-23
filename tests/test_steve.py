import unittest
from unittest.mock import MagicMock
from src.agent.steve import Steve

class TestSteve(unittest.TestCase):

    def setUp(self):
        self.steve = Steve(llm_integration=None)
        self.mock_llm = MagicMock()
        self.steve.llm_integration = self.mock_llm

    def test_product_recommendation(self):
        # Test for a specific product recommendation
        response = self.steve.recommend_product("iPhone")
        self.assertIn("iPhone", response)

    def test_answering_questions(self):
        # Test Steve's ability to answer a question
        question = "What is the latest MacBook model?"
        response = self.steve.answer_question(question)
        self.assertIsInstance(response, str)

    def test_interaction_with_llm(self):
        # Test interaction with the LLM
        user_input = "Tell me about the Apple Watch."
        self.mock_llm.generate_response.return_value = "Apple Watch description from LLM"
        response = self.steve.interact_with_llm(user_input)
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()