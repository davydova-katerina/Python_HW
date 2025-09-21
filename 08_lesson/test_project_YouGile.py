from project_YouGile import ProjectYouGile

api = ProjectYouGile('https://ru.yougile.com/api-v2/')


def test_create_project_():
    # количество проектов до
    login = "davydova.katerina84@gmail.com",
    password = "Trfnthbyf_84",
    name = "Test project"
    projects_before = api.get_project_list(login=login,
                                           password=password,
                                           name=name)
    len_before = len(projects_before)

    # создание проекта
    title = 'ГосУслуги'
    users = {"4902b994-b806-4af4-acec-018ea5ea6468": "worker"}
    companyID = "9347006b-dc75-4550-97d5-3008ba00d4a0"
    result = api.create_project(title, users, login, password, companyID)
    new_id = result['id']

    # количество проектов после
    projects_after = api.get_project_list(login=login,
                                          password=password,
                                          name=name)
    len_after = len(projects_after)

    assert len_after - len_before == 1
    assert projects_after[-1]['title'] == title
    assert projects_after[-1]['id'] == new_id


def test_get_project_with_id():
    # создание проекта
    login = "davydova.katerina84@gmail.com",
    password = "Trfnthbyf_84",
    companyID = "9347006b-dc75-4550-97d5-3008ba00d4a0"
    title = 'Get_ГосУслуги'
    users = {"4902b994-b806-4af4-acec-018ea5ea6468": "worker"}
    result = api.create_project(title, users, login, password, companyID)
    project_id = result['id']

    # обращаемся к проекту
    new_project = api.get_project_with_id(project_id)

    assert new_project['title'] == title
    assert new_project['users'] == users


def test_edit_project():
    login = "avydova.katerina84@gmail.com",
    password = "Trfnthbyf_84",
    companyID = "9347006b-dc75-4550-97d5-3008ba00d4a0"
    title = 'Edit_ГосУслуги'
    users = {"4902b994-b806-4af4-acec-018ea5ea6468": "worker"}

    result = api.create_project(title, users, login, password, companyID)

    project_id = result['id']
    new_deleted = 'false'
    new_title = 'Edited_ГосУслуги'
    new_users = {"4902b994-b806-4af4-acec-018ea5ea6468": "worker"}

    edited = api.edit_project(project_id, new_deleted, new_title, new_users)

    assert edited['title'] == new_title