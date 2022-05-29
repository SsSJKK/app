from typing import List
from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
import sys
from PyQt5.QtWidgets import  QFileDialog



class mywindow(QtWidgets.QMainWindow):
  files = List[str]
  files_len = 0

  def __init__(self):
    super(mywindow, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.ui.pushButton.clicked.connect(self.openFileNamesDialog)
    self.ui.pushButton_2.clicked.connect(self.files_processing)

  def openFileNamesDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    self.files, _ = QFileDialog.getOpenFileNames(
        self, "Выберите файлы для обработки", "", "txxt (*.txt)", options=options)
    self.files_len = len(self.files)
    if self.files:
      self.ui.label_2.setText(f"Выбрано файлов {self.files_len}")

  def file_processing(self, file_name):
    f = open(file_name)
    d = f.read()
    f.close()
    l1 = d.split('\n')
    l2 = [x for x in l1 if x != '']
    new_data = ''
    for x in range(0, len(l2)-1, 2):
      new_data += f'{l2[x]}{l2[x+1]}\n\n'
    n_f_n = file_name.split('/')
    n_f_n[-1] = 'new_'+n_f_n[-1]
    fn = '/'.join(n_f_n)
    n_f = open(fn, 'w')
    n_f.write(new_data)
    n_f.close()

  def files_processing(self):
    for f in self.files:
      self.file_processing(f)
    self.files = List[str]
    self.ui.label_2.setText('Обработано')


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
