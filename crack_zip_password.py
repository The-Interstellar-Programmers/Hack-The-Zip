import zipfile
import time
from tqdm import tqdm

#folder path must be changed
wordlist = r"C:\Users\Username\Desktop\ZipHack\rockyou.txt"
#Put the zipfile's name below. (Must be DIRECT PATH e.g. C:\Users\Username\Desktop\ZipHack\Payment.zip )
zip_file = r"C:\Users\Username\Desktop\ZipHack\Payment.zip"

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words, "word(s) (extracted from rockyou.txt)")

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            time.sleep(1)
            print("\n Password found:", word.decode().strip())
            exit(0)
print("Password not found... try other wordlists.")