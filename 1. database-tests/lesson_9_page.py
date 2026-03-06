from sqlalchemy import create_engine, text


class dbclass:
    __scripts = {
        "select": text("select * from subject"),
        "select by id": text(
            "select * from subject where subject_id = :select_id"),
        "delete by id": text(
            "delete from subject where subject_id = :id_to_delete"),
        "insert new": text("""
                insert into subject ("subject_title")
                values (:new_subject_title)
                   """),
        "get max id": text("select MAX(subject_id) from subject"),
        "edit": text("""
                          update subject set subject_title = :new_title
                          where subject_id = :select_id
                          """)
        }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_subject_by_id(self, id):
        conn = self.db.connect()
        result = conn.execute(
            self.__scripts["select by id"], {"select_id": id})
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        with self.db.begin() as conn:
            conn.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    def create(self, title):
        with self.db.begin() as conn:
            conn.execute(self.__scripts[
                "insert new"], {"new_subject_title": title})

    def edit(self, id, title):
        with self.db.begin() as conn:
            conn.execute(self.__scripts["edit"], {
                "select_id": id, "new_title": title})

    def get_max_id(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["get max id"])
        max_id = result.scalar()
        conn.close()
        return max_id
