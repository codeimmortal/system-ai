# for app in /usr/share/applications/*.desktop; 
#     do echo "${app:24:-8}"; done
import pathlib

def getapplicationlist():
    "get application list"
    root = "/usr/share/applications/"
    root_dir_instance = pathlib.Path(root)
    list = [item.name[:-8] for item in root_dir_instance.glob("*.desktop")]
    return list

def checkStatusForApplication(searchapp,appList):
    "check application status"
    # for item in appList:
    #     if (item.find(searchapp)) != -1:
    #     print ('Found at ', item)
    matchers = searchapp
    matching = [s for s in appList if any(xs in s for xs in matchers)]
    return matching