import pytest
import json
from projects_api import ProjectsAPI


class TestProjects:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = ProjectsAPI()
        self.created_projects = []

    def teardown_method(self):
        """Очистка созданных проектов после каждого теста"""
        for project_id in self.created_projects:
            try:
                self.api.delete_project(project_id)
            except:
                pass

    # POSITIVE TESTS

    def test_create_project_positive(self):
        """Позитивный тест создания проекта"""
        project_data = {
            "title": "Test project",
            "description": "Test project description"
        }

        response = self.api.create_project(project_data)

        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["title"] == project_data["title"]

        project_id = response.json()["id"]
        self.created_projects.append(project_id)

    def test_get_project_positive(self):
        """Позитивный тест получения проекта"""
        # Сначала создаем проект
        project_data = {
            "title": "Project to Get",
            "description": "Project for get test"
        }
        create_response = self.api.create_project(project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        response = self.api.get_project(project_id)

        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["title"] == project_data["title"]

    def test_update_project_positive(self):
        """Позитивный тест обновления проекта"""
        project_data = {
            "title": "Original Project",
            "description": "Original description"
        }
        create_response = self.api.create_project(project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        update_data = {
            "title": "Updated Project",
            "description": "Updated description"
        }
        response = self.api.update_project(project_id, update_data)

        assert response.status_code == 200
        assert response.json()["title"] == update_data["title"]
        assert response.json()["description"] == update_data["description"]

    # NEGATIVE TESTS

    def test_create_project_negative_missing_title(self):
        """Негативный тест создания проекта без обязательного поля title"""
        project_data = {
            "description": "Project without title"
        }

        response = self.api.create_project(project_data)

        assert response.status_code == 400
        assert "error" in response.json()

    def test_get_project_negative_nonexistent_id(self):
        """Негативный тест получения несуществующего проекта"""
        nonexistent_id = "nonexistent_id_12345"

        response = self.api.get_project(nonexistent_id)

        assert response.status_code == 404
        assert "error" in response.json()

    def test_update_project_negative_invalid_data(self):
        """Негативный тест обновления проекта с невалидными данными"""
        project_data = {
            "title": "Test Project",
            "description": "Test description"
        }
        create_response = self.api.create_project(project_data)
        project_id = create_response.json()["id"]
        self.created_projects.append(project_id)

        invalid_data = {
            "title": "",  # Пустое название - должно быть невалидно
            "description": "Updated description"
        }

        response = self.api.update_project(project_id, invalid_data)

        # Предполагаем, что API вернет ошибку валидации
        assert response.status_code in [400, 422]
        assert "error" in response.json()

    def test_update_project_negative_nonexistent_id(self):
        """Негативный тест обновления несуществующего проекта"""
        nonexistent_id = "nonexistent_id_12345"
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }

        response = self.api.update_project(nonexistent_id, update_data)

        assert response.status_code == 404
        assert "error" in response.json()