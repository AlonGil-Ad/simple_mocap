# Simple MoCap
## A simple Python client for OptiTrack MoCap<br/>

### Features:
- Just works out-of-the-box
- No additional packages required - just Python 3.9+
- Supports multiple concurrent clients
- Thread safe
### Prerequisites:
- python>=3.9
### Installation
Install using pip:
```bash
pip install git+https://github.com/AlonGil-Ad/simple_mocap
```

### Quick start:
Use *example.py* as a starting point.</br>
Instantiate SimpleMocap with local IP address (your machine) and server IP address (the machine that runs Motive).
Call get_location(asset) to get the position and rotation of a rigid body by either the String name or Integer ID as defined in Motive.
Return value is a Tuple of the position Tuple and the quaternion rotation Tuple:</br>
((x, y, z), (qx, qy, qz, qw))</br>
Tracking invalid means that the minimum number of markers as defined in Motive isn't being seen by the cameras.</br>
If a rigid body isn't being tracked then it's not marked for tracking in Motive.</br>
get_frame_number() returns the frame number of the current client session.</br>
get_system_frame_number() returns the frame number of Motive. It resets when the stream starts.
### Troubleshooting:
Error: *OSError: [Errno 19] No such device*</br>
Cause: Wrong *local_ip* sent to constructor</br>
Solution: Verify and set correct IP address</br></br>
Error: *struct.error: unpack requires a buffer of 12 bytes*</br>
Cause1: Wrong *server_ip* sent to constructor</br>
Slution: Verify and set correct IP address</br>
Cause2: NatNetClient.py depacketization error or network error</br>
Solution: Restart the script</br></br>
Error: Partial or empty tracking list</br>
Cause: Internal depacketization error or network error</br>
Solution: Restart the script. Make sure to call shutdown()</br></br>
Error: Everything works but your object is not being tracked</br>
Cause: Object not marked for tracking in Motive or wrong String name or Integer ID sent to get_location</br>
Solution: Verify settings in Motive
### Note:
Python 3.9 and above is required for some Logger declarations (specifically the *encoding* keyword).</br>
If you absolutely must use an older version of Python, just remove Logging and replace it with *print* where needed.</br>
The client itself should run on Python=3.x (not tested)
### Notice:
Uses OptiTrack NatNet direct depacketization library for Python 3.x:</br>
https://optitrack.com/support/downloads/developer-tools.html</br>
Some nessesary modifications were made to *NatNetClient.py* and commented *(Alon Gil-Ad)*.<br/>
Original script included and renamed *NatNetClient-original.py*.
