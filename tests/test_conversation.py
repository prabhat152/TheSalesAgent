import unittest
from unittest.mock import MagicMock
from src.agent.conversation import Conversation

class TestConversation(unittest.TestCase):

    def setUp(self):
        self.mock_steve = MagicMock()
        self.conversation = Conversation(steve=self.mock_steve)

    def test_initial_state(self):
        self.assertEqual(self.conversation.state, "waiting")
        self.assertEqual(self.conversation.history, [])

    def test_user_input_handling(self):
        user_input = "Tell me about the latest iPhone."
        self.mock_steve.handle_user_input.return_value = "Information about iPhone"
        response = self.conversation.handle_user_input(user_input)
        self.assertIn("iPhone", response)
        self.assertEqual(self.conversation.state, "responding")

    def test_multi_turn_conversation(self):
        self.mock_steve.handle_user_input.return_value = "Okay"
        self.conversation.handle_user_input("What can you tell me about Apple products?")
        self.conversation.handle_user_input("And the MacBook?")
        self.assertGreater(len(self.conversation.history), 1)

    def test_conversation_end(self):
        self.mock_steve.handle_user_input.return_value = "Goodbye"
        self.conversation.handle_user_input("Thank you, that's all.")
        self.assertEqual(self.conversation.state, "ended")

if __name__ == '__main__':
    unittest.main()