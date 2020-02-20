import logging
import urllib3
import re
import socket
import napalm


class GaiaOSDriver(napalm.base.base.NetworkDriver):
    def __init__(self, hostname,
            username='',
            password='',
            timeout=10,
            optional_args=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout
        self.optional_args = optional_args

    def open(self):
        device_type = "cpgaia"
        self.device = self._netmiko_open(device_type, netmiko_optional_args=self.optional_args)

    def close(self):
        self._netmiko_close()
    
    def cli(self, commands: list) -> dict:
        output = {}
        try:
            if isinstance(commands, list):
                for cmd in commands:
                    output[cmd] = self.device.send_command(cmd)
            else:
                raise TypeError(
                    "Expected <class 'list'> not a {}".format(
                        type(commands)
                        )
                    )
            return output
        except (socket.error, EOFError) as e:
            raise ConnectionClosedException(str(e))
    
    def get_users(self):
        print('blub')

    def get_arp_table(self, vrf=""):
        pass

    def get_config(self, retrieve="all", full=False):
        pass

    def get_facts(self):
        pass

    def get_interfaces(self):
        pass

    def get_interfaces_ip(self):
        pass


if __name__ == '__main__':
    pass
