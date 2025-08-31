import pytest
import requests
from config import Config


@pytest.fixture(scope="session")
def auth_headers():
    """Фикстура для авторизационных заголовков"""
    return {
        "Authorization": f"Bearer {Config.API_TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def base_url():
    """Фикстура для базового URL"""
    return Config.BASE_URL


@pytest.fixture
def cleanup_project(auth_headers, base_url):
    """Фикстура для очистки созданных проектов после тестов"""
    created_projects = []

    yield created_projects

    for project_id in created_projects:
        try:
            response = requests.delete(
                f"{base_url}/projects/{project_id}",
                headers=auth_headers
            )
        except:
            pass