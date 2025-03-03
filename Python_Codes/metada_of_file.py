import os
import time

file_path = "photo.jpg"

created_time = time.ctime(os.path.getctime(file_path))
modified_time = time.ctime(os.path.getmtime(file_path))

print(f"File name: {"".join(list(file_path)[:-4])}")
print(f"Created Time: {created_time}")
print(f"Modified Time: {modified_time}")