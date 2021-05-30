import sqlite3

class SQLHandler:
    def __init__(self):
        super().__init__()
        
    def Start(self):
        self.con = sqlite3.connect('./mydatabase.db')

        self.cursorObj = self.con.cursor()

        print("Opened sql successfully.")

    def SQL(self, cmd = str, commit = False):
        result = self.cursorObj.execute(cmd)
        if not result is None:
            if commit:
                self.con.commit()
            return result
                
    def Close(self):
        self.con.close()
        