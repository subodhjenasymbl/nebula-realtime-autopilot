import subprocess
import sys


def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Warning: {e}")


def run_lint():
    run_command(["python", "-m", "black", "analyst"])
    run_command(["python", "-m", "isort", "analyst"])
    run_command(["python", "-m", "pylint", "analyst"])


def run_test():
    run_command(["python", "-m", "pytest", "tests"])


def run_coverage():
    run_command(["python", "-m", "coverage", "run", "-m", "pytest", "tests"])
    run_command(["python", "-m", "coverage", "report", "-m"])


def run_safety():
    run_command(["python", "-m", "safety", "check", "--full-report"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        task = sys.argv[1]
        if task == "lint":
            run_lint()
        elif task == "test":
            run_test()
        elif task == "coverage":
            run_coverage()
        elif task == "safety":
            run_safety()
        else:
            print(
                "Invalid task. Please specify 'lint', 'test', 'coverage', or 'safety'."
            )
    else:
        print("No task specified. Please specify a task to run.")
