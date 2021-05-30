from sqlHandler import SQLHandler

class SQLMain:
    def __init__(self):
        super().__init__()
        self.s = SQLHandler()
        self.s.Start()
        self.Min = 0
        self.Max = 999
        self.className = None
        self.Shop = None
    
    def SetPriceRange(self, Min = 0, Max = 999):
        self.Min = Min 
        self.Max = Max
    
    def SetClass(self, className = None):
        self.className = className
    
    def SetShop(self, Shop = None):
        self.Shop = Shop
        
    def Query(self):
        sql = f""" 
        select ShopName, DrinkName, Cost
        from (DrinkClass NATURAL JOIN Drink) NATURAL JOIN Shop
        where Cost > {self.Min} AND Cost < {self.Max}
        {f'AND ClassName = "{self.className}"' if self.className != None else ""}{f'AND ShopName = "{self.Shop}"' if self.Shop != None else ""}
        """
        print(sql)
        result = self.s.SQL(sql)
        for res in result:
            line = ", ".join([str(s) for s in res])
            print(line)
            
if __name__ == "__main__":
    sm = SQLMain()
    sm.SetClass("鮮奶茶")
    sm.SetShop()
    sm.Query()