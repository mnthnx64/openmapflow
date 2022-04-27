from typing import List
import tarfile

from .config import FULL_PATHS
from .all_features import AllFeatures
from .dataset import LabeledDataset

training_data_path_keys = ["raw", "processed", "compressed_features.tar.gz"]


def create_features(datasets: List[LabeledDataset]):

    report = "DATASET REPORT (autogenerated, do not edit directly)"
    for d in datasets:
        text = d.create_features()
        report += "\n\n" + text

    all_features = AllFeatures()
    empty_text = all_features.check_empty()
    print(empty_text)
    duplicates_text = all_features.check_duplicates()
    print(duplicates_text)
    report += "\n\nAll data:\n" + empty_text + "\n" + duplicates_text

    with FULL_PATHS["datasets"].open("w") as f:
        f.write(report)

    # Compress features for faster CI/CD
    print("Compressing features...")
    with tarfile.open(FULL_PATHS["datasets"], "w:gz") as tar:
        tar.add(FULL_PATHS["datasets"], arcname="features")


def generate_project():
    """
    Generates an openmapflow.yaml and and sets up the project.
    """
    pass

    # - take unique project name - set it inside the notebooks
    # - bucket creation: remote storage, tifs, earth engine, press, preds-merged
    # - container registry creation
    # env creation

    # If project is directly in git repo
    # dvc init

    # If project is in subdirectory
    # cd <subdir> dvc init --subdir

    # Make data directories: [models, features, processed_labels, raw_labels]

    # Add dvc data: [models, features, processed_labels, raw_labels]
    # dvc add data/raw_labels ...
    # dvc commit

    # Set dvc remote, Google Drive by default for simplicity
    # https://dvc.org/doc/user-guide/setup-google-drive-remote

    # dvc remote add -d gdrive \
    #   gdrive://1EMHILcNFwdusMHHs4eC4OVIJ0Ncp9fiY/crop-mask-example-dvc-store

    # from google.cloud import storage  # type: ignore


def generate_gcloud_architecture():
    pass
    # Check if any of them exist, if yes, choose new project id

    # Create all buckets

    # Create container registry

    # Save to cloud run

    # - download example labels, features, models
    # - dvc init things
