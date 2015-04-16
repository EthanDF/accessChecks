##accessChecks.py
"""this is a script to check access against specific providers"""

import csv
# from bs4 import BeautifulSoup
import requests
import tkinter

root = tkinter.Tk()
root.withdraw()

resultsFile = 'c:\\users\\fenichele\\desktop\\resultsFile.csv'

def readTestList():
    """Read in list of SYS#s and URLs to Test"""

    # from tkinter import filedialog
    # checkFile = tkinter.filedialog.askopenfile()

    checkFile = 'c:\\users\\fenichele\\desktop\\degr.csv'
    # print(checkFile)
    accessCheckList = []

    with open(checkFile, 'r') as csvf:
        u = csv.reader(csvf)
        for row in u:
            accessCheckList.append(row)

    return accessCheckList

def writeResultLog(sysID,url,urlResult):
    import time
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    data = [[now,str(sysID),str(url),str(urlResult)]]
    print (data)
    # resultsFile = 'c:\\users\\fenichele\\desktop\\resultsFile.csv'
    with open(resultsFile, 'a', newline='') as out:
        a = csv.writer(out, delimiter=',', quoting=csv.QUOTE_ALL)
        a.writerows(data)


def degruyterCheckSite(url):
    """check's degruyters site based on URL provided for "Licensed Access"""
    dgtestPhrase = 'Licensed Access'
    dgtestPhrase2 = 'viewbooktoc'

    # urltoCheck = input("\n what is the URL? \n")

    urltoCheck = url

    r = requests.get(urltoCheck)
    rResult = r.text

    dgoutcome = 0
    if (dgtestPhrase in rResult) and (dgtestPhrase2 in rResult):
        dgoutcome = 1

    return dgoutcome

def deGruyter():

    checkList = readTestList()

    for a in checkList:
        sysID = a[0]
        url = a[1]

        urlResult = degruyterCheckSite(url)
        writeResultLog(sysID, url, urlResult)


deGruyter()

