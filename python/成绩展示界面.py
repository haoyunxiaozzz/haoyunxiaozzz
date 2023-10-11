from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox

class stu():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.setWindowTitle('成绩统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText('请输入成绩表')
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)
        self.button.clicked.connect(self.handlecalc)
    def handlecalc(self):
        text = self.textEdit.toPlainText()
        QMessageBox.about(self.window,'结果','成绩有：%s'%text)

app = QApplication([])
stu = stu()
stu.window.show()
app.exec_()