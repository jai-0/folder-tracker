import watchdog
from watchdog.events  import FileSystemEventHandler
from watchdog.observers import Observer
import time
import sys
class ToWatch:
    watchDirectory = "C:\Users\Atharva\AppData\Local\Packages\Microsoft.ScreenSketch_8wekyb3d8bbwe\TempState"#your directory, in this case its the temperory snip and sketch folder for me

    def __init__(self):
        self.oberver=Observer()
        
    def run(self):
        event_handler=Handler()
        self.observer.schedule(event_handler,self.watchDirectory,recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
        