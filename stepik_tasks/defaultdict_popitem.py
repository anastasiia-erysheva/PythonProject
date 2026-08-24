from collections import OrderedDict
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
for i in range(len(data)):
    rule = False if i % 2 == 0 else True
    k, v = data.popitem(last = rule)
    new_data[k] = v
print(new_data)

