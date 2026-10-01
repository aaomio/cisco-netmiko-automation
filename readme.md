# Cisco Network Automation with Netmiko

Python network automation project using **Netmiko** to configure Cisco routers and switches.

The project was built in two stages: first establishing the network and remote access manually through the CLI, followed by Python-based configuration using Netmiko.

## Project Structure

```text
.
├── [config_init/](config_init/)
├── [run_cfg_dotpy/](run_cfg_dotpy/)
└── [Screengrabs/](Screengrabs/)
```

### `config_init`

Contains the initial Cisco IOS CLI configuration files used to establish:

* Device connectivity
* Management VLAN
* Telnet access

These configurations were initially applied through console access.

### `run_cfg_dotpy`

Contains the Python automation scripts and corresponding Cisco configuration files.

The Python scripts use **Netmiko** to connect to the devices and deploy the `.cfg` files.

### `Screengrabs`

Contains screenshots documenting the configuration and automation process.

## Initial Network Setup

The initial configuration established connectivity between the devices and enabled remote management.

A management VLAN was configured on the switches, with VLAN 30 used for management.

An EtherChannel was configured between the two switches using LACP.

Telnet was enabled for remote access because SSH was not supported by the IOS used on the lab devices.

