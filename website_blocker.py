# importing time module to get local time
import time
from datetime import datetime as dt

# ip address of our local host to redirect website ip to our local host
ip_localmachine="127.0.0.1"
# list of websites we want to block
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
# address of our host file
hosts_path="C:\Windows\System32\drivers\etc\hosts"
# time period which we want to block website
start_time="09:0:0"
end_time="18:0:0"

# printing current time
now=dt.now()
current_time=now.strftime("%H:%M:%S")
print(current_time)

# running loop and blocking websites
while True:
    current_time=now.strftime("%H:%M:%S")
    if start_time<=current_time and current_time<=end_time:
        print("Working hours")
        # using file handling we are opening our host file  *r+* mode is to read and write into file
        with open(hosts_path,"r+") as file:
            content=file.read()
            # checking if website address is in our list 
            for website in website_list:
                if website in content:
                    pass
                
                else:
                    # writing websites we want to block in our host file
                    file.write(ip_localmachine+" "+website+"\n")
            
    else:
        # printing "Non working hours" if time is not in our working time
        print("Non working hours")
        with open(hosts_path,"r+") as file:
            file.truncate(0)
            file.close()
            
    # looping it for every 10 sec 
    time.sleep(10)
