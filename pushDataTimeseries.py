import websocket
import json
import time
import getWindmillData

api_root = "https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/"
temperature_url = "/sensors/temperature"
voltage_url = "/sensors/voltage"
heartbeat_url = "/sensors/heartbeat"
max_turbines = 3


team_name = "JustDoIt"
#sensor_type_temp = 'temp'
#sensor_type_voltage = 'volt'
#sensor_type_heartbeat = 'eartbeat'



zone_id = 'd702c860-64ae-4e32-8698-555b85f4fa8c'
ingestion_url = 'wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
uaa_header = 'Basic amRpLWNsaWVudDpqZGktc2VjcmV0'
access_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1ZDM5YmZmYzI5ZjY0MDBhYWNmYmE3MjIwZjVkY2YzMCIsInN1YiI6ImpkaS1jbGllbnQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmQ3MDJjODYwLTY0YWUtNGUzMi04Njk4LTU1NWI4NWY0ZmE4Yy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZDcwMmM4NjAtNjRhZS00ZTMyLTg2OTgtNTU1Yjg1ZjRmYThjLnVzZXIiLCJ1YWEubm9uZSIsInRpbWVzZXJpZXMuem9uZXMuZDcwMmM4NjAtNjRhZS00ZTMyLTg2OTgtNTU1Yjg1ZjRmYThjLmluZ2VzdCJdLCJjbGllbnRfaWQiOiJqZGktY2xpZW50IiwiY2lkIjoiamRpLWNsaWVudCIsImF6cCI6ImpkaS1jbGllbnQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjZkYzM2NjY2IiwiaWF0IjoxNTAwNDg0Njk4LCJleHAiOjE1MDA1Mjc4OTgsImlzcyI6Imh0dHBzOi8vYzBjNTAzNjQtM2EyMS00YjI2LWIwOGYtMjIyZjBjMmQxZGNkLnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiYzBjNTAzNjQtM2EyMS00YjI2LWIwOGYtMjIyZjBjMmQxZGNkIiwiYXVkIjpbImpkaS1jbGllbnQiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ3MDJjODYwLTY0YWUtNGUzMi04Njk4LTU1NWI4NWY0ZmE4YyJdfQ.ooeweSRC5H2tFFpBDIU5p16yeQkM8wausqe72SVCBZp4ZtpcR3jdVqnRbxfQ4f5x_u9EngMOBkD57rr5JoRgKD9IoBFP8rYMxl6L3z2w8hlXvEvQHkB8YnoBCn3zP5D3mt1NNUDpQSsD2wTGduGv6AFLzf7nybdqso0-fbiBsYBZ1lOISXhlfeoKpjHsQ_Y7duzBWWYMY5CL-KWaLdWaLOU0iDkeuKmQKzkhKRSzADqdo7dSILvJeAOhGwxc-0u7cQ1rUO3nf_3BTr24Lpvg5z1Kwgn1r6sUjotqKxlDfRDBRJRQ5lESvlzwuI2mQ-BmpgTDx_TJc3o6E0xqVf_qRg'

dataListTemp = []
dataListVolt = []
dataListHeartbeat = []

max_sensors = 3
sensors = ["temperature", "voltage", "heartbeat"]


def pushData(turbineData, turbine_id, sensor_type):
    name = team_name + "-" + str(turbine_id) + "-" + sensor_type
    print name

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Predix-Zone-Id': zone_id,
        'Content-Type': 'application/json',
    }
    message = {
        "messageId": 'predixguy-CURRENTTIME',
        "body": [
            {
                "name": name,
                "datapoints": turbineData
            }
        ]
    }

    ws = websocket.create_connection(ingestion_url, header=headers)
    ws.send(json.dumps(message))
    result = ws.recv()
    print('Got back message confirmation TimeSeries:\n %s' % result)

while(1):
    for turbId in range (1,max_turbines+1):
        temperature_string = api_root + str(turbId) + temperature_url
        voltage_string = api_root + str(turbId) + voltage_url
        heartbeat_string = api_root + str(turbId) + heartbeat_url

        for sensor_index in range(0, max_sensors):
            if sensors[sensor_index] == "temperature":

                temp_data = getWindmillData.get_data(temperature_string)
                #dataListTemp.clear()

                del dataListTemp[:]

                dataListTemp.append(temp_data)
                
                print dataListTemp

                pushData(dataListTemp, turbId, sensors[sensor_index])

            elif sensors[sensor_index] == "voltage":

                voltage_data = getWindmillData.get_data(voltage_string)
                #dataList.insert(0, voltage_data) #= voltage_data

                #dataListVolt.clear()

                del dataListVolt[:]
                
                dataListVolt.append(voltage_data)

                print dataListVolt

                pushData(dataListVolt, turbId, sensors[sensor_index])

            else:

                heartbeat_data = getWindmillData.get_data(heartbeat_url)
                #dataList[0, heartbeat_data] #= heartbeat_data
                #dataListHeartbeat.clear()

                del dataListHeartbeat[:]

                dataListHeartbeat.append(heartbeat_data)



                print dataListHeartbeat

                pushData(dataListHeartbeat, turbId, sensors[sensor_index])



    time.sleep(5)


#write the timestamp in milliseconds and round
