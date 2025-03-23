# Contents of /ThemeSalesMan/ThemeSalesMan/tests/test_settings.py

import pytest
from src.config.settings import Settings

def test_default_settings():
    settings = Settings()
    assert settings.temperature == 0.1
    assert settings.max_tokens == 150
    assert settings.top_p == 0.9
    assert settings.presence_penalty == 0.0
    assert settings.frequency_penalty == 0.0

def test_custom_settings():
    custom_settings = Settings(temperature=0.5, max_tokens=100)
    assert custom_settings.temperature == 0.5
    assert custom_settings.max_tokens == 100
    assert custom_settings.top_p == 0.9  # Default value
    assert custom_settings.presence_penalty == 0.0  # Default value
    assert custom_settings.frequency_penalty == 0.0  # Default value