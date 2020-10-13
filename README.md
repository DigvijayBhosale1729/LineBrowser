## LineBrowser
LineBrowser is a command line tool that utilizes an installed browser to automate the process of searching, or searching and clicking in a easy and user friendly way

# Installation for Linux users

       git clone https://github.com/FoxSinOfGreed1729/LineBrowser.git
       cd LineBrowser
       pip install -r requirements.txt
       
# Installation for Windows users

       git clone https://github.com/FoxSinOfGreed1729/LineBrowser.git   Usage: python3 browser.py [options] argument use -h for help

Options:
  -h, --help     show this help message and exit
  -u WEBSITE     Specify url of website you want to browse
  -t ITYPE       Specify the type of identifier you want to use to search 1
                 for ID, 2 for Link Text, 3 for Name, 4 for Tag Name, 5 for
                 Xpath
  -i IDENTIFIER  Specify the identifier you want to use for searching
  -m UINPUT      Specify the text you want to input into the search field
  -c CLICKER     Specify link text you want to click after searching
       dir LineBrowser
       pip install -r requirements.txt
       
If Pip is not installed, install it using 

    pip install pip

# How to use the tool

    Usage: python3 browser.py [options] argument use -h for help

    Options:
      -h, --help     show this help message and exit
      -u WEBSITE     Specify url of website you want to browse
      -t ITYPE       Specify the type of identifier you want to use to search 1
                     for ID, 2 for Link Text, 3 for Name, 4 for Tag Name, 5 for
                     Xpath
      -i IDENTIFIER  Specify the identifier you want to use for searching
      -m UINPUT      Specify the text you want to input into the search field
      -c CLICKER     Specify link text you want to click after searching
      
# Indivisual options explained

      -u WEBSITE     Specify url of website you want to browse
The Website should be in quotation marks

      -t ITYPE       Specify the type of identifier you want to use to search 1
                     for ID, 2 for Link Text, 3 for Name, 4 for Tag Name, 5 for
                     Xpath
The type needs to be selected from the html page of the site you want to visit.
This can be done by pressing Ctrl+Shift+C on the keyboard while using the browser,
Or alternatively, you can also right click and click on inspect element

      -i IDENTIFIER  Specify the identifier you want to use for searching
The identifier you want to use (ID, name, etc) should be in quotations

      -m UINPUT      Specify the text you want to input into the search field
The input you want to enter into the search bar should be in quotations as well

      -c CLICKER     Specify link text you want to click after searching
This is the link that LineBrowser will click. 
Note that this is the link text, not the link URL
This too has to be in quotation marks.

# Requirements
LineBrowser currently uses only Mozilla Firefox with a version higher than 79.0
Hence, update your browser to the latest version to avoid any bugs.

LineBrowser wil shortly be available for Google Chrome as well
