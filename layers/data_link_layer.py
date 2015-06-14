# coding: utf-8
from utils import formatting

__author__ = 'vadim'


class EthernetII:
    def __init__(self, dst_mac=None, src_mac=None, ether_type=None, data=None):
        """
        Кадр канального уровня протокола Ethernet II
        :param dst_mac: MAC-адрес получателя
        :param src_mac: MAC-адрес отправителя
        :param ether_type: тип протокола инкапсулируемого пакета
        :param data: инкапсулированный пакет
        :return:
        """
        self.dst_mac = dst_mac
        self.src_mac = src_mac
        self.ether_type = ether_type
        self.data = data

    def __str__(self):
        return 'Destination MAC : ' + formatting(self.src_mac) + \
               ' Source MAC : ' + formatting(self.dst_mac) + \
               ' Protocol : ' + str(self.ether_type)