from zipfile import ZipFile
from datetime import datetime

all_files = []
with ZipFile("workbook.zip") as zip_file:
    for info in zip_file.infolist():
        if info.file_size > 0:
            dt = datetime(*info.date_time)
            pretty_date = dt.strftime("%Y-%m-%d %H:%M:%S")
            all_files.append((info.filename.split('/')[-1], pretty_date, info.file_size, info.compress_size))

all_files.sort()

for name, date, size, compress_size in all_files:
    print(name)  # Чистое имя, без лишних пробелов на конце
    print(f"  Дата модификации файла: {date}")  # Ровно два пробела в начале
    print(f"  Объем исходного файла: {size} байт(а)")  # Ровно два пробела в начале
    print(f"  Объем сжатого файла: {compress_size} байт(а)")  # Ровно два пробела в начале
    print() о