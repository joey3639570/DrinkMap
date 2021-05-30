from sqlHandler import SQLHandler

s = SQLHandler()

s.Start()
line =[
"""
select *
from DrinkClass""",
"""
select *
from Drink""",
"""
select *
from Shop""",
]
for l in line:
    result = s.SQL(l)
    for res in result:
        line = ", ".join([str(s) for s in res])
        print(line)
s.Close()