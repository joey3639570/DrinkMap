from sqlHandler import SQLHandler

s = SQLHandler()

s.Start()
line = ["""
DROP TABLE IF EXISTS Shop;""","""
CREATE TABLE Shop(
   ShopName VARCHAR(7) NOT NULL
  ,ShopID   INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT
  ,Time     VARCHAR(11)
  ,Tel      VARCHAR(10)
  ,Address  VARCHAR(14)
);""","""
INSERT INTO Shop(ShopName,ShopID,Time,Tel,Address) VALUES ('[台南]拉CHA茶',1,NULL,NULL,NULL);""","""
INSERT INTO Shop(ShopName,ShopID,Time,Tel,Address) VALUES ('[台南]Mr.WISH',2,'10:30-22:30','06-2088832','台南市東區育樂街52號');""","""
INSERT INTO Shop(ShopName,ShopID,Time,Tel,Address) VALUES ('[台南]麻古茶坊',3,'08:00-22:00','06-2002221','台南市東區大學路西段1號');""","""
INSERT INTO Shop(ShopName,ShopID,Time,Tel,Address) VALUES ('[台南]鮮茶道',4,'09:20-22:30','06-2388877','台南市東區育樂街156-2號');""","""
INSERT INTO Shop(ShopName,ShopID,Time,Tel,Address) VALUES ('[台南]大苑子',5,'10:00-22:30','06-2082238','台南市東區勝利路149號');
""", """
drop table if exists DrinkClass;
""", """CREATE TABLE DrinkClass (
	classname text,
	classid text
);
""", """INSERT INTO DrinkClass VALUES ('奶茶','A0001');
""", """INSERT INTO DrinkClass VALUES ('鮮奶茶','A0002');
""", """INSERT INTO DrinkClass VALUES ('泰式奶茶','A0003');
""", """INSERT INTO DrinkClass VALUES ('紅茶','B0001');
""", """INSERT INTO DrinkClass VALUES ('綠茶','C0001');
""", """INSERT INTO DrinkClass VALUES ('檸檬茶','D0001');
""", """INSERT INTO DrinkClass VALUES ('高山茶','E0001');
""", """INSERT INTO DrinkClass VALUES ('水果茶','F0001');
""", """INSERT INTO DrinkClass VALUES ('咖啡','G0001');
""", """INSERT INTO DrinkClass VALUES ('鮮奶','H0001');
""", """INSERT INTO DrinkClass VALUES ('巧克力','I0001');
""", """INSERT INTO DrinkClass VALUES ('其它','J0001');
""", """
drop table if exists Drink;
""", """CREATE TABLE Drink (
	shopid int,
	drinkname text,
	classid text,
	cost int
);
""", """INSERT INTO Drink VALUES (1,'就是拉茶','A0003',50);
""", """INSERT INTO Drink VALUES (1,'絲襪奶茶','A0003',50);
""", """INSERT INTO Drink VALUES (1,'特濃奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (1,'泰式奶茶','A0003',60);
""", """INSERT INTO Drink VALUES (1,'泰式奶綠','A0003',60);
""", """INSERT INTO Drink VALUES (1,'隨便拉','A0003',50);
""", """INSERT INTO Drink VALUES (1,'搭波奶奶茶','A0003',50);
""", """INSERT INTO Drink VALUES (1,'可可奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (1,'鴛鴦奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (1,'黑糖奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (1,'凍檸檬茶','D0001',50);
""", """INSERT INTO Drink VALUES (1,'四季春茶','E0001',25);
""", """INSERT INTO Drink VALUES (1,'茉莉綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (1,'烏龍綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (1,'紅紅紅茶','B0001',25);
""", """INSERT INTO Drink VALUES (2,'光果茶','F0001',55);
""", """INSERT INTO Drink VALUES (2,'芒果果粒茶','F0001',50);
""", """INSERT INTO Drink VALUES (2,'酸甜百香綠','F0001',50);
""", """INSERT INTO Drink VALUES (2,'金鑽鳳梨青','F0001',55);
""", """INSERT INTO Drink VALUES (2,'鮮榨柳橙綠','F0001',60);
""", """INSERT INTO Drink VALUES (2,'橙柚纖果子','F0001',60);
""", """INSERT INTO Drink VALUES (2,'愛文芒果冰沙','F0001',80);
""", """INSERT INTO Drink VALUES (2,'荔枝橙橙','F0001',65);
""", """INSERT INTO Drink VALUES (2,'熟果茶','F0001',65);
""", """INSERT INTO Drink VALUES (2,'水蜜桃果粒茶','F0001',50);
""", """INSERT INTO Drink VALUES (2,'蘋果果粒茶','F0001',50);
""", """INSERT INTO Drink VALUES (2,'桑葚冰茶','F0001',55);
""", """INSERT INTO Drink VALUES (2,'野营果粒茶','F0001',60);
""", """INSERT INTO Drink VALUES (2,'野营纖果子','F0001',60);
""", """INSERT INTO Drink VALUES (2,'鮮榨葡萄柚綠','F0001',65);
""", """INSERT INTO Drink VALUES (2,'烤糖葡萄柚','F0001',75);
""", """INSERT INTO Drink VALUES (2,'青果茶','F0001',60);
""", """INSERT INTO Drink VALUES (2,'鲜榨檸檬綠','F0001',50);
""", """INSERT INTO Drink VALUES (2,'鮮榨金桔綠','F0001',50);
""", """INSERT INTO Drink VALUES (2,'白蔗青','F0001',50);
""", """INSERT INTO Drink VALUES (2,'白蔗檸檬青','F0001',50);
""", """INSERT INTO Drink VALUES (2,'金桔檸檬','F0001',50);
""", """INSERT INTO Drink VALUES (2,'檸檬多多','F0001',60);
""", """INSERT INTO Drink VALUES (2,'桔檸纖果子','F0001',60);
""", """INSERT INTO Drink VALUES (2,'蜂蜜檸檬','F0001',65);
""", """INSERT INTO Drink VALUES (2,'鮮榨奇異果汁','F0001',80);
""", """INSERT INTO Drink VALUES (2,'濃厚奶茶','A0002',50);
""", """INSERT INTO Drink VALUES (2,'白玉珍珠濃厚奶茶','A0002',55);
""", """INSERT INTO Drink VALUES (2,'黑糖珍珠濃厚奶茶','A0002',60);
""", """INSERT INTO Drink VALUES (2,'焦糖餅乾濃厚奶茶','A0002',60);
""", """INSERT INTO Drink VALUES (2,'紅/綠/青茶芝芝','J0001',55);
""", """INSERT INTO Drink VALUES (2,'鐵觀音芝芝','J0001',60);
""", """INSERT INTO Drink VALUES (2,'蜜香烏龍芝芝','J0001',65);
""", """INSERT INTO Drink VALUES (2,'抹茶芝芝','J0001',85);
""", """INSERT INTO Drink VALUES (2,'香濃巧克力','I0001',75);
""", """INSERT INTO Drink VALUES (2,'橙果巧克力','I0001',75);
""", """INSERT INTO Drink VALUES (2,'鮮奶紅茶','A0002',50);
""", """INSERT INTO Drink VALUES (2,'鮮奶綠茶','A0002',50);
""", """INSERT INTO Drink VALUES (2,'鐵觀音鮮奶茶','A0002',55);
""", """INSERT INTO Drink VALUES (2,'白玉珍珠鮮奶茶','A0002',55);
""", """INSERT INTO Drink VALUES (2,'黑糖珍珠鮮奶','A0002',65);
""", """INSERT INTO Drink VALUES (2,'燕麥鮮奶茶','A0002',60);
""", """INSERT INTO Drink VALUES (2,'抹茶鮮奶','A0002',60);
""", """INSERT INTO Drink VALUES (2,'高山青茶','E0001',30);
""", """INSERT INTO Drink VALUES (2,'熟成紅茶','B0001',30);
""", """INSERT INTO Drink VALUES (2,'茉香綠茶','C0001',30);
""", """INSERT INTO Drink VALUES (2,'炭培鐵觀音','E0001',35);
""", """INSERT INTO Drink VALUES (2,'小蟬蜜香烏龍','E0001',40);
""", """INSERT INTO Drink VALUES (2,'綠茶多多','C0001',50);
""", """INSERT INTO Drink VALUES (2,'草莓厚奶','A0001',80);
""", """INSERT INTO Drink VALUES (2,'芒果厚奶','A0001',80);
""", """INSERT INTO Drink VALUES (2,'奇異果厚奶','A0001',80);
""", """INSERT INTO Drink VALUES (3,'香橙百香綠茶','F0001',60);
""", """INSERT INTO Drink VALUES (3,'翡翠香橙','F0001',55);
""", """INSERT INTO Drink VALUES (3,'柳橙綠茶','F0001',60);
""", """INSERT INTO Drink VALUES (3,'翡翠柳橙','F0001',55);
""", """INSERT INTO Drink VALUES (3,'番茄梅蜜','F0001',55);
""", """INSERT INTO Drink VALUES (3,'奇異果綠茶','F0001',65);
""", """INSERT INTO Drink VALUES (3,'葡萄柚綠茶','F0001',55);
""", """INSERT INTO Drink VALUES (3,'葡萄柚蜜茶','F0001',55);
""", """INSERT INTO Drink VALUES (3,'百香綠茶','F0001',50);
""", """INSERT INTO Drink VALUES (3,'百香雙Q果','F0001',50);
""", """INSERT INTO Drink VALUES (3,'檸檬汁','F0001',45);
""", """INSERT INTO Drink VALUES (3,'金桔檸檬','F0001',45);
""", """INSERT INTO Drink VALUES (3,'檸檬紅茶','F0001',45);
""", """INSERT INTO Drink VALUES (3,'檸檬綠茶','F0001',45);
""", """INSERT INTO Drink VALUES (3,'蜂蜜檸檬','F0001',55);
""", """INSERT INTO Drink VALUES (3,'檸檬多多','F0001',60);
""", """INSERT INTO Drink VALUES (3,'百香多多','F0001',60);
""", """INSERT INTO Drink VALUES (3,'葡萄柚多多','F0001',65);
""", """INSERT INTO Drink VALUES (3,'錫蘭奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'鐵觀音奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'沖繩奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'波霸奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'椰果奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'咖啡凍奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'仙草凍奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (3,'布丁奶茶','A0001',55);
""", """INSERT INTO Drink VALUES (3,'玫瑰奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (3,'翡翠綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (3,'錫蘭紅茶','B0001',25);
""", """INSERT INTO Drink VALUES (3,'高山金萱茶','E0001',25);
""", """INSERT INTO Drink VALUES (3,'四季春茶','E0001',25);
""", """INSERT INTO Drink VALUES (3,'文山清茶','E0001',25);
""", """INSERT INTO Drink VALUES (3,'烏龍綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (3,'古早味紅茶','B0001',25);
""", """INSERT INTO Drink VALUES (3,'紅茶拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (3,'鐵觀音拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (3,'沖繩鮮奶茶','A0002',55);
""", """INSERT INTO Drink VALUES (3,'波霸紅茶拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (3,'阿華田拿鐵','A0002',65);
""", """INSERT INTO Drink VALUES (3,'布丁鮮奶茶','A0002',65);
""", """INSERT INTO Drink VALUES (3,'玫瑰拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (3,'桂圓拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (3,'冬瓜茶','J0001',25);
""", """INSERT INTO Drink VALUES (3,'梅子冰茶','J0001',25);
""", """INSERT INTO Drink VALUES (3,'冬瓜青茶','E0001',30);
""", """INSERT INTO Drink VALUES (3,'冬瓜檸檬','D0001',45);
""", """INSERT INTO Drink VALUES (3,'檸檬梅子','D0001',50);
""", """INSERT INTO Drink VALUES (3,'冰淇淋紅茶','B0001',45);
""", """INSERT INTO Drink VALUES (3,'梅子綠茶','C0001',35);
""", """INSERT INTO Drink VALUES (3,'多多綠茶','C0001',45);
""", """INSERT INTO Drink VALUES (3,'阿華田拿鐵','A0002',50);
""", """INSERT INTO Drink VALUES (3,'桂圓紅棗茶','J0001',35);
""", """INSERT INTO Drink VALUES (4,'琥珀奶茶','A0001',35);
""", """INSERT INTO Drink VALUES (4,'茉香奶茶','A0001',35);
""", """INSERT INTO Drink VALUES (4,'伯爵奶茶','A0001',40);
""", """INSERT INTO Drink VALUES (4,'焙茶烤奶','A0001',45);
""", """INSERT INTO Drink VALUES (4,'沖繩黑糖奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (4,'珍珠奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (4,'仙草凍奶茶','A0001',45);
""", """INSERT INTO Drink VALUES (4,'布丁奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (4,'紅豆玄米奶茶','A0001',50);
""", """INSERT INTO Drink VALUES (4,'聖塔露黑可可','I0001',45);
""", """INSERT INTO Drink VALUES (4,'抹茶拿鐵','A0002',50);
""", """INSERT INTO Drink VALUES (4,'紅茶拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (4,'綠茶拿鐵','A0002',55);
""", """INSERT INTO Drink VALUES (4,'抹茶紅豆珍珠','A0002',55);
""", """INSERT INTO Drink VALUES (4,'伯爵拿鐵','A0002',60);
""", """INSERT INTO Drink VALUES (4,'黑糖珍珠撞奶','A0002',60);
""", """INSERT INTO Drink VALUES (4,'招牌水果茶','F0001',60);
""", """INSERT INTO Drink VALUES (4,'鮮果雙Q紅茶','F0001',55);
""", """INSERT INTO Drink VALUES (4,'鮮果雙Q綠茶','F0001',55);
""", """INSERT INTO Drink VALUES (4,'水晶冬瓜茶','F0001',30);
""", """INSERT INTO Drink VALUES (4,'藍莓果茶','F0001',40);
""", """INSERT INTO Drink VALUES (4,'墾丁冰茶','F0001',40);
""", """INSERT INTO Drink VALUES (4,'梅果綠茶','F0001',40);
""", """INSERT INTO Drink VALUES (4,'養樂多綠茶','C0001',45);
""", """INSERT INTO Drink VALUES (4,'鳳梨清茶','F0001',45);
""", """INSERT INTO Drink VALUES (4,'檸檬CC','F0001',40);
""", """INSERT INTO Drink VALUES (4,'鮮桔檸檬','F0001',50);
""", """INSERT INTO Drink VALUES (4,'蘆薈好蜜','F0001',50);
""", """INSERT INTO Drink VALUES (4,'蜂蜜檸好','F0001',60);
""", """INSERT INTO Drink VALUES (4,'冬瓜檸檬','F0001',50);
""", """INSERT INTO Drink VALUES (4,'芭樂檸檬玉露','F0001',50);
""", """INSERT INTO Drink VALUES (4,'紅心芭樂梅','F0001',60);
""", """INSERT INTO Drink VALUES (4,'紅心芭樂汁','F0001',60);
""", """INSERT INTO Drink VALUES (4,'薑汁撞奶','A0001',55);
""", """INSERT INTO Drink VALUES (4,'黑糖薑茶','J0001',55);
""", """INSERT INTO Drink VALUES (4,'檸檬翡翠冰鑽','D0001',50);
""", """INSERT INTO Drink VALUES (4,'鳳梨冰鑽','F0001',50);
""", """INSERT INTO Drink VALUES (4,'青梅冰鑽','F0001',50);
""", """INSERT INTO Drink VALUES (4,'可可冰鑽','I0001',50);
""", """INSERT INTO Drink VALUES (4,'抹茶冰鑽','C0001',50);
""", """INSERT INTO Drink VALUES (4,'四季春','E0001',35);
""", """INSERT INTO Drink VALUES (4,'蜜香紅茶','E0001',35);
""", """INSERT INTO Drink VALUES (4,'玉露煎茶','E0001',35);
""", """INSERT INTO Drink VALUES (4,'蜜香果茶','F0001',45);
""", """INSERT INTO Drink VALUES (4,'寒天四季奶青','A0001',55);
""", """INSERT INTO Drink VALUES (4,'阿里山里佳甘露','E0001',45);
""", """INSERT INTO Drink VALUES (4,'日月潭紅茶','E0001',45);
""", """INSERT INTO Drink VALUES (4,'古香烏龍','B0001',25);
""", """INSERT INTO Drink VALUES (4,'古香紅茶','B0001',25);
""", """INSERT INTO Drink VALUES (4,'阿里山冰茶','C0001',25);
""", """INSERT INTO Drink VALUES (4,'頂級茉莉綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (4,'琥珀紅茶','B0001',25);
""", """INSERT INTO Drink VALUES (4,'凍頂烏龍茶','B0001',25);
""", """INSERT INTO Drink VALUES (4,'文山清茶','C0001',25);
""", """INSERT INTO Drink VALUES (4,'烏龍綠茶','C0001',25);
""", """INSERT INTO Drink VALUES (4,'伯爵紅茶','B0001',30);
""", """INSERT INTO Drink VALUES (4,'茶花綠茶','C0001',30);
""", """INSERT INTO Drink VALUES (4,'炭燒培茶','B0001',30);
""", """INSERT INTO Drink VALUES (4,'日式玄米茶','C0001',30);
""", """INSERT INTO Drink VALUES (5,'愛文芒果冰沙','F0001',80);
""", """INSERT INTO Drink VALUES (5,'愛文翡翠','F0001',65);
""", """INSERT INTO Drink VALUES (5,'金鑽鳳梨冰沙','F0001',65);
""", """INSERT INTO Drink VALUES (5,'芭梨戀人','F0001',65);
""", """INSERT INTO Drink VALUES (5,'番茄梅','F0001',60);
""", """INSERT INTO Drink VALUES (5,'芭樂檸檬','F0001',60);
""", """INSERT INTO Drink VALUES (5,'繽紛水果茶','F0001',65);
""", """INSERT INTO Drink VALUES (5,'天天5蔬果汁','F0001',60);
""", """INSERT INTO Drink VALUES (5,'蜂蜜檸檬','F0001',60);
""", """INSERT INTO Drink VALUES (5,'戀戀檸檬','F0001',60);
""", """INSERT INTO Drink VALUES (5,'翡翠檸檬','F0001',55);
""", """INSERT INTO Drink VALUES (5,'鮮果香果綠','F0001',55);
""", """INSERT INTO Drink VALUES (5,'柚美粒','F0001',60);
""", """INSERT INTO Drink VALUES (5,'鮮搾葡萄柚綠','F0001',60);
""", """INSERT INTO Drink VALUES (5,'百香愛玉/檸檬愛玉','F0001',60);
""", """INSERT INTO Drink VALUES (5,'愛文鮮果咖啡','G0001',80);
""", """INSERT INTO Drink VALUES (5,'檸檬鮮果咖啡','G0001',75);
""", """INSERT INTO Drink VALUES (5,'葡萄柚鮮果咖啡','G0001',75);
""", """INSERT INTO Drink VALUES (5,'古城錫蘭紅茶','B0001',30);
""", """INSERT INTO Drink VALUES (5,'文山清茶','E0001',30);
""", """INSERT INTO Drink VALUES (5,'纖活綠茶','C0001',30);
""", """INSERT INTO Drink VALUES (5,'許慶良鮮奶茶','A0002',45);
""", """INSERT INTO Drink VALUES (5,'許慶良珍珠鮮奶茶','A0002',45);
""", """INSERT INTO Drink VALUES (5,'許慶良觀音拿鐵','A0002',45);
""", """INSERT INTO Drink VALUES (5,'許慶良珍珠觀音拿鐵','A0002',45);
""", """INSERT INTO Drink VALUES (5,'許慶良鮮奶','H0001',119);
""", """INSERT INTO Drink VALUES (5,'百果輕果飲','F0001',35);
""", """INSERT INTO Drink VALUES (5,'葡萄柚輕果飲','F0001',35);
""", """INSERT INTO Drink VALUES (5,'蘋果醋冰茶','F0001',50);
""", """INSERT INTO Drink VALUES (5,'蔓越莓冰醋','F0001',50);
""", """INSERT INTO Drink VALUES (5,'養樂多綠茶','C0001',50);
""", """INSERT INTO Drink VALUES (5,'蜜仙草','J0001',50);
""", """INSERT INTO Drink VALUES (5,'冬瓜檸檬','D0001',55);
""", """INSERT INTO Drink VALUES (5,'金桔粒脆纖果','F0001',60);
""", """INSERT INTO Drink VALUES (5,'蔓美粒','F0001',60);
""", """INSERT INTO Drink VALUES (5,'蘋果多輕飲','F0001',65);
""", """INSERT INTO Drink VALUES (5,'奶茶','A0001',35);
""", """INSERT INTO Drink VALUES (5,'珍珠奶茶','A0001',35);
""", """INSERT INTO Drink VALUES (5,'仙草凍奶茶','A0001',35);
""",
"""DROP TABLE IF EXISTS ShopItems;""","""
CREATE TABLE ShopItems(
   ShopID INTEGER  NOT NULL
  ,ItemID VARCHAR(5) NOT NULL
);""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa006');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa007');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa008');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa009');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa010');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (2,'aa005');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa007');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa019');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa002');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa020');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa021');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa023');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa022');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa017');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (3,'aa013');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa001');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa011');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa012');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa013');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa007');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa014');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa003');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa002');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa015');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa016');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa017');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (4,'aa018');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (5,'aa001');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (5,'aa002');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (5,'aa003');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (5,'aa004');""","""
INSERT INTO ShopItems(ShopID,ItemID) VALUES (5,'aa005');""","""
DROP TABLE IF EXISTS Items;""","""
CREATE TABLE Items(
   ItemName VARCHAR(4) NOT NULL
  ,ItemID   VARCHAR(5) NOT NULL
);""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('珍珠','aa001');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('仙草凍','aa002');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('蘆薈','aa003');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('脆纖果','aa004');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('愛玉','aa005');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('白玉珍珠','aa006');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('椰果','aa007');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('羅勒子','aa008');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('黑糖珍珠','aa009');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('燕麥','aa010');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('QQ','aa011');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('荔枝QQ','aa012');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('寒天','aa013');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('紅豆','aa014');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('小紫蘇','aa015');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('統一布丁','aa016');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('養樂多','aa017');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('密鳳梨','aa018');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('咖啡凍','aa019');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('波霸','aa020');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('雙Q果','aa021');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('蜂蜜','aa022');""","""
INSERT INTO Items(ItemName,ItemID) VALUES ('布丁','aa023');""","""
"""
]
for l in line:
    s.SQL(l, True)
s.Close()
