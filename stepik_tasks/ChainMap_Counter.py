from collections import Counter
from collections import ChainMap
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
chain_map = ChainMap(bread, meat, sauce, vegetables, toppings)
ing = input().split(",")
counted = Counter(ing)
sorted_counted = sorted(counted.items())
max_key = max(len(k) for k, v in sorted_counted)
total = 0
for k, v in sorted_counted:
    total += chain_map[k] * v
total_price = f"ИТОГ: {total}р"
lines = []
for k, v in sorted_counted:
    line = f"{k.ljust(max_key)} x {v}"
    lines.append(line)
lines.append(total_price)
line_length = max(len(s) for s in lines)
for line in lines[:-1]:
    print(line)
print("-" * line_length)
print(total_price)


