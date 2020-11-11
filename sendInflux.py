from influxdb import InfluxDBClient	#external library, detailes in README
from datetime import datetime

ADDR = '45.76.207.242' # The address of the Cloud Server

#create a database named 'project'
client = InfluxDBClient(ADDR, 8086, 'admin', 'password', 'project')
client.create_database('project')

#send data with two inputs: measurement and value
def send(measure,value):

	#generate current time for InfluxDB
	curr_time = datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ');

	#generate formatted json
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
	
	#write to database	
	client.write_points(json_body)