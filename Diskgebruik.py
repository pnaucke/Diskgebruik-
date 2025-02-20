import shutil
import os

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

total, used, free = shutil.disk_usage("/")

photos_folder = "C:\photos"
documents_folder = "C:\documents"

photos_size = get_folder_size(os.path.expanduser(photos_folder))
documents_size = get_folder_size(os.path.expanduser(documents_folder))

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
print("Photos: %d GiB" % (photos_size // (2**30)))
print("Documents: %d GiB" % (documents_size // (2**30)))