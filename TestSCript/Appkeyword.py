from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
from Action.PageAction import *
import traceback
from TestSCript.SearchApp import searchApp


# 第一步：获取需要被测试功能模块
# 第二步：获取功能模块的测试步骤以及测试数据
# 第三步：启动一个全新的appium session
# 第四步：客户端与appium服务端通信，发送命令操作设备上的apk
# 第五步：截取错误信息
# 第六步：执行结果回写

def appkeyword():
    # 主入口方法
    excelObj = ParseExcel()
    excelObj.loadWorkBook(dataFilePath)
    caseSheet = excelObj.getSheetByName("测试用例")

    # 记录需要执行的用例个数
    requireCaseNum = 0
    # 记录执行成功的用例数
    successfulCaseNum = 0

    # 获取是否需要执行列的列对象
    isExecuteCaseCols = excelObj.getColumn(caseSheet, testCase_isExecute)
    for idx, i in enumerate(isExecuteCaseCols[1:]):
        if i.value == "y":
            requireCaseNum += 1
            # "需要被执行人"
            caseRow = excelObj.getRow(caseSheet, idx + 2)
            caseName = caseRow[testCase_testCaseName - 1].value
            frameworkName = caseRow[testCase_frameworkName - 1].value
            stepSheetName = caseRow[testCase_testStepSheetName - 1].value
            # print(caseName, " ", frameworkName, " ", stepSheetName)

            if frameworkName == "关键字":
                print("********************* 调用关键字驱动 *******************")
                # 根据用例的sheet名获取用例sheet表对象
                stepSheet = excelObj.getSheetByName(stepSheetName)
                # 获取用例步骤数据
                stepNum = excelObj.getRowsNumber(stepSheet)

                # 记录用例步骤执行成功的个数
                successfulStepNum = 0
                for j in range(2, stepNum +1):
                    # 用例步骤中的第一行是标题行，不需要执行，直接忽略
                    stepRow = excelObj.getRow(stepSheet, j)

                    # 获取用例步骤中的描述
                    stepDesciption = stepRow[caseStep_caseStepDescription - 1].value
                    # 获取关键字列的函数名
                    keyWord = stepRow[caseStep_keyWord - 1].value
                    # 获取操作元素定位方式
                    locationType = stepRow[caseStep_locationType -1].value
                    # 获取操作元素定位表达式
                    locationExpression = stepRow[caseStep_locatorExpression - 1].value
                    # 获取操作值
                    operatorValue = stepRow[caseStep_operatorValue - 1].value
                    print(stepDesciption, " ", keyWord, " ", locationType, " ", locationExpression, " ", operatorValue )

                    # eval('click("id", "xxxx")')

                    if isinstance(operatorValue, int):
                        # 数值类型数据从excel中读取出来是int类型，需要转换成字符串，方便拼接
                        operatorValue = str(operatorValue)

                    # 构造可执行的关键字需要调用的函数字符串
                    if keyWord and locationType and locationExpression and operatorValue:
                        # 表示调用的是传递三个参数的方法
                        step = keyWord + "('%s', '%s', '%s')" %(locationType, locationExpression, operatorValue)
                    elif keyWord and locationType and locationExpression:
                        # 表示调用的是传递两个参数的方法
                        step = keyWord + "('%s', '%s')" %(locationType, locationExpression)
                    elif keyWord and operatorValue:
                        # 表示调用的是传递一个参数的方法
                        step = keyWord + "('%s')" %operatorValue
                    elif keyWord:
                        step = keyWord + "()"
                    print(step)
                    try:
                        eval(step)
                        successfulStepNum += 1
                    except Exception as err:
                        # 用例步骤执行失败，获取当前截图
                        errPicPath = capture_screen()
                        print("执行步骤“%s”失败\n异常信息：%s" %(stepDesciption, str(traceback.format_exc())))

                if successfulStepNum == stepNum - 1:
                    successfulCaseNum += 1
                    print("用例【%s】执行成功" %caseName)

            elif frameworkName == "数据":
                print("********************* 调用数据驱动 *******************")
                # 获取数据源表名
                dataSourceSheetName = caseRow[testCase_dataSourceSheetName - 1].value
                # 步骤sheet表对象
                stepSheet = excelObj.getSheetByName(stepSheetName)
                # 数据源表对象
                dataSheet = excelObj.getSheetByName(dataSourceSheetName)
                result = searchApp(excelObj, stepSheet, dataSheet)
                print(result)
                if result:
                    successfulCaseNum += 1
                    print("用例【%s】执行成功" %caseName)
                else:
                    print("用例【%s】执行失败" % caseName)
        else:
            print("第%s行不需要被执行人" %(idx + 2))

if __name__ == "__main__":
    appkeyword()