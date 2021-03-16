import zipfile
import os

z = zipfile.ZipFile('spam.zip', 'w')        # Создание нового архива
for root, dirs, files in os.walk('.'):      # Список всех файлов и папок в директории folder
    for file in files:
        z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив

z.close()
