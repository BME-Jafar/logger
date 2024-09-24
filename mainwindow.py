# This Python file uses the following encoding: utf-8
import sys
import pandas as pd
import datetime
import json
import os
import warnings

# Suppress a specific warning
warnings.filterwarnings("ignore")  # Replace UserWarning with the specific warning type you want to ignore


from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtUiTools import QUiLoader


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

global counter
global df

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        global df
        if not os.path.exists("logs"):
            os.makedirs("logs")

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create a sample DataFrame
        data = {
            'Timestamp': [],
            'Comment': []
        }
        df = pd.DataFrame(data)
        self.showTabel(df, self.ui.tableView)
        self.ui.startNewButton.clicked.connect(self.startNewExperiment)
        self.ui.timeStampButton.clicked.connect(self.getTimeStamp)
        self.ui.commentButton.clicked.connect(self.addComment)
        self.ui.endExportButton.clicked.connect(self.endAndExport)


    def showTabel(self, df, tabelWiget):
        labels = list(df.columns)
        model = QStandardItemModel(len(df), len(labels))
        model.setHorizontalHeaderLabels(labels)

        for row in range(len(df)):
            for col in range(len(labels)):
                item = QStandardItem(str(df.iloc[row, col]))
                model.setItem(row, col, item)
                print(df.iloc[row, col])

        tabelWiget.setModel(model)

    def startNewExperiment(self):
        global counter
        counter = 0
        name = self.ui.nameText.toPlainText()
        id = self.ui.idText.toPlainText()
        DOB = self.ui.DOBEdit.dateTime().toString("dd-MM-yyyy")
        sex = self.ui.sexBox.currentText()

        if not name or not id:
            self.show_error_message("No name and / or ID!")
            return

        self.ui.nameText.setEnabled(False)
        self.ui.idText.setEnabled(False)
        self.ui.DOBEdit.setEnabled(False)
        self.ui.sexBox.setEnabled(False)
        self.ui.timeStampButton.setEnabled(True)
        self.ui.endExportButton.setEnabled(True)
        self.ui.startNewButton.setEnabled(False)

    def show_error_message(self, msg):
        # Create and show an error message box
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(msg)
        error_box.setStandardButtons(QMessageBox.Ok)

        # Show the message box and wait for user interaction
        error_box.exec()

    def getTimeStamp(self):
        global df
        global counter
        ct = datetime.datetime.now()
        data = {
            'Timestamp': ct,
            'Comment': []
        }
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        self.showTabel(df, self.ui.tableView)
        self.ui.timeStampButton.setEnabled(False)
        self.ui.commentButton.setEnabled(True)

    def addComment(self):
        global df
        global counter
        comment = self.ui.commentText.toPlainText()
        df.iloc[counter, 1] = comment
        counter = counter + 1
        self.ui.timeStampButton.setEnabled(True)
        self.ui.commentButton.setEnabled(False)
        self.showTabel(df, self.ui.tableView)
        self.ui.commentText.clear()

    def endAndExport(self):
        # Create a confirmation message box
        confirmation_box = QMessageBox()
        confirmation_box.setIcon(QMessageBox.Question)
        confirmation_box.setWindowTitle("Confirmation")
        confirmation_box.setText("Are you sure you want to end the experiment")
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.setDefaultButton(QMessageBox.No)

        # Show the message box and wait for user interaction
        response = confirmation_box.exec()

        # Check the user's response
        if response == QMessageBox.Yes:
            global df
            global counter
            name = self.ui.nameText.toPlainText()
            id = self.ui.idText.toPlainText()
            DOB = self.ui.DOBEdit.dateTime().toString("dd-MM-yyyy")
            sex = self.ui.sexBox.currentText()
            dublication = 2
            while(True):

                if not os.path.exists("logs/" + id):
                    os.makedirs("logs/" + id)
                    Path = "logs/" + id + "/"
                    break
                elif not os.path.exists("logs/" + id + "_" + str(dublication)):
                    os.makedirs("logs/" + id + "_" + str(dublication))
                    Path = "logs/" + id + "_" + str(dublication) + "/"
                    break
                else:
                    dublication = dublication + 1

            df.to_csv(Path + id + ".csv")
            data = {
                'Name': name,
                'ID': id,
                'DOB': DOB,
                'sex': sex,
            }
            json_string = json.dumps(data, indent=4)
            # Write to text file
            with open(Path + id + ".txt", 'w') as file:
                file.write(json_string)

            data = {
                'Timestamp': [],
                'Comment': []
            }
            df = pd.DataFrame(data)
            self.ui.nameText.setEnabled(True)
            self.ui.idText.setEnabled(True)
            self.ui.DOBEdit.setEnabled(True)
            self.ui.sexBox.setEnabled(True)
            self.ui.timeStampButton.setEnabled(False)
            self.ui.endExportButton.setEnabled(False)
            self.ui.startNewButton.setEnabled(True)

        else:
            return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
