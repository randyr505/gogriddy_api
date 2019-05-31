# gogriddy_api

# Setup config
cp config_template.cfg to config.cfg
Modify the config.cfg to use your meterID, memberID, and settlement_point

# InfluxDB
If you are using influxdb then make sure to uncomment the line that adds it to your DB
i.e. #client.write_points(influxdb_entry, protocol=influxdb_protocol)

# crontab entry
0,5,10,15,20,25,30,35,40,45,50,55 * * * * /Users/username/bin/gogriddy_api.py

# Referral Link
http://bit.ly/gogriddy
