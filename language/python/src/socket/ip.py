#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


print("eth0 = " + get_ip_address('eth0'))
print("lo = " + get_ip_address('lo'))
