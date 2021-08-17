import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QApplication, QMainWindow, QTableWidget
from PyQt5 import QtWidgets, QtCore, QtGui

import NhapLieu
#nạp giao diện
Ui_MainWindow, QtBaseClass = uic.loadUiType('frmMain.ui')

class frmMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnMoFormNhapLieu.clicked.connect(self.moFormNhapLieu)

    def moFormNhapLieu(self):
        fNhapLieu.setModal(True)
        fNhapLieu.show()
    #đây là hàm call back của main, từ màn hình chi tiết khi bấm lưu sẽ gọi hàm này
    #thông qua alias ref
    #truyền đối tượng sản phẩm từ chi tiết qua đây để xử lý
    def luuDuLieu(self,sp):
        #thêm 1 dòng mới cho QTableWidgetItem:
        self.tblSanPham.insertRow(self.tblSanPham.rowCount())
        row=self.tblSanPham.rowCount()-1
        self.tblSanPham.setItem(row, 0, QTableWidgetItem(sp.ma))
        self.tblSanPham.setItem(row, 1, QTableWidgetItem(sp.ten))

if __name__ == "__main__":
    #tạo các đối tượng cho màn hình chính
    app = QtWidgets.QApplication(sys.argv)
    fMain = frmMain()
    fMain.show()
    #màn hình chi tiết
    fNhapLieu = NhapLieu.frmNhapLieu()
    #truyền tham chiếu màn hình chính qua màn hình chi tiết
    #alias lưu tham chiếu này đặt tên là ref (bạn đặt tên gì tùy)
    fNhapLieu.ref=fMain

    sys.exit(app.exec_())