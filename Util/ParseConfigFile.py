from configparser import ConfigParser
from Config.VarConfig import desiredcapsFilePath

class ParseConfigFile():
    def __init__(self, path):
        self.cf = ConfigParser()
        self.cf.read(path)

    def getItemSection(self, sectionName):
        opetionsDict = dict(self.cf.items(sectionName))
        return opetionsDict

    def getOptionValue(self, sectionName, optionName):
        optionValue = self.cf.get(sectionName, optionName)
        return optionValue

if __name__ == "__main__":
    pcf = ParseConfigFile(desiredcapsFilePath)
    res = pcf.getItemSection("Desired_caps")
    print(type(res))
    print(res)
