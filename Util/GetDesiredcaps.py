from Config.VarConfig import desiredcapsFilePath
from Util.ParseConfigFile import ParseConfigFile

def getDesiredcaps():
    # 获取desired_cpas的配置信息
    pcf = ParseConfigFile(desiredcapsFilePath)
    items = pcf.getItemSection("Desired_caps")
    print(items)
    desired_caps = {
        'platformName': items['platformname'],
        'platformVersion': items['platformversion'],
        'deviceName': items['devicename'],
        'appPackage': items['apppackage'],
        'appActivity': items['appactivity'],
        'unicodeKeyboard': items['unicodekeyboard'],
        'autoAcceptAlerts': items['autoacceptalerts'],
        'resetKeyboard': items['resetkeyboard'],
        'noReset': items['noreset'],
        'newCommandTimeout': items['newcommandtimeout']
    }
    return desired_caps

if __name__ == "__main__":
    print(getDesiredcaps())
