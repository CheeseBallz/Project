import os
import shutil
import time

# files to simulate
FILES = {
    "secret_doc.txt": "Confidential project data",
    "credentials.txt": "user: admin | pass: 12345",
    "photo.jpg": "FAKE_IMAGE_DATA",
}

# files to delete
TO_DELETE = ["secret_doc.txt", "photo.jpg"]

# folders
BASE_DIR = os.getcwd()
RESIDUAL_DIR = os.path.join(BASE_DIR, ".residual")
RECOVERY_DIR = os.path.join(BASE_DIR, "recovered")


def create_files():
    os.makedirs(RESIDUAL_DIR, exist_ok=True)

    for name, content in FILES.items():
        path = os.path.join(BASE_DIR, name)

        with open(path, "w") as f:
            f.write(content)

        shutil.copy(path, os.path.join(RESIDUAL_DIR, name))

    print("Files created")


def delete_files():
    for name in TO_DELETE:
        path = os.path.join(BASE_DIR, name)
        if os.path.exists(path):
            os.remove(path)
            print("Deleted:", name)


def recover_files():
    os.makedirs(RECOVERY_DIR, exist_ok=True)

    recovered = []

    for name in TO_DELETE:
        src = os.path.join(RESIDUAL_DIR, name)
        dst = os.path.join(RECOVERY_DIR, name)

        if os.path.exists(src):
            shutil.copy(src, dst)
            recovered.append(name)
            print("Recovered:", name)

    return recovered


if __name__ == "__main__":
    print("Lost Data Recovery Simulation\n")

    create_files()
    time.sleep(1)

    delete_files()
    time.sleep(1)

    recovered = recover_files()

    print("Recovery rate:", len(recovered), "/", len(TO_DELETE))