from PyQt5.QtWidgets import QMessageBox
import requests

def dirscan(self):
    url = self.le.text()
    if url == "":
        QMessageBox.about(self, "Notice", "please input address")
    else:
        self.tb.append("Directory Scanning...")

        f = open("./dir_scan_list.txt", 'r')
        while True:
            data = f.readline()
            r = requests.get(url + data)
            if r.status_code == 200:
                self.tb.append("[◈] Connect → " + r.url)
            if not data: break

        self.tb.append("")
        self.le.clear()
        f.close()
