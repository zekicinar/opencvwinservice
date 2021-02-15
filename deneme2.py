import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import cv2

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TEST SERVICE2"
    _svc_display_name_ = "TEST SERVICE2"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.isrunning = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isrunning = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        videoStream = cv2.VideoCapture(0)
        while self.isrunning:
            (grabbed, frame) = videoStream.read()
            cv2.imwrite(r'C:\Users\User\Desktop\windowshizmet\winserdeneme.png',frame)
            cv2.namedWindow('ImageWindowName', cv2.WINDOW_NORMAL)
            cv2.imshow('ImageWindowName',frame)
            #cv2.imshow('Frame', frame)
            #cv2.imwrite(r'C:\Users\User\Desktop\windowshizmet\winserdeneme.png',frame)
            #time.sleep(5)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                    #break
            cv2.waitKey(1)
        videoStream.release()
        cv2.destroyAllWindows()
        

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
