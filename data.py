import sqlite3

class DataBase:
    def __init__(self,db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""create table if not exists Data(id INTEGER PRIMARY KEY AUTOINCREMENT,prefixe text, name text, id_bot text, status text, ping text, joue text, ligne text, next text,token text)""")
        self.connect.commit()

    def fetch_all(self) -> list[tuple[str,...]]:
        self.cursor.execute("select * from Data")
        row = self.cursor.fetchall()
        return row

    def insert(self,prefixe,name,id,status,ping,joue,ligne,next,token):
        self.id = len(self.fetch_all())
        self.cursor.execute("insert into Data values(?,?,?,?,?,?,?,?,?,?)",(self.id,prefixe,name,id,status,ping,joue,ligne,next,token,))
        self.connect.commit()

    def delete(self,what_delete,app,x=None):
        if what_delete == "last_row":
            if len(app.row_data) >= 1:
                app.remove_row(app.row_data[-1])
                self.cursor.execute("delete from Data where id_bot=(?)",(self.fetch_all()[-1][3],))
                self.connect.commit()
        elif what_delete == "all_row":
            if len(self.fetch_all()) >= 1:
                for i in range(len(app.row_data)):
                    app.remove_row(app.row_data[-1])
                self.cursor.execute("delete from Data")
                self.connect.commit()
        elif what_delete == "id":
            if len(app.row_data) >= 1:
                self.cursor.execute("delete from Data where id_bot=(?)",(x,))
                self.connect.commit()
                self.update_id()

    def update(self,id,new_value):
        self.cursor.execute("update Data set prefixe=? where id_bot=?",(new_value,id,))
        self.connect.commit()

    def update_id(self):
        for i,x in zip(range(len(self.fetch_all())),self.fetch_all()):
            self.cursor.execute("update Data set id=? where id_bot=?",(i,x[3],))
            self.connect.commit()