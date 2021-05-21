import watchdog
from watchdog.events  import FileSystemEventHandler
from watchdog.observers import Observer
import sys
class ToWatch():
    watchDirectory = "C:\Users\Atharva\AppData\Local\Packages\Microsoft.ScreenSketch_8wekyb3d8bbwe\TempState"#your directory, in this case its the temperory snip and sketch folder for me
    

