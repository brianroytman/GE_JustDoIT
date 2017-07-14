import urllib2, json
import time
import traceback

class Turbine :
    def __init__(self, id):
        self.id = id
        self.temp = ""
        self.voltage = ""

def get_data(requestString):

    try:
        data = json.loads(urllib2.urlopen(requestString).read())
        return data["value"]
        
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

    while(1):
        for x in range (1,max_turbines+1):
            #turbine = Turbine(x)
            voltage_string=api_root + str(x) + voltage_url
            temperature_string=api_root + str(x) + temperature_url
          
            
            turb_temp_val = str(get_data(temperature_string))
            turb_volt_val = str(get_data(voltage_string))
            print "Turbine " + str(x) + ": [Temperature = " + turb_temp_val  + ", Voltage = " + turb_volt_val + "]"

        time.sleep(10)

if __name__ == "__main__":
    main()