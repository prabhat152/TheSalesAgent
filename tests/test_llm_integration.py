import pytest
from src.integrations.llm_integration import LLMIntegration

@pytest.fixture
def llm_integration():
    return LLMIntegration()

def test_send_query(llm_integration):
    query = "What are the latest Apple products?"
    response = llm_integration.generate_response(query)
    assert response is not None
    assert isinstance(response, str)

def test_receive_response(llm_integration):
    query = "Tell me about the iPhone 14."
    response = llm_integration.generate_response(query)
    assert response is not None
    assert "iPhone 14" in response

def test_error_handling(llm_integration):
    query = ""
    response = llm_integration.generate_response(query)
    assert response is not None  # Expecting an error message for empty query

def test_integration_with_ollama(llm_integration):
    query = "What is the best Apple laptop?"
    response = llm_integration.generate_response(query)
    assert "MacBook" in response or "MacBook Air" in response or "MacBook Pro" in response