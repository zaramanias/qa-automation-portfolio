from lesson_9_page import dbclass

db = dbclass(
    "postgresql+psycopg://postgres:Zxcvbn4321@localhost:5432/QA")


def test_get_subjects():
    list_subj = db.get_subjects()
    assert len(list_subj) == 14


def test_add_new_subj():
    list_before_adding = db.get_subjects()
    db.create("Spanish")
    list_after_adding = db.get_subjects()

    assert len(list_after_adding) == len(list_before_adding) + 1

    max_id = db.get_max_id()
    db.delete(max_id)


def test_edit_subj():
    db.create("Chinese")
    id = db.get_max_id()
    new_name = "Chinese Traditional"
    db.edit(id, new_name)
    new_subj = db.get_subject_by_id(id)[0]
    assert new_subj["subject_title"] == new_name
    db.delete(id)


def test_delete_subj():
    subj_before_adding = db.get_subjects()

    titles = [
        "Sexologia",
        "Metodologia",
        "Alterlogia"
    ]
    created_ids = []

    for title in titles:
        db.create(title)
        new_id = db.get_max_id()
        created_ids.append(new_id)

    subj_after_adding = db.get_subjects()
    assert len(subj_after_adding) == len(subj_before_adding) + len(titles)

    for id in created_ids:
        db.delete(id)

    subj_after_delete = db.get_subjects()
    assert len(subj_after_delete) == len(subj_before_adding)
