from zipfile import ZipFile
with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    best_k = 100.00
    best_file_name = ""
    for item in info:
        if item.file_size > 0:
            k = (item.compress_size / item.file_size) * 100
            if k < best_k:
                best_k = k
                best_file_name = item.filename.split("/")[-1]
print(best_file_name)