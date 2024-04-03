import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QMessageBox, QWidget, QLabel
from sort_orig import calculate_race_times, sort_times
from jsVid import process_files
import os
import subprocess
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
#Не успел разобраться с QML ;(
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Результаты спортсменов")
        self.setWindowIcon(QIcon('iconTitl.svg'))
        layout = QVBoxLayout()

        button_style = """
        QPushButton {
        background-color: #B958A5;
        border-radius: 15px;
        border: none;
        color: white;
        padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #000000;
            }"""
        
        

        self.btn_load_competitors = QPushButton("Загрузить файл *.json")
        self.btn_load_competitors.clicked.connect(self.load_competitors_file)
        layout.addWidget(self.btn_load_competitors)

        self.btn_load_results = QPushButton("Загрузить файл *.txt")
        self.btn_load_results.clicked.connect(self.load_results_file)
        layout.addWidget(self.btn_load_results)

        self.btn_calculate = QPushButton("Вычислить результаты")
        self.btn_calculate.clicked.connect(self.calculate_results)
        layout.addWidget(self.btn_calculate)

        self.btn_save_results = QPushButton("Сохранить результаты в JSON")
        self.btn_save_results.clicked.connect(self.save_results_json)
        layout.addWidget(self.btn_save_results)


        self.btn_load_competitors.setStyleSheet(button_style)
        self.btn_load_results.setStyleSheet(button_style)
        self.btn_calculate.setStyleSheet(button_style)
        self.btn_save_results.setStyleSheet(button_style)

        self.table = QTableWidget()
        icon = QIcon("Olym.svg")
        iconLabel = QLabel()
        iconLabel.setPixmap(icon.pixmap(400, 400))
        layout.addWidget(iconLabel)

        iconLabel.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  #6EDCD9, stop:1 #E15FED);")

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_competitors_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл json", "", "JSON Файлы (*.json)")
        if file_path:
                try:
                    process_files(file_path, 'sorted_times.txt')
                    print(file_path)
                except FileNotFoundError as e:
                    error_message = f"Пожалуйста введите сначала файл *.txt: {e}"
                    QMessageBox.critical(self, "Error", error_message)

    def load_results_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл txt", "", "Текстовые файлы (*.txt)")
        if file_path:
            calculate_race_times(file_path)
            sort_times('sorted_times.txt')

    def calculate_results(self):
        try:
            with open('output_data.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError as e:
            error_message = f"Пожалуйста сначала введите все нужные для работы файлы *.txt и *.json: {e}"
            QMessageBox.critical(self, "Error", error_message)

        data = {}
        item_id = 1

        for line in lines:
            values = line.split()
            data[str(item_id)] = {
                "Нагрудный номер": values[0],
                "Имя": values[1],
                "Фамилия": values[2],
                "Результат": values[3][2:-4]
                }
            item_id += 1
            
        with open('Result.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        subprocess.call(["python", "RES.py"])


    def save_results_json(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить результаты в JSON", "", "JSON Файлы (*.json)")
        if file_path:
                with open('output_data.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    
                    data = {}
                    item_id = 1

                    for line in lines:
                        values = line.split()
                        data[str(item_id)] = {
                            "Нагрудный номер": values[0],
                            "Имя": values[1],
                            "Фамилия": values[2],
                            "Результат": values[3][2:-4]
                            }
                        item_id += 1


                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                    file_paths = ["output_data.txt", "sorted_times.txt", 'Result.json']
                    

                    for file_path in file_paths:
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            print(f"Файл {file_path} успешно удален")
                        else:
                            print(f"Файл {file_path} не существует")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(550, 300, 700, 600)


    window.show()
    sys.exit(app.exec())