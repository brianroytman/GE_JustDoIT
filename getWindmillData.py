import urllib2, json
import time
import traceback
import datetime

class Turbine :

    def __init__(self, id):
        self.id = id
        self.temp = ""
        self.voltage = ""

def get_data(requestString):

    try:
        data = json.loads(urllib2.urlopen(requestString).read())
        timestamp = data["timestamp"]
        
        #convert timestamp to milliseconds then round up

        #time_ms = time.gmtime(timestamp/1000.)

        #int(time.time() * 1000)

        #time_ms = timestamp * 1000
        time_ms = int(time.time() * 1000)

        #print requestString
        #print "ok"
        #print time_ms

        value =  data["value"]
        quality = 3

        finalData = [
            time_ms,
            value,
            quality
        ]
    
        return finalData
        
    except:
        return "NULL"


def main():
    api_root="https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/"
    temperature_url="/sensors/temperature"
    voltage_url="/sensors/voltage"
    max_turbines=3

    '''
    headers = {
        'cache-control': "no-cache",
        'postman-token': "d92739a6-1a81-ff72-7ef3-7e43aca7c1fe"
    }
    '''
    '''
    while(1):
        for x in range (1,max_turbines+1):
            #turbine = Turbine(x)
            voltage_string=api_root + str(x) + voltage_url
            temperature_string=api_root + str(x) + temperature_url
        
            
            turb_temp_val = str(get_data(temperature_string))
            turb_volt_val = str(get_data(voltage_string))
            print "Turbine " + str(x) + ": [Temperature = " + turb_temp_val  + ", Voltage = " + turb_volt_val + "]"

        time.sleep(10)

    '''

    #Create a list of lists
    # [[timestamp, temp/voltage value, quality]]
    dataList = []

    while(1):
        for x in range (1,max_turbines+1):
            #turbine = Turbine(x)
            
            voltage_string=api_root + str(x) + voltage_url
            temperature_string=api_root + str(x) + temperature_url
        
            
            
            
            #turb_temp_val = str(get_data(temperature_string))
            print temperature_string
            turb_temp_val = get_data(temperature_string)
            
            #turb_volt_val = str(get_data(voltage_string))

            print turb_temp_val
            dataList.append(turb_temp_val)
            
            #print "Turbine " + str(x) + ": [Temperature = " + turb_temp_val  + ", Voltage = " + turb_volt_val + "]"

        time.sleep(1)


if __name__ == "__main__":
    main()