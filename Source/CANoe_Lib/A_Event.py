import pythoncom
import time

def _DoEvents():
    pythoncom.PumpWaitingMessages()
    time.sleep(.1)

def DoEventsUntil(cond, event_name:str, timeout_ms:int):
    timeout = int(timeout_ms/100)
    for i in range(0, timeout):
        if not cond():
            _DoEvents()
        else:
            break
    else:
        print(f"Timeout ({timeout_ms/1000}s), unable to '{event_name}', event not occurred.")
