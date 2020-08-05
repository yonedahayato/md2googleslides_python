import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

parser = argparse.ArgumentParser()

parser.add_argument("file_path")

def upload_to_drive(file_path):
    """upload_to_drive func

    upload file to drive

    Args:
        file_path(str): upload file path

    """
    gauth = GoogleAuth()
    gauth.CommandLineAuth()

    drive = GoogleDrive(gauth)
    f = drive.CreateFile()
    f.SetContentFile(file_path)
    f.Upload()
    print(file_path)

if __name__ == "__main__":
    args = parser.parse_args()
    upload_to_drive(args.file_path)
