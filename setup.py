import sys
import subprocess
import os
import platform
import webbrowser
from urllib.request import urlopen
import time

def check_python_version():
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("Error: Python 3.7 or higher is required")
        print(f"Your version: Python {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor} detected")
    return True

def check_pip():
    print("\nChecking pip installation...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
        print("✓ pip is installed")
        return True
    except subprocess.CalledProcessError:
        print("Error: pip is not installed")
        return False

def install_requirements():
    print("\nInstalling required packages...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✓ All requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print("Error installing requirements:")
        print(e)
        return False
    except FileNotFoundError:
        print("Error: requirements.txt not found in current directory")
        return False

def check_file_structure():
    print("\nChecking project file structure...")
    required_files = [
        "app.py",
        "requirements.txt",
        os.path.join("static", "script.js"),
        os.path.join("templates", "index.html")
    ]

    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print("Error: Missing required files:")
        for file in missing_files:
            print(f"  - {file}")
        return False

    print("✓ All required files present")
    return True

def check_port_availability():
    print("\nChecking if port 5000 is available...")
    try:
        urlopen("http://localhost:5000", timeout=1)
        print("Warning: Port 5000 is already in use")
        return False
    except:
        print("✓ Port 5000 is available")
        return True

def main():
    print("=== Oven Timer App Setup ===")

    # Check all requirements
    python_ok = check_python_version()
    pip_ok = check_pip()
    files_ok = check_file_structure()
    port_ok = check_port_availability()

    if not all([python_ok, pip_ok, files_ok]):
        print("\nSetup failed. Please fix the above errors and try again.")
        return

    # Install requirements
    if not install_requirements():
        print("\nSetup failed during package installation.")
        return

    print("\n=== Setup completed successfully! ===")
    print("\nTo run the application:")
    print("1. Open a terminal/command prompt")
    print("2. Navigate to this directory")
    print("3. Run: python app.py")
    print("4. Open your web browser and go to: http://localhost:5000")

    # Ask to run the application
    run_now = input("\nWould you like to run the application now? (y/n): ")
    if run_now.lower() == 'y':
        print("\nStarting the application...")
        try:
            process = subprocess.Popen([sys.executable, "app.py"])
            time.sleep(2)  # Wait for server to start
            webbrowser.open('http://localhost:5000')
            print("\nApplication is running!")
            print("Press Ctrl+C in this terminal to stop the server when done.")
            process.wait()
        except KeyboardInterrupt:
            process.terminate()
            print("\nApplication stopped.")
        except Exception as e:
            print(f"\nError starting application: {e}")

if __name__ == "__main__":
    main()
