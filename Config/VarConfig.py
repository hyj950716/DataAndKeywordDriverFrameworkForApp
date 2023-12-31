import os
# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\TestData\\七猫免费小说.xlsx"

# 获取配置文件存放路径
desiredcapsFilePath = parentDirPath + "\\Config\\DesiredScapsConfig.ini"

#异常图片存放目录
screenPicturesDir = parentDirPath + "\\ExceptionPictures"


# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName=1
testCase_frameworkName=3
testCase_testStepSheetName=4
testCase_dataSourceSheetName=5
testCase_isExecute=6
testCase_runTime=7
testCase_testResult=8

# 用例步骤表中，部分列对应的数字序号
caseStep_caseStepDescription=1
caseStep_keyWord=2
caseStep_locationType=3
caseStep_locatorExpression=4
caseStep_operatorValue=5
caseStep_runTime=6
caseStep_testResult=7
caseStep_errMsg=8
caseStep_errPicPath=9

# 数据源表中，是否执行列对应的数字编号
dataSource_appName=1
dataSource_assertKeyword=2
dataSource_isExecute=3
dataSource_runTime=4
dataSource_testResult=5


if __name__ == "__main__":
    print(dataFilePath)