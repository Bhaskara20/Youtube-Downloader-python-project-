import sys
import youtube_dl

download= {}
def downloader_funct():
    with youtube_dl.YoutubeDL(download) as dwnld:
        dwnld.download([dld])


opsi="y"
print("=======================================================\n\n")
print("    SELAMAT DATANG DI PROGRAM YT DOWNLOADER ANDRU\n\n")
print("=======================================================\n")

while opsi=="y":
    link=input("Masukan link youtube : ")
    dld=link.strip()
    downloader_funct()
    opsi=input("Mau download video lain? [y/n] : ")
    if opsi=="n":
        print("=======================================================\n\n")
        print("       Terimakasih telah menggunakan jasa kami\n")
        print("=======================================================\n")
        sys.exit()




