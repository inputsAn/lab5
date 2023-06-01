import os, os.path

def processing():
    DIR = 'test_data'
    count_of_files =len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print(f"Количество файлов в директории: {count_of_files}")