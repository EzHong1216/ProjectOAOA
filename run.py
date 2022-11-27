import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from get_whois import get_whois
from get_ip import get_ip
from get_robot import get_robot
from domain import get_domain_name
from port_scan import scan_port, is_Valid_Port
from web_weak_scan import web_weak_scanner

#UI파일 연결
form_class = uic.loadUiType("./PortScanner.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #whois 탭 기능 연결
        self.whois_GoButton.clicked.connect(self.whois_GoFunc)
        self.whois_Input.returnPressed.connect(self.whois_GoFunc)
        self.whois_SaveButton.clicked.connect(self.whois_SaveFunc)
        
        #ip추출 탭 기능 연결
        self.ipget_GoButton.clicked.connect(self.ipget_GoFunc)
        self.ipget_Input.returnPressed.connect(self.ipget_GoFunc)
        
        #robot추출 탭 기능 연결
        self.robot_GoButton.clicked.connect(self.robot_GoFunc)
        self.robot_Input.returnPressed.connect(self.robot_GoFunc)
        
        #domain추출 탭 기능 연결
        self.domain_IsSub = True
        self.domain_GoButton.clicked.connect(self.domain_GoFunc)
        self.domain_Input.returnPressed.connect(self.domain_GoFunc)
        self.domain_RadioSub.clicked.connect(self.domain_RadioFunc)
        self.domain_RadioMain.clicked.connect(self.domain_RadioFunc)
        
        #port스캔 탭 기능 연결
        self.port_GoButton.clicked.connect(self.port_GoFunc)
        
        #취약점검 탭 기능 연결
        self.weak_GoButton.clicked.connect(self.weak_GoFunc)
        self.weak_URLInput.returnPressed.connect(self.weak_GoFunc)
        self.weak_ListGoButton.clicked.connect(self.weak_GoListFunc)
        self.weak_LogSaveButton.clicked.connect(self.weak_SaveLogFunc)
        self.weak_LogExcelButton.clicked.connect(self.weak_SaveExcelFunc)
        self.weak_scanner = web_weak_scanner()
    
#Whois 탭 메소드
    #입력창에 있는 값으로 whois 결과 추출
    def whois_GoFunc(self):
        result = get_whois(self.whois_Input.text())
        self.whois_LogBox.setPlainText(result)
    
    #입력창에 있는 값을 JSON 파일로 저장
    def whois_SaveFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./whois_result.json', filter='JSON (*.json)')
        if filename == "":
            return
        with open(filename[0], 'w') as f:
            f.write(self.whois_LogBox.toPlainText())
            
#ip추출 탭 메소드
    #입력창에 있는 URL로 ip추출
    def ipget_GoFunc(self):
        result = get_ip(self.ipget_Input.text())
        self.ipget_Result.setText(result)
    
#robot추출 탭 메소드
    #입력창에 있는 URL에서 robots.txt 추출후 저장
    def robot_GoFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./robots.txt', filter='txt (*.txt)')
        if filename == "":
            return
        if self.robot_Input.text() == "":
            return
        result = get_robot(self.robot_Input.text())
        with open(filename[0], 'w') as f:
            f.write(result)

#domain추출 탭 메소드
    def domain_RadioFunc(self):
        if self.domain_RadioSub.isChecked():
            self.domain_IsSub = True
        elif self.domain_RadioMain.isChecked():
            self.domain_IsSub = False
    
    def domain_GoFunc(self):
        result = get_domain_name(self.domain_Input.text())
        self.domain_Result.setText(result)

#port스캔 탭 메소드
    def port_GoFunc(self):
        if self.port_PortMax.value() < self.port_PortMin.value():
            self.port_Result.setText("스캔할 포트의 범위가 유효하지 않습니다")
            return
        
        self.port_Result.setText("")
        total_result = {}
        for i in range(1, self.port_LoopNum.value()+1):
            self.port_Result.append(f"{i}회차")
            loop_result = scan_port(self.port_IPInput.text(), self.port_PortMin.value(), self.port_PortMax.value())
            
            for p in range(self.port_PortMin.value(), self.port_PortMax.value()+1):
                if p in loop_result:
                    self.port_Result.append(f"{p}번 포트 연결됨")
                else:
                    self.port_Result.append(f"{p}번 포트 닫힘")
            self.port_Result.append("")
            
            for p in loop_result:
                try:
                    total_result[p] += 1
                except:
                    total_result[p] = 1
        
        self.port_Result.append(f"접속한 주소: {self.port_IPInput.text()}")
        self.port_Result.append(f"총 {self.port_LoopNum.value()}번 접속 시도 하였습니다")
        if len(total_result) == 0:
            self.port_Result.append(f"연결된 포트 없음")
            return
        for key, value in total_result.items():
            self.port_Result.append(f"{key}번 포트에 {value}회 연결됨")
            
#취약점검 탭 메소드
    def weak_GoFunc(self):
        self.weak_Result.setText("")
        result = self.weak_scanner.scan([self.weak_URLInput.text()])
        for s in result:
            self.weak_Result.append(s)
    
    def weak_GoListFunc(self):
        self.weak_Result.setText("")
        filename = QFileDialog.getOpenFileName(self, caption='Open List', directory='./', filter='txt (*.txt)')
        if filename == "":
            return
        with open(filename[0], 'r') as f:
            urls = f.readlines()
            result = self.weak_scanner.scan(urls)
            for s in result:
                self.weak_Result.append(s)
    
    def weak_SaveLogFunc(self):
        result = self.weak_Result.toPlainText()
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./robots.txt', filter='txt (*.txt)')
        if filename == "":
            return
        with open(filename[0], 'w') as f:
            f.write(result)
    
    def weak_SaveExcelFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./result.xlsx', filter='Excel file (*.xlsx)')
        if filename == "":
            return
        self.weak_scanner.save_Excel(filename[0])

def main():
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    
    
    
if __name__ == "__main__" :
    main()