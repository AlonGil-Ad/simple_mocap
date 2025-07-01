# Copyright 2025 by Alon Gil-Ad
# Center for Intelligent Systems (CIS), Faculty of Computer Science
# Technion - Israel Institute of Technology
# https://github.com/AlonGil-Ad/simple_mocap

from time import sleep
import logging

from simple_mocap.natnet_client import NatNetClient
from simple_mocap import DataDescriptions
from simple_mocap.Asset import Asset

logger = logging.getLogger()

class SimpleMocap:
    _assets = []                # List of tracked assets
    _streaming_client = None    # NatNet client
    _frame_no: int = 0          # Frame count for this client
    _server_frame_no: int = 0   # Frame number as reported by the server

    def __init__(self, local_ip, server_ip):
        # Setup
        self._streaming_client = NatNetClient()
        self._streaming_client.print_level = 0
        self._streaming_client.set_client_address(local_ip)
        self._streaming_client.set_server_address(server_ip)
        self._streaming_client.set_use_multicast(1)
        self._streaming_client.new_frame_with_data_listener = self.__receive_new_frame_with_data
        self._streaming_client.data_descriptions_listener = self.__receive_new_data_description

        # Start
        logger.info(f'SimpleMocap: starting sync')
        self._streaming_client.run("c")
        self._streaming_client.request_data_descriptions()

        # Wait a while for the system to start transmitting. Increase on low network performance
        sleep(1)

    # Callback for frame data
    def __receive_new_frame_with_data(self, data_dict):
        self._frame_no += 1
        self._server_frame_no = data_dict["frame_number"]
        rb_list = data_dict["mocap_data"].rigid_body_data.rigid_body_list
        for rb in rb_list:
            if rb.id_num in self._assets:
                a = next(asset for asset in self._assets if asset == rb.id_num)
                if not rb.tracking_valid:
                    a.set_tracking_invalid()
                else:
                    a.set_location(rb.pos, rb.rot)

    # Callback for tracked object description
    def __receive_new_data_description(self, data_desc: DataDescriptions):
        logger.debug(f'SimpleMocap: received Data Descriptions')
        for rb in data_desc.rigid_body_list:
            if rb.id_num not in self._assets:
                self._assets.append(Asset(rb.id_num, DataDescriptions.get_as_string(rb.sz_name)))
        logger.debug(f'SimpleMocap: tracked rigid bodies:')
        for a in self._assets:
            logger.debug(f'{a}')

    # Returns ((x, y, z), (qx, qy, qz, qw))
    # asset can be string name or ID int as defined in Motive
    def get_location(self, asset):
        try:
            a = next(a for a in self._assets if a == asset)
            if not a.is_tracking_valid():
                logger.warning(f'Tracking for {asset} is invalid')
                return None
            return a.get_location()
        except StopIteration:       # asset not in assets and isn't being tracked
            logger.warning(f'{asset} is not being tracked')
            return None

    # Get frame number of current session
    def get_frame_number(self) -> int:
        return self._frame_no

    # Get server's frame number. Resets on Motive relaunch
    def get_system_frame_number(self) -> int:
        return self._server_frame_no

    # Orderly shutdown - important!
    def shutdown(self):
        if self._streaming_client is not None:
            logger.info(f'SimpleMocap: shutting down')
            self._streaming_client.shutdown()
            self._streaming_client = None




