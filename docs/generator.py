import os

def walkdir(dirpath=""):
    for root, dirs, files in os.walk(dirpath):
        print(root, dirs, files)


if __name__ == "__main__":
    walkdir(".")
