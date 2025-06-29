# Simple MoCap
## A simple Python client for OptiTrack MoCap<br/>

### Features:
- Just works out-of-the-box
- No additional packages required - just Python 3.x
- Supports multiple concurrent clients
- Thread safe
### Prerequisites:
- python 3.x
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
Solution: Vetify and set correct IP address</br></br>
Error: *struct.error: unpack requires a buffer of 12 bytes*</br>
Cause1: Wrong *server_ip* sent to constructor</br>
Slution: Vetify and set correct IP address</br>
Cause2: NatNetClient.py depacketization error or network error</br>
Solution: Restart the script</br></br>
Error: Partial or empty tracking list</br>
Cause: Internal depacketization error or network error</br>
Solution: Restart the script. Make sure to call shutdown()</br></br>
Error: Everything works but your object is not being tracked</br>
Cause: Object not tracked by Motive or mismatch of string name or int ID</br>
Solution: Verify setting in Motive

### Notice:
Uses OptiTrack NatNet direct depacketization library for Python 3.x</br>
https://optitrack.com/support/downloads/developer-tools.html</br>
Some nessesary modifications were made to *NatNetClient.py* and commented *(Alon Gil-Ad)*.<br/>
Original script included and renamed *NatNetClient-original.py*.
