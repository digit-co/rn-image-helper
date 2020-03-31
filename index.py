import os
from ios import create_ios_folder
from android import move_android_assets

# 1. Export + rename files from Figma

# Map from whatever name the asset had in Figma to the desired name
name_map = {
  "incentive asset": "incentive_lock",
}

def rename_figma_files(name_map):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  for file_name in os.listdir("./"):
    if not file_name.endswith(".png"):
      continue
    for old_name in name_map:
      if old_name not in file_name:
        continue
      new_name = file_name.replace(old_name, name_map[old_name])
      # Standardize naming for @1x sizing
      if "@" not in new_name:
        new_name = new_name.split(".")[0] + "@1x.png"
      old_path = "{}/{}".format(dir_path, file_name)
      new_path = "{}/{}".format(dir_path, new_name)
      os.rename(old_path, new_path)

rename_figma_files(name_map)

# 2. Move files to iOS + Android folders
# Map from name of asset to iOS folder
name_to_folder = {
  "incentive_lock": "incentiveLock"
}

for image_name in name_to_folder:
  folder = name_to_folder[image_name]
  create_ios_folder(image_name, folder)
  move_android_assets(image_name)