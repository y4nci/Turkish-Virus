import ctypes
import os

error = "Hi, I am a Turkish virus but because of poor technology in my country unfortunately " + \
                "I am not able to harm your computer. Please be so kind to delete one of your important " + \
                "files yourself and then forward me to other users. Many thanks for your cooperation! Best " + \
                "regards, Turkish Virus."

ctypes.windll.user32.MessageBoxW(0, error, "Virus Error!", 4)

i = 0

while i < 32:

    cwd = os.getcwd()
    path = os.path.join(cwd, "TÜRKLER GELİYOR")
    os.makedirs(path)
    os.chdir(path)

    i += 1

file = open("TÜRKLER GELDİ.txt", "w", encoding="utf-8")
file.write("TÜRKLER GİDİYOR")
file.close()

