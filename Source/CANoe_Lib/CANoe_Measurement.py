
import win32com.client
from .A_Event import *
class CanoeMeasurement:
    #class variable
    started = False
    stopped = True

    def __init__(self, measurement_object):
        self.measurement = measurement_object
        win32com.client.WithEvents(self.measurement, MeasurementEvent)
        self.running = lambda : self.measurement.Running

    def start(self):
        if not self.running():
            self.measurement.Start()
            DoEventsUntil(lambda : CanoeMeasurement.started, "Start Measurement", 60000)

    def stop(self):
        if self.running():
            self.measurement.StopEx()
            DoEventsUntil(lambda : CanoeMeasurement.stopped, "Stop Measurement", 30000)

#--------------------------- EVENT CALLBACK - START ---------------------------------------------------

class MeasurementEvent:

    def __init__(self):
        pass

    def OnStart(self):
        print("CANoe measurement starting...")
        CanoeMeasurement.started = True
        CanoeMeasurement.stopped = False

    def OnStop(self):
        print("CANoe measurement stopping...")
        CanoeMeasurement.started = False
        CanoeMeasurement.stopped = True

    def OnInit(self):
        print("CANoe measurement initilizing...")

    def OnExit(self):
        print("CANoe measurement closing...")

#--------------------------- EVENT CALLBACK - END ---------------------------------------------------