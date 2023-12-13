import time
import os
import shutil


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler # on_create

source="C:/Users/lscub/Downloads"
dest="C:/Users/lscub/Downloads"

dir_tree = {
    "Image_Files":['.png','.jpg','.jpeg','.gif','.jfif'],
    "Video_Files":['.mpg','.mp2','.mp4','.avi'],
    "Document_Files":['.ppt','.xls','.csv','.pdf','.txt'],
    "Setup_Files":['.exe','.bin','.cmd']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):  # creates folder according to ur file type
        #print(event)
        #name,ext = os.path.splitext(event.src_path)
        #time.sleep(1)
        #for key,value in dir_tree.items():
            #time.sleep(1)
            def on_created(self,event):
                 print("hey,{event.src_path} has been created")
            def on_deleted(self,event):
                 print("Hey,{event.src_path} has been created")

            if ext in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded" + file_name)
                path1 = source + "/"+ file_name
                path2 = dest + "/"+ key
                path3 = path2 + "/"+ file_name

                if os.path.exists(path2):
                    print("directory exist")
                    print("moving " + file_name + "..........")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making directory...........")
                    os.makedirs(path2)
                    print("moving " + file_name + "..........")
                    shutil.move(path1,path3)
                    time.sleep(1)



event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running.....")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
