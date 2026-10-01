from netmiko import ConnectHandler

WLC1 = {
    "device_type": "cisco_wlc",
    "host": "192.168.30.20",
    "username": "Admin",
    "password": "PASSWORD"
}

connection = ConnectHandler(**WLC1)

print(connection.find_prompt())

output = connection.send_config_from_file("WLC1.cfg")

print(output)

connection.disconnect()