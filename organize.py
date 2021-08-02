import stat
import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.ipynb'],

    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
            else:
                nw_ext=value[1:]
                SUBDIRECTORIES[nw_ext]=value

    return nw_ext

files_sys=Path("/Users/thrib/Documents")
def organizeDirectory():
    for item in files_sys.iterdir():
         # scandir will grab every anything in the current working directorty
    
        if item.is_dir():
            continue
        file_name=item.stem  #gets it file_name
        #os.chmod(item, stat.S_IWRITE)
        filepath=Path(item) # i shoud get the paths, so that helps in manipulating files
        filetype=filepath.suffix.lower() # .suffix attribute return the file extension.
        directory=pickDirectory(filetype) # will get the category that file belongs to
        #directoryPath=Path(directory)

        directoryPath = files_sys.joinpath(directory)
        print(directoryPath)
        if not directoryPath.exists() :
            directoryPath.mkdir()
        #print(filepath)
        #print(directoryPath)
        new_path=directoryPath.joinpath(file_name) #adds file name at the end of the directory.
        #print(new_path)
        item.replace(new_path)

organizeDirectory()

