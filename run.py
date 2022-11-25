import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from get_whois import get_whois
from get_ip import get_ip
from get_robot import get_robot

#UI파일 연결
form_class = uic.loadUiType("./PortScanner.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #whois 탭 기능 연결
        self.whoisGoButton.clicked.connect(self.whoisGoFunc)
        self.whoisInput.returnPressed.connect(self.whoisGoFunc)
        self.whoisSaveButton.clicked.connect(self.whoisSaveFunc)
        
        #ip추출 탭 기능 연결
        self.ipget_GoButton.clicked.connect(self.ipget_GoFunc)
        self.ipget_Input.returnPressed.connect(self.ipget_GoFunc)
        
        #robot추출 탭 기능 연결
        self.robot_GoButton.clicked.connect(self.robot_GoFunc)
        self.robot_Input.returnPressed.connect(self.robot_GoFunc)
    
#Whois 탭 메소드
    #입력창에 있는 값으로 whois 결과 추출
    def whoisGoFunc(self):
        result = get_whois(self.whoisInput.text())
        self.whoisLogBox.setPlainText(result)
    
    #입력창에 있는 값을 JSON 파일로 저장
    def whoisSaveFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./whois_result.json', filter='JSON (*.json)')
        with open(filename[0], 'w') as f:
            f.write(self.whoisLogBox.toPlainText())
            
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