from PyQt5 import QtWidgets
import sys
import random

import Ui_untitled

class fruit(QtWidgets.QMainWindow,Ui_untitled.Ui_MainWindow):
    def __init__(self):
        super(fruit,self).__init__()
        self.setupUi(self)
    #点击开始按钮
    def onStart(self):
        #情况上面数据
        self.textBrowser.setHtml(randomNum(1))
        self.textBrowser_2.setHtml(randomNum(2))
        self.textBrowser_3.setHtml(randomNum(3))
        self.textBrowser_4.setHtml(randomNum(4))
        self.textBrowser_5.setHtml(randomNum(5))
        self.textBrowser_6.setHtml(randomNum(1))
        self.textBrowser_7.setHtml(randomNum(2))
        self.textBrowser_8.setHtml(randomNum(3))
        self.textBrowser_9.setHtml(randomNum(4))
        self.textBrowser_10.setHtml(randomNum(5))
        self.textBrowser_11.setHtml(randomNum(1))
        self.textBrowser_12.setHtml(randomNum(2))
        self.textBrowser_13.setHtml(randomNum(3))
        self.textBrowser_14.setHtml(randomNum(4))
        self.textBrowser_15.setHtml(randomNum(5))
        #获取下注的倍率
        num = int(self.spinBox.text())
        award = self.spinBox_2.text()
        

        html_str = '你选择:'+ str(num) + '  连线,单线投入: '+ str(award)
        str_data,str_data1,str_data2 = [],[],[]
        return_num = 0
        
        return_num_2,return_num_3,return_num_4,return_num_5,return_num_6,return_num_7,return_num_8,return_num_9 = 0,0,0,0,0,0,0,0
        if num == 1:
            str_data = rowCount(self)
            return_num = numTop(str_data,int(award))
            str_str = '  结果： 中奖 ：' + str(return_num)
            html_str = html_str + '  ,线路1值' + str(str_data) + str_str
            self.textBrowser_16.setHtml(html_str)
        elif num == 2:#2条线
            str_data = rowCount(self)
            return_num = numTop(str_data,int(award))
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            num_sum = return_num + return_num_2
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + str_str
            self.textBrowser_16.setHtml(html_str)
        elif num == 3:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            num_sum = return_num + return_num_2 + return_num_3
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 4:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount3(self)
            return_num_4 = numTop(str_data2,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 5:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount4(self)
            return_num_4 = numTop(str_data3,int(award))
            str_data4 = rowCount5(self)
            return_num_5 = numTop(str_data4,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4 + return_num_5
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3)  + ', 线路5值 ' + str(str_data4) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 6:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount4(self)
            return_num_4 = numTop(str_data3,int(award))
            str_data4 = rowCount5(self)
            return_num_5 = numTop(str_data4,int(award))
            str_data5 = rowCount6(self)
            return_num_6 = numTop(str_data5,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4 + return_num_5 + return_num_6
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3)  + ', 线路5值 ' + str(str_data4)  + ', 线路6值 ' + str(str_data5) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 7:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount4(self)
            return_num_4 = numTop(str_data3,int(award))
            str_data4 = rowCount5(self)
            return_num_5 = numTop(str_data4,int(award))
            str_data5 = rowCount6(self)
            return_num_6 = numTop(str_data5,int(award))
            str_data6 = rowCount7(self)
            return_num_7 = numTop(str_data6,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4 + return_num_5 + return_num_6 + return_num_7
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3)  + ', 线路5值 ' + str(str_data4)  + ', 线路6值 ' + str(str_data5) + ' , 线路7值' + str(str_data6) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 8:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount4(self)
            return_num_4 = numTop(str_data3,int(award))
            str_data4 = rowCount5(self)
            return_num_5 = numTop(str_data4,int(award))
            str_data5 = rowCount6(self)
            return_num_6 = numTop(str_data5,int(award))
            str_data6 = rowCount7(self)
            return_num_7 = numTop(str_data6,int(award))
            str_data7 = rowCount8(self)
            return_num_8 = numTop(str_data7,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4 + return_num_5 + return_num_6 + return_num_7 + return_num_8
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3)  + ', 线路5值 ' + str(str_data4)  + ', 线路6值 ' + str(str_data5) + ' , 线路7值' + str(str_data6) + ' ，线路8值 ' + str(str_data7) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        elif num == 9:
            str_data1 = rowCount2(self)
            return_num_2 = numTop(str_data1,int(award))
            str_data2 = rowCount3(self)
            return_num_3 = numTop(str_data2,int(award))
            str_data3 = rowCount4(self)
            return_num_4 = numTop(str_data3,int(award))
            str_data4 = rowCount5(self)
            return_num_5 = numTop(str_data4,int(award))
            str_data5 = rowCount6(self)
            return_num_6 = numTop(str_data5,int(award))
            str_data6 = rowCount7(self)
            return_num_7 = numTop(str_data6,int(award))
            str_data7 = rowCount8(self)
            return_num_8 = numTop(str_data7,int(award))
            str_data8 = rowCount9(self)
            return_num_9 = numTop(str_data8,int(award))
            num_sum = return_num + return_num_2 + return_num_3 + return_num_4 + return_num_5 + return_num_6 + return_num_7 + return_num_8 + return_num_9
            str_str = '  结果： 中奖 ：' + str(num_sum)
            html_str = html_str + '  ,线路1值' +  str(str_data)
            html_str = '      ' + html_str + '  ,线路2值' + str(str_data1) + ', 线路3值 ' + str(str_data2) + ' , 线路4值' + str(str_data3)  + ', 线路5值 ' + str(str_data4)  + ', 线路6值 ' + str(str_data5) + ' , 线路7值' + str(str_data6) + ' ，线路8值 ' + str(str_data7) + ', 线路9值' + str(str_data8) + str_str
            
            self.textBrowser_16.setHtml(html_str)
        else:
            #self.textBrowser_16.setHtml('等待后续完成')
            str_data = rowCount(self)
            return_num = numTop(str_data,int(award))
        # if return_num == 0:
        #     str_str = '   结果：   未中奖'
        # else :
            str_str = '  结果： 中奖 ：' + str(return_num)
            html_str = html_str + '  ,线路1值' + str(str_data) + str_str
            self.textBrowser_16.setHtml(html_str)

    
#计算概率
def randomNum(num_1):
    #定义一个字典
    if num_1 == 1:
        weight_data = {'香蕉':400,'苹果':210,'草莓':120,'黄桃':60,'三叶草':50,'777':40,'蓝莓':30,'葡萄':1,'WILD':5,'BONUS':5,'BAR':7}
    elif num_1 == 2:
        weight_data = {'香蕉':350,'苹果':150,'草莓':80,'黄桃':70,'三叶草':70,'777':70,'蓝莓':65,'葡萄':55,'WILD':25,'BONUS':15,'BAR':50}
    elif num_1 == 3:
        weight_data = {'香蕉':300,'苹果':150,'草莓':100,'黄桃':70,'三叶草':60,'777':60,'蓝莓':60,'葡萄':60,'WILD':60,'BONUS':50,'BAR':30}
    elif num_1 == 4:
        weight_data = {'香蕉':150,'苹果':130,'草莓':120,'黄桃':100,'三叶草':100,'777':80,'蓝莓':80,'葡萄':80,'WILD':80,'BONUS':70,'BAR':10}
    else:
        weight_data = {'香蕉':80,'苹果':90,'草莓':90,'黄桃':65,'三叶草':65,'777':90,'蓝莓':100,'葡萄':100,'WILD':120,'BONUS':150,'BAR':50}
    
    total = sum(weight_data.values())    # 权重求和
    ra = random.uniform(0, total)   # 在0与权重和之前获取一个随机数 
    curr_sum = 0
    ret = None
    keys = weight_data.keys()
    for k in keys:
        curr_sum += weight_data[k]             # 在遍历中，累加当前权重值
        if ra <= curr_sum:          # 当随机数<=当前权重和时，返回权重key
            ret = k
            break
    html = '<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\"><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">'+ ret +'</span></p></body></html>'
    return html

#获取条数
def rowCount(val):
    str_data1 = []
    #查看线路1有误中奖
    cell_6 = val.textBrowser_6.toPlainText()
    cell_7 = val.textBrowser_7.toPlainText()
    cell_8 = val.textBrowser_8.toPlainText()
    cell_9 = val.textBrowser_9.toPlainText()
    cell_10 = val.textBrowser_10.toPlainText()

    str_data1.append(cell_6)
    str_data1.append(cell_7)
    str_data1.append(cell_8)
    str_data1.append(cell_9)
    str_data1.append(cell_10)
    return str_data1
#获取条数2
def rowCount2(val):
    str_data1 = []
    cell_1 = val.textBrowser.toPlainText()
    cell_2 = val.textBrowser_2.toPlainText()
    cell_3 = val.textBrowser_3.toPlainText()
    cell_4 = val.textBrowser_4.toPlainText()
    cell_5 = val.textBrowser_5.toPlainText()

    str_data1.append(cell_1)
    str_data1.append(cell_2)
    str_data1.append(cell_3)
    str_data1.append(cell_4)
    str_data1.append(cell_5)
    return str_data1
#获取条数3
def rowCount3(val):
    str_data = []
    cell_11 = val.textBrowser_11.toPlainText()
    cell_12 = val.textBrowser_12.toPlainText()
    cell_13 = val.textBrowser_13.toPlainText()
    cell_14 = val.textBrowser_14.toPlainText()
    cell_15 = val.textBrowser_15.toPlainText()

    str_data.append(cell_11)
    str_data.append(cell_12)
    str_data.append(cell_13)
    str_data.append(cell_14)
    str_data.append(cell_15)
    return str_data
#获取条数4
def rowCount4(val):
    str_data = []
    cell_1 = val.textBrowser.toPlainText()
    cell_7 = val.textBrowser_7.toPlainText()
    cell_13 = val.textBrowser_13.toPlainText()
    cell_9 = val.textBrowser_9.toPlainText()
    cell_5 = val.textBrowser_5.toPlainText()

    str_data.append(cell_1)
    str_data.append(cell_7)
    str_data.append(cell_13)
    str_data.append(cell_9)
    str_data.append(cell_5)
    return str_data
#获取条数5
def rowCount5(val):
    str_data = []
    cell_11 = val.textBrowser_11.toPlainText()
    cell_7 = val.textBrowser_7.toPlainText()
    cell_3 = val.textBrowser_3.toPlainText()
    cell_9 = val.textBrowser_9.toPlainText()
    cell_15 = val.textBrowser_15.toPlainText()

    str_data.append(cell_11)
    str_data.append(cell_7)
    str_data.append(cell_3)
    str_data.append(cell_9)
    str_data.append(cell_15)
    return str_data
#获取条数6
def rowCount6(val):
    str_data = []
    cell_1 = val.textBrowser.toPlainText()
    cell_2 = val.textBrowser_2.toPlainText()
    cell_8 = val.textBrowser_8.toPlainText()
    cell_14 = val.textBrowser_14.toPlainText()
    cell_15 = val.textBrowser_15.toPlainText()

    str_data.append(cell_1)
    str_data.append(cell_2)
    str_data.append(cell_8)
    str_data.append(cell_14)
    str_data.append(cell_15)
    return str_data
#获取条数7
def rowCount7(val):
    str_data = []
    cell_11 = val.textBrowser_11.toPlainText()
    cell_12 = val.textBrowser_12.toPlainText()
    cell_8 = val.textBrowser_8.toPlainText()
    cell_4 = val.textBrowser_4.toPlainText()
    cell_5 = val.textBrowser_5.toPlainText()

    str_data.append(cell_11)
    str_data.append(cell_12)
    str_data.append(cell_8)
    str_data.append(cell_4)
    str_data.append(cell_5)
    return str_data
#获取条数8
def rowCount8(val):
    str_data = []
    cell_6 = val.textBrowser_6.toPlainText()
    cell_12 = val.textBrowser_12.toPlainText()
    cell_8 = val.textBrowser_8.toPlainText()
    cell_4 = val.textBrowser_4.toPlainText()
    cell_10 = val.textBrowser_10.toPlainText()

    str_data.append(cell_6)
    str_data.append(cell_12)
    str_data.append(cell_8)
    str_data.append(cell_4)
    str_data.append(cell_10)
    return str_data
#获取条数9
def rowCount9(val):
    str_data = []
    cell_6 = val.textBrowser_6.toPlainText()
    cell_2 = val.textBrowser_2.toPlainText()
    cell_8 = val.textBrowser_8.toPlainText()
    cell_14 = val.textBrowser_14.toPlainText()
    cell_10 = val.textBrowser_10.toPlainText()

    str_data.append(cell_6)
    str_data.append(cell_2)
    str_data.append(cell_8)
    str_data.append(cell_14)
    str_data.append(cell_10)
    return str_data

#判断是否中奖
def numTop(dataList,award):

    award_val_2 = {"香蕉":1}
    award_val_3 = {"香蕉":3,"草莓":3,"黄桃":15,"蓝莓":25,"三叶草":30,"苹果":35,"葡萄":45,"BAR":75,"BONUS":25,"777":100}
    award_val_4 = {"香蕉":10,"草莓":10,"黄桃":40,"蓝莓":50,"三叶草":70,"苹果":80,"葡萄":100,"BAR":175,"BONUS":50,"777":200}
    award_val_5 = {"香蕉":75,"草莓":85,"黄桃":250,"蓝莓":400,"三叶草":550,"苹果":650,"葡萄":800,"BAR":1250,"BONUS":400,"777":1750}

    # dataList = ['黄桃', '黄桃', '黄桃', '黄桃', '黄桃']
    # award = 100

    for i in range(0,len(dataList)):
        print(dataList[i])
        if dataList[i] == dataList[i+1]:
            #中奖
            if dataList[i] == dataList[i+2]:
                #如果是香蕉就是3倍 草莓3倍 黄桃15倍 蓝莓25 三叶草30倍 苹果35倍 葡萄45倍 BAR75倍 BONUS25倍 777 10倍
                if dataList[i] == dataList[i+3]:
                    if dataList[i] == dataList[i+4]:
                        sum_award = (award) * award_val_5[dataList[i]] # 赢取5倍
                        return sum_award
                    else :
                        sum_award = (award) * award_val_4[dataList[i]] # 赢取4倍
                        return sum_award
                else :
                    sum_award = (award) * award_val_3[dataList[i]] # 赢取3倍
                    return sum_award
            else :
                if award_val_2.get(dataList[i]):
                    sum_award = (award) * award_val_2[dataList[i]] # 赢取2倍
                else :
                    sum_award = 0
                return sum_award
        else :
            #未中奖
            print('未中奖')
            return 0

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = fruit()
    window.show()
    sys.exit(app.exec_())