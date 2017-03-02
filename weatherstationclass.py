from weatherAnalyst import *

class weatherstation():
    def __init__(self):
        self.name = ""
        self.timest = ""
        self.foldstrg = ""
        self.foldcfstr = ""

    def whichDataset(self):
        self.dataFlag = def_dataset()

    def which_station(self):
        self.flag, self.statstrg,self.statcfstrg, self.statName = def_station()
        if self.dataFlag == 1:
            self.foldstrg = str(self.statstrg + "/all_data_multiple.csv")
        elif self.dataFlag == 2:
            self.foldstrg = "datadownload_CF/" + str(self.statcfstrg)
        else:
            print("Ooops. Something went wrong. Fucking Manu!")

    def time_interval(self):
        self.time_flag = def_intervalFlag()
        if self.time_flag == 1:
            self.sd, self.ed = defineDaysBack()
            self.open_csv_interval()
        elif self.time_flag == 2:
            self.sd, self.ed = defineTimeInterval()
            self.open_csv_interval()

    def open_csv_interval(self):
        print("Opening the CSV File. This might take a little moment.")
        print("")
        if self.dataFlag == 1:
            self.df = pd.read_csv(self.foldstrg, names = ['Timestamp',
                                                'StationName',
                                                'AirTemp',
                                                'AirRelHum',
                                                'SolarRad',
                                                'SoilWat',
                                                'SoilTe',
                                                'WindSpeed',
                                                'WindMax',
                                                'WindDir',
                                                'Precip',
                                                'AirPres'],
                                                 sep=",",
                                                 parse_dates=['Timestamp'],
                                                 header=0,
                                                 index_col=['Timestamp'])
            #Replace all the ' None' Strings with Nan
            self.df = self.df.replace([' None'], np.nan)
            #df.ix[self.sd : self.ed]
        elif self.dataFlag == 2:
            if self.flag == 5:
                self.df = pd.read_csv(self.foldstrg, sep="," ,
                                                    header = 3,
                                                    index_col=['TIMESTAMP'],
                                                    names = [
                                                    'TIMESTAMP',
                                                    'RECORD',
                                                    'BattV_Avg',
                                                    'PTemp_C_Avg',
                                                    'AirTC_Avg',
                                                    'RH',
                                                    'SlrW_Avg',
                                                    'SlrMJ_Tot',
                                                    'VWC_Avg',
                                                    'GrTemp_Avg',
                                                    'EC_Avg',
                                                    'P_Avg',
                                                    'PA_Avg',
                                                    'VR_Avg',
                                                    'WS_ms_Avg',
                                                    'WS_ms_max',
                                                    'WS_ms_min',
                                                    'WindDir_Avg',
                                                    'WS_ms_S_WVT',
                                                    'WindDir_D1_WVT',
                                                    'Rain_mm_Tot',
                                                    'BP_mbar_Avg'],
                                                    parse_dates=['TIMESTAMP'])
            else:
                self.df = pd.read_csv(self.foldstrg, sep="," ,
                                                    header = 3,
                                                    index_col=['TIMESTAMP'],
                                                    names = [
                                                    'TIMESTAMP',
                                                    'RECORD',
                                                    'BattV_Avg',
                                                    'PTemp_C_Avg',
                                                    'AirTC_Avg',
                                                    'RH',
                                                    'PVap_Avg',
                                                    'SlrW_Avg',
                                                    'SlrMJ_Tot',
                                                    'VWC_Avg',
                                                    'GrTemp_Avg',
                                                    'EC_Avg',
                                                    'P_Avg',
                                                    'PA_Avg',
                                                    'VR_Avg',
                                                    'WS_ms_Avg',
                                                    'WS_ms_max',
                                                    'WS_ms_min',
                                                    'WindDir_Avg',
                                                    'WS_ms_S_WVT',
                                                    'WindDir_D1_WVT',
                                                    'Rain_mm_Tot',
                                                    'BP_mbar_Avg'],
                                                    parse_dates=['TIMESTAMP'])
            #self.df = self.df.drop(self.df.index[[0,1]])
            self.df.index = pd.to_datetime(self.df.index)
            self.df = self.df.replace([' None'], np.nan)
            self.df = self.df.replace(['NAN'], np.nan)
            self.df = self.df.replace(['"NAN"'], np.nan)

    def checkPrintFlag(self):
        if self.dataFlag == 1:
        #checks print flag and adjusts the printStr which is passed to print command
            while True:
                #Asks the user which value he wants to print
                self.printFlag = input("Which Value do you want to print ?\n1.Air Temperature\n2.Air Relative Humidity\n3.Solar Radiation\n4.Soil Water Content\n5.Soil Temperature\n6.Wind Speed\n7.Wind Maximum Speed\n8.Wind Direction\n9.Precipitation\n10.Air Pressure\n")
                if self.printFlag == "1":
                    print('Printing air temperature.')
                    self.printStr = "AirTemp"
                    self.labelStr = "Air temperature °C"
                    break
                elif self.printFlag == "2":
                    print('Printing relative air humidity.')
                    self.printStr = "AirRelHum"
                    self.labelStr = "Air relative humidity"
                    break
                elif self.printFlag == "3":
                    print('Printing solar radiation')
                    self.printStr = "SolarRad"
                    self.labelStr = "Solar Radiation"
                    break
                elif self.printFlag == "4":
                    print('Printing soil water content')
                    self.printStr = "SoilWat"
                    self.labelStr = "Soil water content"
                    break
                elif self.printFlag == "5":
                    print('Printing soil temperature')
                    self.printStr = "SoilTe"
                    self.labelStr = "Soil Temperature °C" + '.png'
                    break
                elif self.printFlag == "6":
                    print('Printing wind speed')
                    self.printStr = "WindSpeed"
                    self.labelStr = "Wind speed Km/h"
                    break
                elif self.printFlag == "7":
                    print('Printing maximum wind speed.')
                    self.printStr = "WindMax"
                    self.labelStr = "Wind maximum speed Km/h"
                    break
                elif self.printFlag == "8":
                    print('Printing wind direction')
                    self.printStr = "WindDir"
                    self.labelStr = "Wind direction"
                    break
                elif self.printFlag == "9":
                    print('Printing precipitation')
                    self.printStr = "Precip"
                    self.labelStr = "Precipitation"
                    break
                elif self.printFlag == "10":
                    print('Printing airpressure')
                    self.printStr = "AirPres"
                    self.labelStr = "Air pressure"
                    break
                elif self.printFlag == "11":
                    print('Printing PVap_Avg. Whatever')
                    self.printStr = "PVap_Avg"
                    self.labelStr = "PVap_Avg"
                else:
                    print('I could not understand that.')

        elif self.dataFlag == 2:
            while True:
                self.printFlag = input("Which Value do you want to print ?\n"+
                                                "1. BattV_Avg\n"+
                                                "2. PTemp_C_Avg\n"+
                                                "3. AirTC_Avg\n"+
                                                "4. RH\n"+
                                                "5. SlrW_Avg\n"+
                                                "6. SlrMJ_Tot\n"+
                                                "7. VWC_Avg\n"+
                                                "8. GrTemp_Avg\n"+
                                                "9. EC_Avg\n"+
                                                "10. P_Avg\n"+
                                                "11. PA_Avg\n"+
                                                "12. VR_Avg\n"+
                                                "13. WS_ms_Avg\n"+
                                                "14. WS_ms_max\n"+
                                                "15. WS_ms_min\n"+
                                                "16. WindDir_Avg\n"+
                                                "17. WS_ms_S_WVT\n"+
                                                "18. WindDir_D1_WVT\n"+
                                                "19. Rain_mm_Tot\n"+
                                                "20. BP_mbar_Avg\n")
                if self.printFlag == "1":
                    print('Printing average battery voltage.')
                    self.printStr = "BattV_Avg"
                    self.labelStr = "Average Battery Voltage (V)"
                    break
                elif self.printFlag == "2":
                    print('Printing soil temperatue average')
                    self.printStr = "PTemp_C_Avg"
                    self.labelStr = "Average Panel Temperature °C"
                    break
                elif self.printFlag == "3":
                    print('Printing average air temperature')
                    self.printStr = "AirTC_Avg"
                    self.labelStr = "Average Air Temperature °C"
                    break
                elif self.printFlag == "4":
                    print('Printing soil water content')
                    self.printStr = "RH"
                    self.labelStr = "Relative Humidity"
                    break
                elif self.printFlag == "5":
                    print('Printing average solar radiation in W')
                    self.printStr = "SlrW_Avg"
                    self.labelStr = "Average Solar Radiation W/m^2"
                    break
                elif self.printFlag == "6":
                    print('Printing wind speed')
                    self.printStr = "SlrMJ_Tot"
                    self.labelStr = "Average Solar Radiation MJ/m^2"
                    break
                elif self.printFlag == "7":
                    print('Printing volumetric water content')
                    self.printStr = "VWC_Avg"
                    self.labelStr = "Volumetric Water Content m^3/m^3"
                    break
                elif self.printFlag == "8":
                    print('Printing average ground temperature')
                    self.printStr = "GrTemp_Avg"
                    self.labelStr = "Average Ground Temperature °C"
                    break
                elif self.printFlag == "9":
                    print('Printing electric conductivity')
                    self.printStr = "EC_Avg"
                    self.labelStr = "Electric Conductivity dS/m"
                    break
                elif self.printFlag == "10":
                    print('Printing permeability')
                    self.printStr = "P_Avg"
                    self.labelStr = "Permeability"
                    break
                elif self.printFlag == "11":
                    print('printing period average. What the fuck?')
                    self.printStr = "PA_Avg"
                    self.labelStr = "PeriodAverageWhatisthis?"
                    break
                elif self.printFlag == "12":
                    print('printing voltage ratio')
                    self.printStr = "VR_Avg"
                    self.labelStr = "Voltage Ratio"
                    break
                elif self.printFlag == "13":
                    print("printing wind speed")
                    self.printStr = "WS_ms_Avg"
                    self.labelStr = "Wind Speed m/s"
                    break
                elif self.printFlag == "14":
                    print("printing wind speed ")
                    self.printStr = "WS_ms_max"
                    self.labelStr = "Wind Speed Maximum m/s"
                    break
                elif self.printFlag == "15":
                    print("printing minimum wind speed")
                    self.printStr = "WS_ms_min"
                    self.labelStr = "Minimum Wind Speed m/s"
                    break
                elif self.printFlag == "16":
                    print("printing average wind direction")
                    self.printStr = "WindDir_Avg"
                    self.labelStr = "Wind direction"
                    break
                elif self.printFlag == "17":
                    print("printing ")
                    self.printStr = "WS_ms_S_WVT"
                    self.labelStr = "SomethingSomething17"
                    break
                elif self.printFlag == "18":
                    print("printing wind direction")
                    self.printStr = "WindDir_D1_WVT"
                    self.labelStr = "WindDirection"
                    break
                elif self.printFlag == "19":
                    print("printing total rain mm")
                    self.printStr = "Rain_mm_Tot"
                    self.labelStr = "Total rain [mm]"
                    break
                elif self.printFlag == "20":
                    print("printing air pressure mbar")
                    self.printStr = "BP_mbar_Avg"
                    self.labelStr = "Air Pressure mbar"
                    break
                else:
                    print("Oops, something went wrong.")


    def printValues(self):
        #DEPRECATED: Moved to .csv import?
        #Checks the pandas database after NaN values
        #self.df[self.sd : self.ed][self.printStr][self.df[self.sd : self.ed][self.printStr] == ' None'] = np.nan
        #self.df[self.df == ' None'] = np.nan
        fig, ax = plt.subplots(figsize = [10,6])
        line = plt.plot(self.df[self.sd : self.ed][self.printStr],'r')
        minVal = min(pd.to_numeric(self.df[self.sd : self.ed][self.printStr]))
        maxVal = max(pd.to_numeric(self.df[self.sd : self.ed][self.printStr]))
        #plt.xlim()
        plt.ylim([minVal-3,maxVal+3])
        plt.title(self.statstrg + ' , ' + self.printStr)
        plt.ylabel(self.labelStr)
        if self.printFlag == "16" or "18":
            plt.yticks(np.arange(0,360,25))
            plt.ylim([0,360])

        plt.savefig(self.statName + '_' + self.printStr + '.png', dpi=720)
