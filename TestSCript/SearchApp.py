from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
from Action.PageAction import *
import traceback

def searchApp(execlObj, stepSheet, dataSheet):
    try:
        dataIsExecuteCols = execlObj.getColumn(dataSheet, dataSource_isExecute)
        appNameCols = execlObj.getColumn(dataSheet, dataSource_appName)

        # 需要执行的数据个数
        requireDataNum = 0
        # 成功执行的数据个数
        successfulDataNum = 0

        for idx, i in enumerate(dataIsExecuteCols[1:]):
            if i.value == "y":
                requireDataNum += 1
                successfulStepNum = 0
                print("开始执行[%s]" %appNameCols[idx + 1].value)
                stepNum = execlObj.getRowsNumber(stepSheet)

                for j in range(2, stepNum + 1):
                    # 用例步骤中第一行为标题行，所以需要从第二行开始
                    stepRow = execlObj.getRow(stepSheet, j)

                    # 获取用例步骤中的描述
                    stepDescription = stepRow[caseStep_caseStepDescription - 1].value
                    # 获取关键字列的函数名
                    keyWord = stepRow[caseStep_keyWord - 1].value
                    # 获取操作元素定位方式
                    locationType = stepRow[caseStep_locationType - 1].value
                    # 获取定位表达式
                    locationExpression = stepRow[caseStep_locatorExpression -1].value
                    # 获取操作值
                    operatorValue = stepRow[caseStep_operatorValue -1].value

                    print(keyWord, " ", locationType, " ", locationExpression, " ", operatorValue)

                    if isinstance(operatorValue, int):
                        # 数值类型数据从excel中读取出来是int类型，需要转换成字符串，方便拼接
                        operatorValue = str(operatorValue)

                    # 构造可执行的关键字需要调用的函数字符串
                    if keyWord and locationType and locationExpression and operatorValue:
                        # 表示调用的是传递三个参数的方法
                        if len(operatorValue) == 1 and operatorValue.isupper():
                            step = keyWord + "('%s', '%s', '%s')" % (locationType, locationExpression, appNameCols[idx + 1].value)
                        else:
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
                        print("执行步骤“%s”失败\n异常信息：%s" %(stepDescription, str(traceback.format_exc())))
                if successfulStepNum == stepNum - 1:
                    successfulDataNum += 1
                else:
                    print("执行失败")
            else:
                print("[%s]被设置为忽略执行" %appNameCols[idx + 1].value)
        if requireDataNum == successfulDataNum:
            return 1
        return 0




    except Exception as err:
        print("数据驱动框架主程序发生异常\n异常信息:%s" % str(traceback.format_exc()))