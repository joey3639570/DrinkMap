import sqlite3

class SQLHandler:
    def __init__(self):
        super().__init__()
        
    def Start(self):
        self.con = sqlite3.connect('./mydatabase.db')

        self.cursorObj = self.con.cursor()

    print("Opened sql successfully.")

    def SQL(self, cmd = str):
        result = self.cursorObj.execute(cmd)
        if not result is None:
            for res in result:
                line = ", ".join([str(s) for s in res])
                print(line)
                
    def Close(self):
        self.con.close()
        
if __name__ == '__main__':
    s = SQLHandler()
    s.Start()
    s.SQL("DROP TABLE IF EXISTS STUDENT;")
    s.SQL("""CREATE TABLE STUDENT (
        `Name` CHAR(20) NOT NULL,
        `Student_Number` INT NOT NULL,
        `Class` INT NOT NULL,
        `Major` CHAR(10) NOT NULL,
        PRIMARY KEY (`Student_Number`)
        );""")
    s.SQL("""
        INSERT INTO STUDENT
        VALUES('Smith', 17, 1, 'CS'),
            ('Brown', 8, 2, 'CS');""")
    s.SQL("""UPDATE STUDENT
          SET Class = 3
          where Class=1""")
    s.SQL("""select *
          from STUDENT;""")