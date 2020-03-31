import os

def get_files_to_move(substr):
  files = []
  for file_name in os.listdir("./"):
    if substr in file_name:
      files.append(file_name)
  return files