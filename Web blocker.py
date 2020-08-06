from datetime import datetime as dt
import time
import io

block_websites = ["www.facebook.com", "web.whatsapp.com", "twitter.com"]
redirect = "127.0.0.1"
host_path = "C:\Windows\System32\drivers\etc\hosts"
work_hours = [dt(dt.now().year,dt.now().month,dt.now().day,14),dt(dt.now().year,dt.now().month,dt.now().day,19)]
print(work_hours)


while True:
    if work_hours[0] < dt.now() < work_hours[1]:
        print("Common its our working hours!")
        with open(host_path,'r+') as file:
            content = file.read()
            for site in block_websites:
                if site in content: pass
                else:
                    file.write("\n"+redirect+" "+site)
    else:
        print("Yay its my funtime now")
        with open(host_path,'r+') as file1:
            contents = file1.readlines()
            file1.seek(0)
            for line in content:
                if not any(site in line for site in block_websites):
                    file1.write(line)
            file1.truncate()

    time.sleep(10)
