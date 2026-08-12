# paths.py
from pathlib import Path

# Base directory setup
KAGGLE_CACHE_DIR = Path("/Users/hassothea/.cache/kagglehub/datasets/")

def get_all_kaggle_files(base_path):
    target = Path(base_path)
    if not target.exists():
        print(f"Warning: Path {target} does not exist.")
        return {}
    
    file_dict = {}
    
    # .rglob("*") recursively walks through every subfolder at every level
    for file in target.rglob("*"):
        if file.is_file():
            # Key: 'dataset_name/filename.csv' to avoid name collisions between different datasets
            # file.parts[-3] gets the dataset folder name, file.name gets the file
            if file.name[-3:] == 'csv':
                file_dict[file.name] = str(file.resolve())
    return file_dict

# Dynamically map absolutely everything inside your Kaggle cache

DATASET_FILES = get_all_kaggle_files(KAGGLE_CACHE_DIR)
DATASET_FILES['Enfants.txt'] = "/Users/hassothea/Documents/Teaching/ITC/Courses/Master/EDA/Slides/data/Enfants.txt"
DATASET_FILES['heart_failure.csv'] = '/Users/hassothea/.cache/kagglehub/datasets/fedesoriano/heart-failure-prediction/versions/1/heart.csv'
DATASET_FILES['columns.csv'] = "/Users/hassothea/Documents/Teaching/ITC/Courses/Master/EDA/Slides/data/columns.csv"
DATASET_FILES['amazon.csv'] = "/Users/hassothea/Documents/Teaching/AUPP/Data_Analytics/Courses/data/amazon.csv"
DATASET_FILES['account_activity.csv'] = "/Users/hassothea/Documents/Teaching/AUPP/Data_Analytics/Courses/data/account_activity.csv"
DATASET_FILES['marketing.csv'] = "/Users/hassothea/Documents/Teaching/AUPP/Data_Analytics/Courses/data/marketing.csv"
DATASET_FILES['faithful.csv'] = "/Users/hassothea/Documents/Teaching/AUPP/Data_Analytics/Courses/data/faithful.csv"
DATASET_FILES['Titanic-Dataset.csv'] = "/Users/hassothea/Documents/Teaching/AUPP/Data_Analytics/Courses/data/Titanic-Dataset.csv"
# Verification prints
# print(f"Base Directory: {KAGGLE_CACHE_DIR}")
# print(f"Found {len(DATASET_FILES)} files.")
# print("Mapped Files:", DATASET_FILES)