# Zamunda Book Downloader

## Overview

Zamunda Book Downloader is a Python script designed to simplify the process of downloading books from the Zamunda website. By providing a starting URL, the script will systematically download all books in Bulgarian language from the specified page number until it reaches the beginning of the catalog.

## Features

- **Easy to Use**: Simply provide the starting URL, and the script will handle the rest.
- **Language Filter**: Downloads only books in Bulgarian language.
- **Sequential Download**: Downloads books from the specified page number until the first page.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ceo-py/Book-Downloader-Zamunda.git
   cd zamunda-book-downloader
   
2. **Install Requirements:**
    ```bash
   pip install -r requirements.txt

3. **Configure Your Credentials:**
Open the script zamunda_downloader.py and set your Zamunda username and password:
    ```bash
   username = 'YOUR_USERNAME'
   password = 'YOUR_PASSWORD'

4. **Set the Starting Page:**
Open the script zamunda_downloader.py and set your starting page:
    ```bash
   page = 34

5. **Set the WebDriver:**
Open the script zamunda_downloader.py and set your path to the webdriver:
    ```bash
   PATH = r"YOUR PATH TO CHROME DRIVER"
   

6. **Run the Script:**
The script will systematically download all Bulgarian books starting from the specified page until it reaches the first page.
    ```bash
   python zamunda_downloader.py
   
