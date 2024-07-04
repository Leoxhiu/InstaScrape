## Description
This is a simple python application mainly built with selenium library.

## Goal
Automate usernames scraping from target user's followers list.

## How to use?

### For Windows
1. Download [InstaScrape](https://github.com/Leoxhiu/InstaScrape/archive/refs/heads/main.zip)

2. Download [Python](https://www.python.org/downloads/)
   
3. Move your file to Desktop for easier configuration

4. Open .env with notepad

5. Adjust configuration in .env based on your preference, replace (_italic words_) directly
    - INSTA_USERNAME=_(your instagram username)_
    - INSTA_PASSWORD=_(your instagram password)_
    - TARGET_USER=_(url/link to the profile)_
    - ITERATION=_(number to scroll through the followers list)_
    - CHECKPOINT=_(store data after this number of scrolling)_

6. Launch CMD

7. Enter
   ```sh 
   cd Desktop/InstaScrape-main

9. Enter
   ```sh
   .\env\Scripts\activate

11. Enter
    ```sh
    pip install -r requirements.txt

13. Enter
    ```sh
    python main.py

15. The application is successfully launched!
    
16. For future launch, you can try to double click on **main.py**. If it's not working, enter:
    ```sh
    cd Desktop/InstaScrape-main
    .\env\Scripts\activate
    python main.py

### For MAC
Currently unavailable

## File description
### main.py
Main program file to be run.

### user.txt
The file to store the usernames.
