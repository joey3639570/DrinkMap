from sqlHandler import SQLHandler
import pandas as pd

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
        
    def Query(self, key=dict):
        """
        key 有 主特徵 次特徵 價格下限 價格上限 店家 
        名字上是
        {'select1','select2','price_low','price_high','store_name'}
        型態上是
        {'string','string','int','int','string'}
        """
        #region unpack
        
        #define select1 = classname
        self.SetClass(key['select1'])
        self.drinkName = key['select2']
        self.SetPriceRange(key['price_low'], key['price_high'])
        self.SetShop(key['store_name'])
        #endregion
        
        sql = f"""
select ShopName, DrinkName, Cost
from (DrinkClass NATURAL JOIN Drink) NATURAL JOIN Shop
where Cost > {self.Min} AND Cost < {self.Max}
{f'AND ClassName = "{self.className}"' if self.className != None else ""}
{f'AND DrinkName like "%{self.drinkName}%"' if self.drinkName != None else ""}
{f'AND ShopName = "{self.Shop}"' if self.Shop != None else ""}
        """
        print(f"\nSQL:{sql}")
        #result = self.s.SQL(sql)
        df = pd.read_sql_query(sql, self.s.con)
        print(f'pd.dataframe:\n{df}')
        return df
        
if __name__ == "__main__":
    sm = SQLMain()
    
    key = {}
    key['select1'] = '水果茶'
    key['select2'] = '檸檬'
    key['price_low'] = 40
    key['price_high'] = 70
    key['store_name'] = '大苑子'
    
    df = sm.Query(key)