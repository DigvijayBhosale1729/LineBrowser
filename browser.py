#Written By FoxSinOfGreed1729
#Thanks to devs of Python, Selenium

import platform
import browserforlinuxfirefox
import browserforwindowsfirefox
import browserforwindowschromechan
import browserinput
import windowschromechanclick
import windowsfirefoxclick
import linuxfirefoxclick

if platform.system()=='Linux':

    try:
        print('Linux')
        data=[None, None, None, None, None]
        data=browserinput.inputfn()
        print('Input smooth')
        print(data)
        if data[2]==None:
            browserforlinuxfirefox.linuxOpenSite(data[0])
        elif data[4]==None:
            print('In 2')
            print(data)
            if data[3]==1:
                driverobj=browserforlinuxfirefox.linuxSearchByID(data[0],data[1],data[2])
            elif data[3]==2:
                driverobj=browserforlinuxfirefox.linuxSearchByLinkText(data[0],data[1],data[2])
            elif data[3]==3:
                driverobj=browserforlinuxfirefox.linuxSearchByName(data[0],data[1],data[2])
            elif data[3]==4:
                driverobj=browserforlinuxfirefox.linuxSearchByTagName(data[0],data[1],data[2])
            elif data[3]==5:
                driverobj=browserforlinuxfirefox.linuxSearchByXpath(data[0],data[1],data[2])
            else:
                if driverobj=='error':
                    print('Some error has occured while searching for requested identifier')
                    exit(0)
                print('Incorrect Data Entered')
            driverobj.quit()
        elif data[4]!=None:
            if data[3]==1:
                driverobj=browserforlinuxfirefox.linuxSearchByID(data[0],data[1],data[2])
            elif data[3]==2:
                driverobj=browserforlinuxfirefox.linuxSearchByLinkText(data[0],data[1],data[2])
            elif data[3]==3:
                driverobj=browserforlinuxfirefox.linuxSearchByName(data[0],data[1],data[2])
            elif data[3]==4:
                driverobj=browserforlinuxfirefox.linuxSearchByTagName(data[0],data[1],data[2])
            elif data[3]==5:
                driverobj=browserforlinuxfirefox.linuxSearchByXpath(data[0],data[1],data[2])
            else:
                if driverobj=='error':
                    print('Some error has occured while searching for requested identifier')
                    exit(0)
                print('Incorrect Data Entered')
            print(driverobj)
            linuxfirefoxclick.linuxClick(driverobj, data[4])
            driverobj.quit()
    except:
        print('Error in finding elements or incorrect site entered')


elif platform.system()=='Windows':
    try:
        print('windows')
        data=[None, None, None, None, None]
        data=browserinput.inputfn()
        print('Input smooth')
        if len(data)==1:
            browserforwindowsfirefox.windowsOpenSite(data[0])
        elif len(data)==4 and data[3]==0:
            if data[3]==1:
                driverobj=browserforwindowsfirefox.windowsSearchByID(data[0],data[1],data[2])
            elif data[3]==2:
                driverobj=browserforwindowsfirefox.windowsSearchByLinkText(data[0],data[1],data[2])
            elif data[3]==3:
                driverobj=browserforwindowsfirefox.windowsSearchByName(data[0],data[1],data[2])
            elif data[3]==4:
                driverobj=browserforwindowsfirefox.windowsSearchByTagName(data[0],data[1],data[2])
            elif data[3]==5:
                driverobj=browserforwindowsfirefox.windowsSearchByXpath(data[0],data[1],data[2])
            else:
                if driverobj=='error':
                    print('Some error has occured while searching for requested identifier')
                    exit(0)
                print('Incorrect Data Entered')
            driverobj.quit()
        elif len(data)==4:
            if data[3]==1:
                driverobj=browserforwindowsfirefox.windowsSearchByID(data[0],data[1],data[2])
            elif data[3]==2:
                driverobj=browserforwindowsfirefox.windowsSearchByLinkText(data[0],data[1],data[2])
            elif data[3]==3:
                driverobj=browserforwindowsfirefox.windowsSearchByName(data[0],data[1],data[2])
            elif data[3]==4:
                driverobj=browserforwindowsfirefox.windowsSearchByTagName(data[0],data[1],data[2])
            elif data[3]==5:
                driverobj=browserforwindowsfirefox.windowsSearchByXpath(data[0],data[1],data[2])
            else:
                if driverobj=='error':
                    print('Some error has occured while searching for requested identifier')
                    exit(0)
                print('Incorrect Data Entered')
            windowsfirefoxclick.windowsClick(driverobj, data[4])
            driverobj.quit()
    except:
        print('Error in finding elements or incorrect site entered')
