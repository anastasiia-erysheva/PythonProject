from zipfile import ZipFile
with ZipFile("workbook.zip") as zip_file:
    info = zip_file.namelist()
file_count = 0
for file in info:
    if not file.endswith("/"):
        file_count += 1
print(file_count)