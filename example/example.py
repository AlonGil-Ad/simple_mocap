# Copyright 2025 by Alon Gil-Ad
# Center for Intelligent Systems (CIS), Faculty of Computer Science
# Technion - Israel Institute of Technology
# https://github.com/AlonGil-Ad/simple_mocap

import logging
from time import sleep
from simple_mocap import SimpleMocap

if __name__ == "__main__":
    # Optional logger usage. The client inherits the root logger.
    # Default logging level for the client is INFO
    logger = logging.getLogger()
    logging.basicConfig(encoding='utf-8')
    # Available logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    logger.setLevel('DEBUG')
    # Instantiate and starts the client. Change local_ip to your IP address
    mocap = SimpleMocap(local_ip="132.68.35.50", server_ip="132.68.35.2")

    for i in range(5):
        print(f'Frame number: {mocap.get_frame_number()}')                      # Get frame number
        print(f'Target: {mocap.get_location("Target")}')                        # Get rigid body "Target" by name
        print(f'Target: {mocap.get_location(603)}')                             # Get rigid body "Traget" by ID
        print(f'NonexistantBody: {mocap.get_location("NonexistantBody")}')      # Get undefined rigid body
        sleep(1)

    mocap.shutdown()        # Always call shutdown before script end

