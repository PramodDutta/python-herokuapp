##!/use/bin/env python
import time
import requests
import urllib.request
import os
import urllib

genreList = ['Action', 'Adventure', 'Animation', 'Biography',
             'Comedy', 'Crime', 'Documentary', 'Drama', 'FamilyFantasy',
             'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
             'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getMovies(g, r, p):
    responeData = requests.get(
        "https://yts.to/api/v2/list_movies.json?page=1" + "minimum_rating=" + r + "&quality=" + p + "&limit=50&genre=" + g)
    print("Number of Results : - " + str(responeData.json()['data']['limit']))
    print(bcolors.BOLD+" |   Title  |   Seeds   |   Peers   |   Size    |   "+bcolors.ENDC)
    for i in range(1, 50):
        titleOfTorrent = str(responeData.json()['data']['movies'][i]['title_long'])
        noofseeds = str(responeData.json()['data']['movies'][i]['torrents'][0]['seeds'])
        noofpeers = str(responeData.json()['data']['movies'][i]['torrents'][0]['peers'])
        size = str(responeData.json()['data']['movies'][i]['torrents'][0]['size'])
        if p == "720p":
            urlOfTorrent = str(responeData.json()['data']['movies'][i]['torrents'][0]['url'])
        else:
            urlOfTorrent = str(responeData.json()['data']['movies'][i]['torrents'][0]['url'])
        print(" | "+titleOfTorrent+"| "+noofseeds+" | "+noofpeers+" | "+size+" | ")
        downLoadTorrent(urlOfTorrent, titleOfTorrent)


def main():
    print(bcolors.WARNING+"*** Welcomoe to Yify Movies Downloader ***"+bcolors.ENDC)
    print(bcolors.OKGREEN+"Enter the Genre and Rating Score from below List"+bcolors.ENDC)
    for l in genreList:
        print(" "+bcolors.OKBLUE+l+'\b', end="||"+bcolors.ENDC)

    print('\n')
    inputGenre = input("Enter the Genre:- ")
    inputRating = input("Enter the Rating:- ")
    inputPiexel = input("Enter 720p or 1080p:- ")
    getMovies(inputGenre, inputRating, inputPiexel)


def downLoadTorrent(url, mytitle):
    testfile = urllib.request.URLopener()
    dirname = os.path.dirname(os.path.abspath(__file__))
    testfile.retrieve(url, str(dirname+'\\'+mytitle+".torrent"))
    file = str(mytitle+".torrent")
    os.startfile(file)
    time.sleep(2)

if __name__ == "__main__":
        main()
