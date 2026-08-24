from zipfile import ZipFile
with ZipFile("workbook.zip")as zip_file:
    info = zip_file.infolist()
    file_size = 0
    file_compressed_size = 0
    for item in info:
        file_size += item.file_size
        file_compressed_size += item.compress_size
print(f"Объем исходных файлов: {file_size} байт(а)")
print(f"Объем сжатых файлов: {file_compressed_size} байт(а)")