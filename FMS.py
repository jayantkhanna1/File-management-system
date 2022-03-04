#using watchdog module to check
import watchdog.events
import watchdog.observers
import time
  
#defining class to get events 
class FileWatcherBinding(watchdog.events.PatternMatchingEventHandler):
    #initial function
    def __init__(self,timee):
        time.sleep(timee)
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*'],ignore_directories=True, case_sensitive=False)
    #checking for directory events
    #checking for on created events
    def on_created(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received created event - % s." % event.src_path)
        f.close()
        print("Watchdog received created event - % s." % event.src_path)

    #checking for modified event
    def on_modified(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received modified event - % s." % event.src_path)
        f.close()
        print("Watchdog received modified event - % s." % event.src_path)

    #checking for deleted event
    def on_deleted(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received deleted event - % s." % event.src_path)
        f.close()
        print("Watchdog received deleted event - % s." % event.src_path)

    #checking for any event
    def on_any_event(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received event happen- % s." % event.src_path)
        f.close()
        print("Watchdog received event happen - % s." % event.src_path)

    #checking for moving event
    def on_moved(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received move event - % s." % event.src_path)
        f.close()
        print("Watchdog received move event - % s." % event.src_path)
    
    #checking for closed event
    def on_closed(self, event):
        #creating a log file
        f=open('log.txt','a')
        #writing in log file
        f.write("Watchdog received closed event - % s." % event.src_path)
        f.close()
        print("Watchdog received closed event - % s." % event.src_path)
  
if __name__ == "__main__":
    #Getting dir path from user
    src_path = input("Enter path to a dir ")
    
    #calling class and getting its objects
    event_handler = FileWatcherBinding(1)

    #Staring observer
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()

    #Exists on keyboard interrrupt
    try:
        print("Monitoring")
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting")
        observer.stop()
    observer.join()