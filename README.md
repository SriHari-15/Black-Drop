# Black Drop

- A simple file sharing server to transfer files from PC to any other device on the local network
- It is written in **Python** and uses Flask to run the server
- Add the files to the `files` directory

![](https://i.imgur.com/19B74ii.png)

## Features

- Files hosted are in the Windows Explorer Details view
- The page auto refreshes and auto updates when new files are added or removed from the `files` directory
- Black and Orange minimalist theme

## Requirements
- Python
- Flask
- Flask Socket IO
- Watchdog
```
pip install flask flask_socketio watchdog
```

## Usage

- Clone this repo
- Run app.py to start the server
```
py app.py
```
-   Flask will show your local ip address in the terminal, however you can run `ipconfig` to get your active local IPv4 address
-   Open a browser in your phone or any other device and enter `<your local IPv4>:5000` and download the files in `files` direcrory
- **Note:** The port is set to `5000` by default in `app.py`. If you want to change it, modify the last line in `app.py` to any other port you want.

----
✌️Sri Hari
