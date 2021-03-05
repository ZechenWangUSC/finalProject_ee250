EE 250 Final Project
By: Zechen Wang

Instructions:

*External Libraries:
  1) Grovepi, instructions available in Lab2 document. 
      https://docs.google.com/document/d/17NHBwSutQN23CijD4JJJOim-Y_GUBpsduvoaBICbWlE/edit
      **IMPORTANT: Please change line 10 in sensors.py to your local Grovepi Library
  2) Influx-Python
      https://influxdb-python.readthedocs.io/en/latest/

*Setup:
  1) Raspberry Pi and GrovePi sensor kit are needed
  2) Use D4 for Ultrasonic ranger, D3 for humidity and temperature sensor, A0 for light sensor.
  3) Run sensors.py to start application.
  **This project require a cloud server. The server used in the demo will keep running till Dec.30, 2020. 

  3a) If you wish to use my server:
    1) log into http://45.76.207.242:3000, the credentials are 'admin' and 'password'
    2) find the 'project' dashboard
    3) run sensors.py on your local device, and you should see visualized data.
       **IMPORTANT: You might need to change the time range on the upper right corner. Current settings are for a different timezone.

  3b) If you wish to use your own server:
    1) see comments in sendInflux.py and change the target address.
    2) install and run influxDB on your server.
    3) install and run Grafana on your server.
    4) add InfluxDB as a source in Grafana, and the database is named 'project', no authentication used
    5) add the following query strings in Grafana dashboard:
        SELECT "value" FROM "Temperature" WHERE ("host" = 'Device1') AND $timeFilter
        SELECT "value" FROM "Humidity" WHERE ("host" = 'Device1') AND $timeFilter
        SELECT "value" FROM "Light" WHERE ("host" = 'Device1') AND $timeFilter
        SELECT "value" FROM "Distance" WHERE ("host" = 'Device1') AND $timeFilter
    6) run sensors.py on your local device, and you should see visualized data.

Details on Grafana & InfluxDB configuration can be found in documentation:
https://github.com/ZechenWangUSC/finalProject_ee250/blob/master/ref.pdf
