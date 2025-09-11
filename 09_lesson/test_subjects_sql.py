import pytest
from sqlalchemy.exc import IntegrityError
from conftest import Subject


class TestSubjectCRUD:
    """Тесты для CRUD операций с сущностью Subject"""

    def test_add_subject(self, db_session):
        """Тест добавления нового предмета"""
        # Подготовка
        subject_title = "Math"

        # Действие
        new_subject = Subject(name=subject_title)
        db_session.add(new_subject)
        db_session.commit()

        # Проверка
        saved_subject = db_session.query(Subject).filter_by(name=subject_title).first()
        assert saved_subject is not None
        assert saved_subject.name == subject_title

        # Очистка (автоматически через фикстуру db_session)

    def test_update_subject(self, db_session):
        """Тест изменения названия предмета"""
        # Подготовка - создаем предмет
        original_name = "PA"
        new_name = "PA_new"

        subject = Subject(name=original_name)
        db_session.add(subject)
        db_session.commit()

        # Действие - изменяем название
        subject_to_update = db_session.query(Subject).filter_by(name=original_name).first()
        subject_to_update.name = new_name
        db_session.commit()

        # Проверка
        updated_subject = db_session.query(Subject).filter_by(name=new_name).first()
        assert updated_subject is not None
        assert updated_subject.name == new_name

        # Проверяем, что старого названия больше нет
        old_subject = db_session.query(Subject).filter_by(name=original_name).first()
        assert old_subject is None

    def test_delete_subject(self, db_session):
        """Тест удаления предмета"""
        # Подготовка - создаем предмет
        subject_title = "Art"

        subject = Subject(name=subject_title)
        db_session.add(subject)
        db_session.commit()

        # Проверяем, что предмет создан
        created_subject = db_session.query(Subject).filter_by(name=subject_title).first()
        assert created_subject is not None

        # Действие - удаляем предмет
        subject_to_delete = db_session.query(Subject).filter_by(name=subject_title).first()
        db_session.delete(subject_to_delete)
        db_session.commit()

        # Проверка
        deleted_subject = db_session.query(Subject).filter_by(name=subject_title).first()
        assert deleted_subject is None

    def test_add_duplicate_subject_should_fail(self, db_session):
        """Тест: добавление дубликата предмета должно вызывать ошибку"""
        # Подготовка
        subject_title = "Biology"

        subject1 = Subject(name=subject_title)
        db_session.add(subject1)
        db_session.commit()

        # Действие и проверка - попытка добавить дубликат
        subject2 = Subject(name=subject_title)
        db_session.add(subject2)

        with pytest.raises(IntegrityError):
            db_session.commit()

        # Откатываем failed transaction
        db_session.rollback()