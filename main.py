import watchdog
from watchdog.events  import FileSystemEventHandler
from watchdog.observers import Observer
import time
import sys
class ToWatch:
    watchDirectory = r"C:\Users\Atharva\AppData\Local\Packages\Microsoft.ScreenSketch_8wekyb3d8bbwe\TempState" #your directory, in this case its the temperory snip and sketch folder for me

    def __init__(self):
        self.oberver = Observer()
        
    def run(self):

        event_handler=Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_change(event):
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            print (event.src_path)
  
if __name__ == '__main__':
    watch = ToWatch()
    watch.run()