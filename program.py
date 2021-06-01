import os
import cat_service
import subprocess
import platform

def main():
    print_header()

    folder = get_or_create_output_folder()
    print(f'Found or created folder: {folder}')
    download_cats(folder)
    display_cats(folder)
    

def print_header():
    print('-------------------------')
    print('-------CAT-FACTORY-------')
    print('-------------------------')

def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)
    
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path

def download_cats(folder):
    print('Contacting the server to download some cat pics!')
    cat_count = 8
    for i in range(1,cat_count+1):
        print(f'Downloading cat {i}')
        name = f'lolcat_{i}'
        cat_service.get_cat(folder, name)

    print('Done downloading your cat images!')

def display_cats(folder):
    operating_system = platform.system()

    if operating_system == "Windows":
        print('Displaying cats in Windows OS')
        subprocess.call(['explorer', folder])
    elif operating_system == "Linux":
        print('Displaying cats in Linux OS')
        subprocess.call(['xdg-open', folder])
    elif operating_system == "Darwin":
        print('Displaying cats in Mac OS')
        subprocess.call(['open', folder])
    else:
        print(f"We don't support your os: {operating_system}")


if __name__ == '__main__':
    main()