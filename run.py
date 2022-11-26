import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from get_whois import get_whois
from get_ip import get_ip
from get_robot import get_robot
from domain import get_domain_name

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
    
#Whois 탭 메소드
    #입력창에 있는 값으로 whois 결과 추출
    def whois_GoFunc(self):
        result = get_whois(self.whois_Input.text())
        self.whois_LogBox.setPlainText(result)
    
    #입력창에 있는 값을 JSON 파일로 저장
    def whois_SaveFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./whois_result.json', filter='JSON (*.json)')
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
        result = get_robot(self.robot_Input.text())
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./robots.txt', filter='txt (*.txt)')
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