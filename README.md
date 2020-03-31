Helper script for creating React Native assets for iOS and Android.

To use the script
1) Make sure file path is correct. I have both this repo and digit-mobile on my Desktop. Otherwise, modify `constants.py` accordingly.
2) Download the 1x, 2x, and 3x assets from Figma. Move them to within the folder.
3) Edit `name_map`, `name_to_folder` in `index.py` depending on which assets you want to add.
4) Run `index.py`. This should add the iOS and Android assets to `digit-mobile`.

Some quirks:
1) The Contents.json files for iOS have trailing spaces that will need to manually fixed.
2) You can manually clean up the extra image files + iOS directory folder.
