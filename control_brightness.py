import screen_brightness_control as pct
print(pct.get_brightness())

current_brightness = pct.get_brightness()
print(current_brightness)


pct.set_brightness(35)
 
print(pct.get_brightness())







import platform

#Computer network name
print(f"Computer network name: {platform.node()}")
#Machine type
print(f"Machine type: {platform.machine()}")
#Processor type
print(f"Processor type: {platform.processor()}")
#Platform type
print(f"Platform type: {platform.platform()}")
#Operating system
print(f"Operating system: {platform.system()}")
#Operating system release
print(f"Operating system release: {platform.release()}")
#Operating system version
print(f"Operating system version: {platform.version()}")
import psutil
#Physical cores
print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
#Logical cores
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
#Current frequency
print(f"Current CPU frequency: {psutil.cpu_freq().current}")
#Min frequency
print(f"Min CPU frequency: {psutil.cpu_freq().min}")
#Max frequency
print(f"Max CPU frequency: {psutil.cpu_freq().max}")
#System-wide CPU utilization
print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
#System-wide per-CPU utilization
print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")
#Total RAM
print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
#Available RAM
print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
#Used RAM
print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
#RAM usage
print(f"RAM usage: {psutil.virtual_memory().percent}%")

import webbrowser 
webbrowser.open_new_tab("http://www.google.com")
webbrowser.open_new_tab("http://www.gmail.com")