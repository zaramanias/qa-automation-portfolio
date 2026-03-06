import requests

base_url = "https://yougile.com/api-v2"


class YougileApi:
    def __init__(self):
        self.token = None
        self.headers = {}

    def login(self, login, password, company_id):
        resp = requests.post(f"{base_url}/auth/keys/get", json={
            "login": login, "password": password, "companyId": company_id})
        self.token = resp.json()[0]["key"]
        self.headers = {"Authorization": f"Bearer {self.token}"}
        return resp

    def get_proj(self, proj_id=None):
        if proj_id:
            url = f"{base_url}/projects/{proj_id}"
        else:
            url = f"{base_url}/projects"
        resp = requests.get(url, headers=self.headers)
        return resp

    def new_proj(self, title, user_id):
        resp = requests.post(f"{base_url}/projects", json={
            "title": title, "users": {user_id: "admin"}}, headers=self.headers)
        return resp
    
    def new_board(self, title: str, proj_id: str) -> requests.Response:
        resp = requests.post(f"{base_url}/boards", json={
            "title": title, "projectId": proj_id}, headers=self.headers)
        return resp

    def new_column(self, title: str,
                   color: int, board_id: str) -> requests.Response:
        resp = requests.post(f"{base_url}/columns", json={
            "title": title, "color": color, "boardId": board_id},
            headers=self.headers)
        return resp

    def new_task(self, title: str, column_id: str,
                 description: str = "") -> requests.Response:
        resp = requests.post(f"{base_url}/tasks", json={
            "title": title, "columnId": column_id, "description": description},
            headers=self.headers)
        return resp

    def get_tasks(self) -> requests.Response:
        resp = requests.get(f"{base_url}/task-list", headers=self.headers)
        return resp

    def get_task_by_id(self, id: str) -> requests.Response:
        resp = requests.get(f"{base_url}/tasks/{id}", headers=self.headers)
        return resp

    def delete_task(self, id: str) -> requests.Response:
        resp = requests.put(f"{base_url}/tasks/{id}",
                            json={"deleted": True}, headers=self.headers)
        return resp

    def delete_proj(self, proj_id: str,
                    deleted: bool = True) -> requests.Response:
        resp = requests.put(f"{base_url}/projects/{proj_id}", json={
            "deleted": deleted}, headers=self.headers)
        return resp
