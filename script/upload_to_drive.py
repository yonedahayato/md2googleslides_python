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

    print("file path 1: {}".format(file_path))
    # file_path = file_path.encode('utf-8')
    file_path = file_path.encode('utf-16', 'surrogatepass')
    # file_path = file_path.encode('cp932')
    print("file path 2: {}".format(file_path))
    # file_path = file_path.decode("utf-8")
    # file_path = file_path.decode("Shift_JIS")
    file_path = file_path.decode('utf-16', 'surrogatepass')

    print("file path 3: {}".format(file_path))

    f.SetContentFile(file_path)
    f.Upload()

if __name__ == "__main__":
    args = parser.parse_args()
    upload_to_drive(args.file_path)
