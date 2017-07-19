import websocket
import json
import requests

#zone_id = os.getenv('TS_PREDIX_ZONE_ID')
#query_url = os.getenv('TS_QUERY_URL')

team_name = "JustDoIt"
turbine_id = '1'
sensor_type = 'temperature'

name = team_name + "-" + turbine_id + "-" + sensor_type

#zone_id = 'd97f5953-2c07-4e8f-ac0d-8b8df897135e'
zone_id = 'd702c860-64ae-4e32-8698-555b85f4fa8c'
#query_url = 'https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints/latest'
query_url = 'https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints'


''''
uaa_headers = {
    'content-type': "application/x-www-form-urlencoded",
    'authorization': 'Basic dHMtY2xpZW50MTpLZld1cHhTd001Q1hmaDg='

    }
'''
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1ZDM5YmZmYzI5ZjY0MDBhYWNmYmE3MjIwZjVkY2YzMCIsInN1YiI6ImpkaS1jbGllbnQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmQ3MDJjODYwLTY0YWUtNGUzMi04Njk4LTU1NWI4NWY0ZmE4Yy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZDcwMmM4NjAtNjRhZS00ZTMyLTg2OTgtNTU1Yjg1ZjRmYThjLnVzZXIiLCJ1YWEubm9uZSIsInRpbWVzZXJpZXMuem9uZXMuZDcwMmM4NjAtNjRhZS00ZTMyLTg2OTgtNTU1Yjg1ZjRmYThjLmluZ2VzdCJdLCJjbGllbnRfaWQiOiJqZGktY2xpZW50IiwiY2lkIjoiamRpLWNsaWVudCIsImF6cCI6ImpkaS1jbGllbnQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjZkYzM2NjY2IiwiaWF0IjoxNTAwNDg0Njk4LCJleHAiOjE1MDA1Mjc4OTgsImlzcyI6Imh0dHBzOi8vYzBjNTAzNjQtM2EyMS00YjI2LWIwOGYtMjIyZjBjMmQxZGNkLnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiYzBjNTAzNjQtM2EyMS00YjI2LWIwOGYtMjIyZjBjMmQxZGNkIiwiYXVkIjpbImpkaS1jbGllbnQiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ3MDJjODYwLTY0YWUtNGUzMi04Njk4LTU1NWI4NWY0ZmE4YyJdfQ.ooeweSRC5H2tFFpBDIU5p16yeQkM8wausqe72SVCBZp4ZtpcR3jdVqnRbxfQ4f5x_u9EngMOBkD57rr5JoRgKD9IoBFP8rYMxl6L3z2w8hlXvEvQHkB8YnoBCn3zP5D3mt1NNUDpQSsD2wTGduGv6AFLzf7nybdqso0-fbiBsYBZ1lOISXhlfeoKpjHsQ_Y7duzBWWYMY5CL-KWaLdWaLOU0iDkeuKmQKzkhKRSzADqdo7dSILvJeAOhGwxc-0u7cQ1rUO3nf_3BTr24Lpvg5z1Kwgn1r6sUjotqKxlDfRDBRJRQ5lESvlzwuI2mQ-BmpgTDx_TJc3o6E0xqVf_qRg',
    #'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiIzMTA1ZjdlM2MyNzY0YWUxOTZjZWE3OThhYTZlNjA0NyIsInN1YiI6InRzLWNsaWVudDEiLCJzY29wZSI6WyJ1YWEucmVzb3VyY2UiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5pbmdlc3QiLCJ1YWEubm9uZSIsInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlLnVzZXIiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5xdWVyeSJdLCJjbGllbnRfaWQiOiJ0cy1jbGllbnQxIiwiY2lkIjoidHMtY2xpZW50MSIsImF6cCI6InRzLWNsaWVudDEiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlkYWMxM2ZmIiwiaWF0IjoxNTAwNDA2MjQ3LCJleHAiOjE1MDE0NTc0NDcsImlzcyI6Imh0dHBzOi8vZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkLnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkIiwiYXVkIjpbInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlIiwidWFhIiwidHMtY2xpZW50MSJdfQ.P7hGLLF6qUU_5h2GUStlCQWN25DD2rIu2LBkxH-hHWM60Cy6ILSNlc5IHqM2Mc_7llI-uP1geLq6kduo4Ks-dBLNMTq6BrACvaUUYDhAjIfsAkJRx5idKhJVgru-VHY-X9Tk0loziw3ldTk3GaB4hQSoDLyWGrALM5M3bnLE8ImhCAkYkVEbWT1oHFAWffWLkKxfSDyVfZ-myE-hPmxL_ga6AJOb85O8FjLvygg4jdYlL26s80zzyJXofRbNiNSDjaeELgiy_zXd2B1vFyofXm90q4iNLp-BQXqqSK4WHvBHKcClHSn7GaCiDPqYJZK-MPIej03_xJpLRxvMJKY6Jw',
    'Predix-Zone-Id': zone_id
}
body = {
    "start": "24h-ago",
    "end": "10s-ago",
    "tags": [
        {
            "name":  [name]
        }
    ]
}
response = requests.post(query_url, headers=headers, data=json.dumps(body))
#results = response.json()['stats']
print response.text
#print results