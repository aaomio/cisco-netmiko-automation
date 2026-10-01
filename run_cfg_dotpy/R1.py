from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "10.0.0.1",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

connection = ConnectHandler(**R1)

print(connection.is_alive())

connection.send_config_from_file("R1.cfg")

running = connection.send_command("show running-config")
print(running)

startup = connection.send_command("show startup-config")
print(startup)

connection.disconnect()