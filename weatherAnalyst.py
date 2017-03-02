##IMPORT MAIN LIBARIES
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#%matplotlib inline

## MAIN FUNCTION DEFINITIONS

def def_dataset():
    while True:
        choose_dataFlag = input("Which Dataset do you want to import? \n1: Satellite\n2: CF  ")
        if choose_dataFlag == "1":
            Datasetname = "Satellite_Data"
            print("Which cheese do you use to attract a bear? Camembert!\n proceeding with satellite dataset.")
            return int(choose_dataFlag)
        elif choose_dataFlag == "2":
            Datasetname = "/datadownload_CF"
            print("Which cheese do you use to hide a small pony? Mascarpone!\n proceeding with CF_Card data.")
            return int(choose_dataFlag)
        else:
            print("No!")

def def_station():
    while True:
        choose_flag = input("Which Station do you want to import ?\n1: Tueb\n2: Azucar\n3: Santa Gracia\n4: La Campana\n5: Nahuelbuta\n")
        if choose_flag == "1":
            stationName = "Tuebingen_Station"
            print(stationName)
            folder = "2104_Tue"
            folderCf1 = ""

            return int(choose_flag), folder, folderCf, stationName
            break
        elif choose_flag == "2":
            stationName = "Azucar_Station"
            print(stationName)
            folder = "2102_PdA"
            folderCf = "PdA/160405_161108_modified_ascii/TOA5_PanDeAzucar.SaveFull.csv"
            return int(choose_flag), folder, folderCf, stationName
            break
        elif choose_flag == "3":
            stationName = "Santa_Gracia_Station"
            print(stationName)
            folder = "2101_SG"
            folderCf = "SG/160401_161110_modified_ascii/TOA5_SantaGracia.SaveFull.csv"
            return int(choose_flag), folder, folderCf, stationName
            break
        elif choose_flag == "4":
            stationName = "La_Campana_Station"
            print(stationName)
            folder = "2103_LC"
            folderCf = "LC/160407_161114_modified_ascii/TOA5_LaCampana.SaveFull.csv"
            return int(choose_flag), folder, folderCf, stationName
            break
        elif choose_flag == "5":
            stationName = "Nahuelbuta_Station"
            print(stationName)
            folder = "2100_Na"
            folderCf = "Na/160327_161104_modified_ascii/TOA5_Nahuelbuta.SaveFull.csv"
            return int(choose_flag), folder, folderCf, stationName
            break
        else:
            print("Kirstin. I don't understand what you want. Type a number between 1 and 5")

def def_intervalFlag():
    while True:
        intInputString = ("Do you want to look at data from the last few weeks or in a specific time interval?\n1. Last few days\n2. specific interval\n")
        interval_flag = input(intInputString)
        if interval_flag == "1":
            return int(interval_flag)
            break
        elif interval_flag == "2":
            return int(interval_flag)
            break
        else:
            print("Kirstin. I only understand the numbers I show you")

def defineTimeInterval():
    print("Choose a interval: ")
    print("")
    startDate = input("Start Date (Format: YEAR-MONTH-DAY HH:MM:SS) : ")
    endDate = input("End Date (Format : YEAR-MONTH-DAY HH:MM:SS) :")
    return startDate, endDate

def defineDaysBack():
    while True:
        daysDiffInt = int(input("How many days of data do you want to look at?"))
        daysDiff = datetime.timedelta(days=daysDiffInt)
        today = datetime.datetime.today()
        today.strftime("%Y-%m-%d 00:00:00")
        daysBack = today - daysDiff
        startDate = daysBack.strftime("%Y-%m-%d 00:00:00")
        endDate = today.strftime("%Y-%m-%d 00:00:00")

        if isinstance(daysDiffInt, int) == True:
            break
        else:
            print("this was not a number...")

    return startDate, endDate
