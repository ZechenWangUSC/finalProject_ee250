from influxdb import InfluxDBClient
from datetime import datetime
import time

client = InfluxDBClient(addr, 8086, 'admin', 'password', db)

def init(addr,db):
	#client = InfluxDBClient(addr, 8086, 'admin', 'password', db)
	client.create_database('project')

def send(measure,value):

	curr_time = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ');

	json_body = [
	    {
	        "measurement": measure,
	        "tags": {
	            "host": "Device1",
	        },
	        "time": curr_time,
	        "fields": {
	            "value": value
	        }
	    }
	]	
	client.write_points(json_body)
	#result = client.query('select value from Distance;')
	#print("Result: {0}".format(result))
