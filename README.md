# Simple MoCap
## A simple Python client for the OptiTrack MoCap System<br/>

### Features:
- Just works out-of-the-box. Use *example.py* as a starting point
- No external paqckage requirements - just Python 3.x
- Thread safe
### Prerequisites:
- python 3.x
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
Solution: Restart the script</br></br>
Error: Everything works but your object is not being tracked</br>
Cause: Object not tracked by Motive or mismatch of string name or int ID</br>
Solution: Verify setting in Motive

### Notice:
Uses OptiTrack NatNet direct depacketization library for Python 3.x
https://optitrack.com/support/downloads/developer-tools.html
Some nessesary modifications were made to NatNetClient.py and commented *(Alon Gil-Ad)*.<br/>
Original script included and renamed "NatNetClient-original.py".



