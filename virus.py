# -*- coding: utf-8 -*-
"""Virus.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NWJF4UiXRX6bJ8W3-wndBP5-y_8Jtekj
"""

import os

def simulate_virus(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write("\nThis file has been infected by a simulated virus!")

if __name__ == "__main__":
    file_to_infect = "example.txt"
    simulate_virus(file_to_infect)
    print(f"Simulated virus has modified {file_to_infect}.")

import os

def simulate_antivirus(file_path: str, backup_file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(backup_file_path):
        os.rename(backup_file_path, file_path)
    print(f"{file_path} has been restored to its original state.")

if __name__ == "__main__":
    infected_file = "example.txt"
    backup_file = "example_backup.txt"

    simulate_antivirus(infected_file, backup_file)