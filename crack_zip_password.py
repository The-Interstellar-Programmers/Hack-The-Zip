import time
import zipfile
from tqdm import tqdm


wordList = input("Please provide the EXACT path to your desired word list (ex: /home/preso/wordlist.txt): \n")
zipFile = input("Now please provide the EXACT path to your zip file you want to acess (ex: /home/preso/file_to_acess): \n")

try:
    zipFile = zipfile.ZipFile(zipFile)
    nWords = len(list(open(wordList, "rb")))
except Exception as e:
    print("Error! Make sure to enter the paths correctly. (Exact error is below)\n \n")
    time.sleep(2.5)
    print(e)

print("\nPasswords to test: ", nWords, "password(s)\n")

with open(wordList, "rb") as wordList:
    for word in tqdm(wordList, total = nWords, unit = "word"):
        try:
            zipFile.extractall(pwd = word.strip())
        except:
            continue
        else:
            time.sleep(1)
            print("\n Password found: ", word.decode().strip())
            exit(0)
