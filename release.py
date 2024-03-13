import subprocess
import sys


def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def build_package():
    print("Building package...")
    run_command(["python", "setup.py", "sdist", "bdist_wheel"])


def upload_package():
    print("Uploading package to PyPI...")
    run_command(["twine", "upload", "dist/*"])


if __name__ == "__main__":
    build_package()
    if len(sys.argv) > 1 and sys.argv[1] == "--no-upload":
        print("Skipping upload to PyPI.")
    else:
        upload_package()
