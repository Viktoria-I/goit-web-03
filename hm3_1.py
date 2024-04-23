import os
import threading
import shutil
import logging

def sort_files(source_folder, target_folder):

    logging.basicConfig(level=logging.INFO)

    logging.info(f"Start sorting files from '{source_folder}' to '{target_folder}'")
  
    if not os.path.exists(source_folder):
         logging.error(f"Error: Folder '{source_folder}' not found")
        
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_ext = os.path.splitext(file)

            ext_dir = os.path.join(target_folder, file_ext[1:])
            if not os.path.exists(ext_dir):
                try:
                    os.makedirs(ext_dir)
                except OSError as e:
                    logging.error(f"Error creating folder '{ext_dir}': {e}")
                    continue

            shutil.copy2(file_path, ext_dir)

    logging.info("Files were sorted.")

if __name__ == "__main__":
    source_folder = input("Input source folder path: ")
    target_folder = input("Input target folder path (default: 'E:\dist'): ") or "E:\dist"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    else:
        print(f"Error: Folder '{target_folder}' is exist. Please enter another folder name.")

    thread = threading.Thread(target=sort_files, args=(source_folder, target_folder))
    thread.start()
    thread.join()
    