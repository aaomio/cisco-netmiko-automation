from netmiko import ConnectHandler

SW1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.30.11",
    "username": "admin",
    "password": "cisco",
}

connection = ConnectHandler(**SW1)

print(connection.is_alive())

connection.send_config_from_file("SW1.cfg")

running = connection.send_command("show running-config")
print(running)

startup = connection.send_command("show startup-config")
print(startup)

connection.disconnect()