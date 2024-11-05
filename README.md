# dicom-viewer
Python command-line tool to view DICOM medical images (x-rays, etc.)

## Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
1. Put the files from your doctor in a folder at the root of this repo
2. Run the following command. This will find all of your DICOM image files, display them in figures, then save them as .JPEG files to an output directory:
```
python view.py <base-directory>
```
where `<base-directory>` is the directory that contains all of your DICOM image files