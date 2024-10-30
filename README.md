# system_info_report
The System Information Report Tool is a Python-based application designed to gather comprehensive details about the operating system and hardware configuration of the machine on which it runs. This tool collects essential system information, making it useful for system diagnostics, performance monitoring, and troubleshooting purposes.

Downloading the Tool
Ensure Git is Installed: Before cloning the repository, make sure you have Git installed on your system. You can check if Git is installed by running:

bash
Copier le code
git --version
If Git is not installed, you can install it using:

Debian/Ubuntu/Kali:
bash
Copier le code
sudo apt update
sudo apt install git
Windows: Download and install Git from git-scm.com.
macOS: Use Homebrew:
bash
Copier le code
brew install git
Clone the Repository: Open a terminal and run the following command to clone the repository:

bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/system_info_report.git
Navigate to the Directory: Change into the cloned directory:

bash
Copier le code
cd system_info_report
Install Required Library: Make sure you have the psutil library installed. You can install it using pip:

bash
Copier le code
pip install psutil
Using the Tool on Kali Linux
Open Terminal: Launch the terminal in Kali Linux.

Navigate to the Tool Directory: Use the cd command to go to the directory where the tool was cloned:

bash
Copier le code
cd ~/system_info_report
Run the Script: Execute the Python script to generate the system information report:

bash
Copier le code
python system_info_report.py
If you are using Python 3 specifically, you may need to run:

bash
Copier le code
python3 system_info_report.py
View the Report: After running the script, a text file named system_report.txt will be created on your Desktop. You can view it using a text editor or by running:

bash
Copier le code
cat ~/Desktop/system_report.txt
Additional Notes
Make sure you have Python installed on your system. You can check by running:

bash
Copier le code
python --version
If Python is not installed, you can install it using:

bash
Copier le code
sudo apt install python3
If you encounter permission issues, you may need to run the script with sudo:

bash
Copier le code
sudo python3 system_info_report.py
