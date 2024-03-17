import subprocess

def run_test():
    # Execute test1.py
    test_process = subprocess.Popen(["python", "file_save.py"])
    # Wait for test1.py to finish
    test_process.wait()
    # Once test1.py is closed, execute check1.py
    subprocess.Popen(["python", "main_.py"])

# Run the test function
run_test()
