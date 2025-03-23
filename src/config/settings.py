from pydantic import BaseModel

class Settings(BaseModel):
    temperature: float = 0.1
    max_tokens: int = 150
    top_p: float = 0.9
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0

_current_settings = Settings()

def get_setting(key):
    return getattr(_current_settings, key, None)

def set_setting(key, value):
    if hasattr(_current_settings, key):
        setattr(_current_settings, key, value)
    else:
        raise KeyError(f"Setting '{key}' not found.")