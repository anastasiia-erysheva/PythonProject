from zipfile import ZipFile
target_date = (2021, 11, 30, 14, 22, 0)
result_files = []
with ZipFile("workbook.zip") as zip_file:
    data = zip_file.infolist()
    for item in data:
        if item.file_size > 0 and item.date_time > target_date:
            result_files.append(item.filename.split("/")[-1])
result_files.sort()
for item in result_files:
    print(item)
