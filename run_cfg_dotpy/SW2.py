from netmiko import ConnectHandler

SW2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.30.12",
    "username": "admin",
    "password": "cisco",
}

connection = ConnectHandler(**SW2)

print(connection.is_alive())

connection.send_config_from_file("SW2.cfg")

running = connection.send_command("show running-config")
print(running)

startup = connection.send_command("show startup-config")
print(startup)

connection.disconnect()