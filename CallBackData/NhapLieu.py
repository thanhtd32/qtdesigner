import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets

from SanPham import SanPham


class frmNhapLieu(QDialog):

    def __init__(self):
        super(frmNhapLieu, self).__init__()
        loadUi('frmNhapLieu.ui',self)
        self.btnLuu.clicked.connect(self.xuLyLuu)
        self.ref=None
    def xuLyLuu(self):
        #lấy dữ liệu trên giao diện
        ma= self.txtMa.text()
        ten=self.txtTen.text()
        #khởi tạo thành đối tượng sản phẩm
        sp=SanPham(ma,ten)
        #gửi đối tượng ngược lại cho màn hình chính (gọi là callBack)
        self.ref.luuDuLieu(sp)