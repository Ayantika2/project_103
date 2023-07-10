import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\Ayantika\Downloads"
to_dir = "C:\Users\Ayantika\Grade 11\Files"

dir_tree = {
    "Image_Files" : ['.jpg','.png','.jpeg','.jfif','.gif'],
    "Video_Files" : ['.mp4', '.mov', '.avi'],
    "Document_Files" : ['.docx', '.ppt','.xlxs','.xls','.pdf'],
    "Steup_Files": ['.exe','.bin','.cmd','.msi','.dmg']
}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
        name,extension = os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            time.sleep(2)
            
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded"+file_name)
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = path2 + '/' + file_name
                
                if os.path.exists(path2):
                    print("Directory already exists")
                    print("Moving .... ")
                else:
                    print("Making Directory")
                    os.makedirs(path2)
                    print("Moving .... ")
                    shutil.move(path1,path3)
                    time.sleep(2)
        
    def on_deleted(self,event):
        print(f"Oops! Someone deleted{event.src_path}")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stopped()                