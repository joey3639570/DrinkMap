# -*- coding: utf-8 -*-
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
    
    def AddShop(self, value, 
                output = lambda x:print(x), 
                confirm_callback = lambda:input('Confirm Input? (y/n)\n')):
        """
        輸入 dictionary 
        key是
        {'storename','storetime1','storetime2','storephone'}
        型態上是
        {'string','string','string','string'}
        以此插入資料庫內
        並且以資料庫的編號順序排下去
        """
        
        sql = f"""INSERT INTO Shop(ShopName,Time,Tel,Address) VALUES ('{value["storename"]}','{value["storetime1"]}-{value["storetime2"]}','{value["storephone"]}','{value["storeaddress"]}');
        """
        self.s.SQL(sql)
        
        sql = """
        SELECT *
        FROM Shop;
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        
        output(f'Result Will Be:\n{df}')
        
        ensure = ""
        while not ensure in ["y","n"]:
            ensure = confirm_callback()
            if ensure == "y":
                self.s.Commit()
                df = pd.read_sql_query(sql, self.s.con)
                output(f'Result:\n{df}')
            elif ensure == "n":
                self.s.Abort()
                df = pd.read_sql_query(sql, self.s.con)
                output(f'Result:\n{df}')
                
        return df
    
    def GetShopList(self,
                    output = lambda x:print(x)):
        sql = """
        SELECT shopname, shopid
        FROM Shop;
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        output(df)
        
        l = list(zip(*df.values.tolist()))
        
        return list(zip(l[0], l[1]))
    
    def GetShopListByItem(self, ItemName,
                    output = lambda x:print(x)):
        sql = f"""
        SELECT ShopName
        FROM Shop natural join ShopItems natural join Items
        where ItemName = '{ItemName}';
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        output(df)
        return [t[0] for t in df.values.tolist()] 

    def GetDrinkList(self,
                 output = lambda x:print(x)):
        """
        列出飲料類別列表:
        無須input，執行便會回傳
        飲料類別 的list
        e.g.[奶茶,鮮奶茶,泰式奶茶,紅茶,綠茶]
        """
        
        sql = f"""
        SELECT classname
        FROM DrinkClass;
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        ret = [t[0] for t in df.values.tolist()]
        output(ret)
        return ret
    
    def GetDrink(self, id,
                 output = lambda x:print(x)):
        sql = f"""
        SELECT drinkname, ClassName, cost
        FROM Drink natural join DrinkClass
        where shopid={id};
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        output(df)
        return df
    
    def GetItemList(self,
                 output = lambda x:print(x)):
        """
        列出加料類別列表:
        無須input，執行便會回傳
        加料類別 的list
        e.g. [珍珠,仙草凍,蘆薈,脆纖果,愛玉]
        """
        
        sql = f"""
        SELECT ItemName
        FROM Items;
        """
        output(f"\nSQL:{sql}")
        df = pd.read_sql_query(sql, self.s.con)
        ret = [t[0] for t in df.values.tolist()]
        output(ret)
        return ret

    
    def SetPriceRange(self, Min = 0, Max = 999):
        if Min != None and Min != '':
            self.Min = Min 
        if Max != None and Max != '':
            self.Max = Max
    
    def SetClass(self, className = None):
        self.className = className
    
    def SetShop(self, Shop = None):
        self.Shop = Shop
        
    def Query(self, key=dict, output = lambda x:print(x)):
        """
        key 有 主特徵 次特徵 價格下限 價格上限 店家 
        名字上是
        {'select1','select2','price_low','price_high','store_name'}
        型態上是
        {'string','string','int','int','string'}
        """
        #region unpack
        
        #define select1 = classname
        self.SetClass(key.setdefault('select1', None))
        self.drinkName = key.setdefault('select2', None)
        self.SetPriceRange(key.setdefault('price_low', None), key.setdefault('price_high', None))
        self.SetShop(key.setdefault('store_name', None))
        #endregion
        
        sql = f"""
select ShopName, DrinkName, Cost
from (DrinkClass NATURAL JOIN Drink) NATURAL JOIN Shop
where Cost > {self.Min} AND Cost < {self.Max}
{f'AND ClassName = "{self.className}"' if self.className != None else ""}
{f'AND DrinkName like "%{self.drinkName}%"' if self.drinkName != None else ""}
{f'AND ShopName = "{self.Shop}"' if self.Shop != None else ""}
        """
        output(f"\nSQL:{sql}")
        #result = self.s.SQL(sql)
        df = pd.read_sql_query(sql, self.s.con)
        output(f'pd.dataframe:\n{df}')
        return df
        
if __name__ == "__main__":
    sm = SQLMain()
    
    key = {}
    key['select1'] = '水果茶'
    key['select2'] = '檸檬'
    key['store_name'] = None
    
    key['price_low'] = None
    key['price_high'] = None
    df = sm.Query(key)
    
    
    """
    key = {'storename':"test",'storetime1':"08:00",'storetime2':"10:00",'storephone':"0123456789","storeaddress":"home"}
    df = sm.AddShop(key, 
                    output = lambda x:print(x), 
                    confirm_callback= lambda:input('Confirm Input? (y/n)\n'))
    """
                    
    # print(sm.GetShopList(output = lambda x:print(x))) # [('拉CHA茶', 1), ('Mr.WISH', 2), ('麻古茶坊', 3), ('鮮茶道', 4), ('大苑子', 5)]
    
    #sm.GetDrink(5, output = lambda x:print(x))
    
    # sm.GetDrinkList() # ['奶茶', '鮮奶茶', '泰式奶茶', '紅茶', '綠茶', '檸檬茶', '高山茶', '水果茶', '咖啡', '鮮奶', '巧克力', '其它'] 
    
    # sm.GetItemList() # ['珍珠', '仙草凍', '蘆薈', '脆纖果', '愛玉', '白玉珍珠', '椰果', '羅勒子', '黑糖珍珠', '燕麥', 'QQ', '荔枝QQ', '寒天', '紅豆', '小紫蘇', '統一布丁', '養樂多', '密鳳梨', '咖啡凍', '波霸', '雙Q果', '蜂蜜', '布丁']
    
    print(sm.GetShopListByItem('珍珠')) # ['鮮茶道', '大苑子']
    