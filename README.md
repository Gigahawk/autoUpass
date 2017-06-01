Dependencies:
- Python - Tested working on Python 3.x, I'm pretty sure there are issues with Python 2.x
- Selenium - Interface for browser automation
- PhantomJS - Technically you can use any browser that webdriver that selenium supports but PhantomJS will usually be faster because it is headless  

Installation:
- Install dependencies (instructions for everything can be found online)
- Place autoUpass.py and uPassMail.py somewhere on your machine and make it executable
- Replace variables in autoUpass.py with your CWL login credentials (yes you're storing your CWL password in plaintext, but I don't think the CWL api is open source and quite frankly couldnt be bothered to figure it out anyways)
- Replace variables in uPassMail.py with some gmail login credentials as well as an address to recieve notifications (I would HIGHLY recommend using a throwaway email as the sender)
- Set it to run every month from crontab (use google to find out how to run things from crontab)

Notes:
- This scipt designed for use with UBC CWL accounts, although realistically it could be adapted for any other institution simply by changing the elements that it searches for on the login page.
