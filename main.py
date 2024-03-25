import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QMessageBox, QWidget, QLabel
from sort_orig import calculate_race_times, sort_times
from jsVid import process_files
import os
import subprocess
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
'''#Не успел разобраться с QML ;( 
# Использовал CSS не судите строго :)
# Надеюсь просмотрите код, первый раз просто присылай рабботы, постарался всё рассписать чтобы было понятно )'''


'''Они будут создаваться по ходу выполнение программы, просто чтоб не пугали
# sorted_times.txt - Там лежит раздница во времени и номерной знак, отсортированные уже
# output_data.txt - Там лежит тоже самое что и в sorted_times.txt, но только уже с привязанымми именем и фалилией
# Result.json - Мой файл для выведения таблицы там уже лежат результаты в виде json
# После того как вы сохраните свой Json файл, моя программа "уберёт за собой" xD ранее перечисленные файлы xD '''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Результаты спортсменов")
        self.setWindowIcon(QIcon('iconTitl.svg'))
        layout = QVBoxLayout()

        # CSS Стили для кнопок замена QML закомментировать если нужно держаться строго заданию ;(
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
        
        
        #Внешка кнопок ну и их назначение
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

        # CSS Стили для кнопок замена QML закомментировать если нужно держаться строго заданию ;(
        self.btn_load_competitors.setStyleSheet(button_style)
        self.btn_load_results.setStyleSheet(button_style)
        self.btn_calculate.setStyleSheet(button_style)
        self.btn_save_results.setStyleSheet(button_style)

        # Для icon выделил место и прописал размеры
        self.table = QTableWidget()
        icon = QIcon("Olym.svg")
        iconLabel = QLabel()
        iconLabel.setPixmap(icon.pixmap(400, 400))
        layout.addWidget(iconLabel)

        iconLabel.setAlignment(Qt.AlignCenter)

        # CSS Стили для окна приложения замена QML закомментировать если нужно держаться строго заданию ;(
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  #6EDCD9, stop:1 #E15FED);")

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Функционал кнопок
        

    # Далее по плану json файл, откройте jsVid.py, там напишу как работает
    def load_competitors_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл json", "", "JSON Файлы (*.json)")
        if file_path:
                # Это для пользователя который сначало захочет начать с json файла
                try:
                    process_files(file_path, 'sorted_times.txt')
                    # Для себя)
                    # print(file_path)
                except FileNotFoundError as e:
                    error_message = f"Пожалуйста введите сначала файл *.txt: {e}"
                    QMessageBox.critical(self, "Error", error_message)

    # Начинаю я с txt файла, откройте  sort_orig.py, там напишу как работает
    def load_results_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл txt", "", "Текстовые файлы (*.txt)")
        if file_path:
            calculate_race_times(file_path)
            sort_times('sorted_times.txt')

    # Тут это для таблицы
    def calculate_results(self):
        # Это если пользователь захочет сразу результат посмотреть
        try:
            with open('output_data.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError as e:
            error_message = f"Пожалуйста сначала введите все нужные для работы файлы *.txt и *.json: {e}"
            QMessageBox.critical(self, "Error", error_message)
        # Тут я перевожу свой txt файл output_data.txt в json
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
            
        # Это нужно программе чтоб результат в таблицу внести
        with open('Result.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # Тут как раз таки вызываю таблицу, просто я не понял как её сделать в приложении и сделала отдельно)
        subprocess.call(["python", "RES.py"])

    # Это уже сохранение итога в видде json
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
                    # Тут правило, нагадил убери xD
                    # И это уже крайняя операция
                    file_paths = ["output_data.txt", "sorted_times.txt", 'Result.json']
                    
                    # Это для меня чтоб понимать есть ли файл
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