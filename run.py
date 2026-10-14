from app.core.config import get_settings

settings = get_settings()

print(f"App Name: {settings.app_name}")
print(f"Groq API Key: {settings.groq_api_key}")
