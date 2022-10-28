from PIL import Image
from os import walk

def reduce_img_tohalf(img_path, new_img_path):
    img = Image.open(img_path)
    width, height = img.size
    new_width = int(width / 2)
    new_height = int(height / 2)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(new_img_path)

# resize all files in folder and subfolders

def resize_all_files_in_folder(folder_path):
    for (dirpath, dirnames, filenames) in walk(folder_path):
        for filename in filenames:
            if filename.endswith('.JPG'):
                img_path = dirpath + '/' + filename
                new_img_path = dirpath + '/' + 'half_' + filename
                reduce_img_tohalf(img_path, new_img_path)

resize_all_files_in_folder('Tropy_materiales/docs/procedimiento rebelión - 1833')