from rich.console import Console
import wmi

computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_name = os_info.Name
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

console = Console()
value = []

specification = {
    "OS Name": str(format(os_name[11:25])),
    "OS Version": str(format(os_version)),
    "CPU": str(format(proc_info.Name)),
    "RAM": str(format(system_ram)),
    "Graphics Card": str(format(gpu_info.Name))
    }      
    
for key in specification.keys():
    value.append(key)

def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def info(message):
    log ("INFO", message)

def logicalToStrConverter(logic):
    return "y" if logic else "n"

def showMenu(modes):
    console.rule("[bold red] Menu")
    for entry in value:
        print ("[" + str(value.index(entry)) + "] / [ " + logicalToStrConverter(modes[entry]) + " ]: " + entry)
    print("[" + str(len(value)) + "]: Proceed")
    
def getUserChoice(modes):
    showMenu(modes)
    return int(input("Choose the option "))

def buildModes():
    modes = {}
    for entry in value:
        modes[entry] = False
    return modes

def startManager():
    modes = buildModes()
    while True:
        choice = getUserChoice(modes)
        if choice == len(value):
            return modes
            break
        else:
            try:
                modes[value[choice]] = not modes[value[choice]]
            except Exception as e:
                info("Please, enter valid number")
    
def Result(modes):
    resultstr = ""
    for entry in value:
        if modes[entry]:
            resultstr += (entry + ": "  + specification[entry]) + "\n"
    dataFile = open("Lesson4.txt", "w")
    dataFile.write(resultstr)
    dataFile.close()

def main():
    info("Program started")
    Result(startManager())

main()