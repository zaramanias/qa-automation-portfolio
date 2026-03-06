import os
import pytest
from dotenv import load_dotenv
from YougilePage import YougileApi


load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
COMPANY_ID = os.getenv("COMPANY_ID")
USER_ID = os.getenv("USER_ID")


@pytest.fixture()
def yougile():
    api = YougileApi()
    api.login(LOGIN, PASSWORD, COMPANY_ID)
    return api


def test_login(yougile):
    assert yougile.token is not None


def test_get_projs_positive(yougile):
    resp = yougile.get_proj()
    assert resp.status_code == 200
    assert len(resp.json()["content"]) == resp.json()["paging"]["count"]


def test_get_proj_with_invalid_id_negative(yougile):
    resp = yougile.get_proj("123")
    assert resp.status_code == 404


def test_post_proj_positive(yougile):
    title = "Noviy Proj"
    resp = yougile.new_proj(title, USER_ID)
    assert resp.status_code == 201

    proj_id = resp.json()["id"]
    new_resp = yougile.get_proj(proj_id)
    assert new_resp.json()["title"] == title
    assert USER_ID in new_resp.json()["users"]


def test_post_proj_bad_title_negative(yougile):
    title = ""
    resp = yougile.new_proj(title, USER_ID)

    assert resp.status_code == 400


def test_delete_proj_with_id_positive(yougile):
    resp = yougile.new_proj("Proj for delete", USER_ID)
    assert resp.status_code == 201

    proj_id = resp.json()["id"]

    delete = yougile.delete_proj(proj_id, deleted=True)
    assert delete.status_code == 200

    get_resp = yougile.get_proj(proj_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["deleted"] is True


def test_delete_all_proj_positive(yougile):
    resp = yougile.get_proj()
    assert resp.status_code == 200

    projs = resp.json()["content"]
    for proj in projs:
        proj_id = proj["id"]

        del_resp = yougile.delete_proj(proj_id, deleted=True)
        assert del_resp.status_code == 200

    resp = yougile.get_proj()
    assert len(resp.json()["content"]) == 0


def test_delete_proj_with_invalid_id(yougile):
    resp = yougile.delete_proj("123")
    assert resp.status_code == 404
