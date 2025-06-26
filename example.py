# Copyright 2025 by Alon Gil-Ad
# Center for Intelligent Systems (CIS), Faculty of Computer Science
# Technion - Israel Institute of Technology
# https://github.com/AlonGil-Ad/simple_mocap

import logging
from time import sleep
from SimpleMocap import SimpleMocap

if __name__ == "__main__":
    logger = logging.getLogger()
    # Available logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    logger.setLevel('DEBUG')
    logging.basicConfig(encoding='utf-8')
    # Instantiate and starts the client. Change local_ip to your IP address
    mocap = SimpleMocap(local_ip="132.68.35.50", server_ip="132.68.35.2")

    for i in range(5):
        print(f'Frame number: {mocap.get_frame_number()}')
        print(f'Target: {mocap.get_location("Target")}')
        print(f'Target: {mocap.get_location(603)}')
        print(f'Tello2: {mocap.get_location("Tello2")}')
        print(f'Tello3: {mocap.get_location("Tello3")}')
        sleep(1)

    mocap.shutdown()

