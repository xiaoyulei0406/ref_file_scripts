import argparse
import os
import shutil
import glob

## add input and output arguments
def parse_argument():
    parser = argparse.ArgumentParser(
        description = 'Re-organize ***folder based on different file extensions'
    )
    parser.add_argument('-i', dest = 'input_dir', help = 'Input file folder that needed to be reorganized')
    args=parser.parse_args()
    return args

# dict for different file extension

exts = {
    'literatures' : ['.pdf'],
    'docs' : ['.csv','.doc','.docx','.ppt','.pptx','.xls','.xlsx'],
    'images': ['.jpg', '.png', '.jpeg', '.gif'],
}

# sort files based on extensions

def get_sort (file):
    keys = list (exts.keys())
    for key in keys:
        for ext in exts[key]:
            if file.endswith (ext):
                return (key)

# Iterations for files in the input file folder

def main():
    args = parse_argument()
    file_folder = args.input_dir
    if not os.path.isdir(file_folder):
        print('\nFile folder is not exist')
    else:
        files = glob.glob(file_folder)

        for file in files:
            dist = get_sort(file)
            if dist:
                try:
                    shutil.move(file, "../newsorts/" + dist)
                except:
                    print(file + " is already exist")
            else:
                try:
                    shutil.move(file, "../newsorts/others")
                except:
                    print(file + " is already exist")


if __name__ == '__main__':
    main()
