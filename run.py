import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from whois_get import whois_get

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
    
    #입력창에 있는 값으로 whois 결과 추출
    def whoisGoFunc(self):
        result = whois_get(self.whoisInput.text())
        self.whoisLogBox.setPlainText(result)
    
    #입력창에 있는 값을 JSON 파일로 저장
    def whoisSaveFunc(self):
        filename = QFileDialog.getSaveFileName(self, caption='Save Result', directory='./result.json', filter='JSON (*.json)')
        with open(filename[0], 'w') as f:
            f.write(self.whoisLogBox.toPlainText())
            

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