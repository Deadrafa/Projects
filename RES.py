from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import json
from PySide6.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle('Таблица Результатов')
        self.setWindowIcon(QIcon('iconTitl.svg'))
        
        table_widget = QTableWidget()
        table_widget.setRowCount(5)  # Устанавливаем количество строк
        table_widget.setColumnCount(5)  # Устанавливаем количество столбцов

# CSS Стили для таблицы замена QML закомментировать если нужно держаться строго заданию ;(
        table_widget.setStyleSheet("""
    QTableWidget {
        background-color: #B958A5; 
        color: #000000;  
    }
    
    QTableWidget::item {
        padding: 5px;  
    }
    
    QTableWidget::item:selected {
        background-color: #000000;  
    }
    
    QHeaderView::section {
        background-color: #6EDCD9;  
        color: black;  
        padding: 5px;  
    }
""")
        
        # Заполнение таблицы данными
        for i, (key, value) in enumerate(data.items()):
            if i == 5:
                break
            table_widget.setItem(i, 0, QTableWidgetItem(str(key)))
            table_widget.setItem(i, 1, QTableWidgetItem(str(value['Нагрудный номер'])))
            table_widget.setItem(i, 2, QTableWidgetItem(value['Имя']))
            table_widget.setItem(i, 3, QTableWidgetItem(value['Фамилия']))
            table_widget.setItem(i, 4, QTableWidgetItem(str(value['Результат'])))

            headers = ['Занятое место', 'Номер', 'Имя', 'Фамилия', 'Результат']
            table_widget.setHorizontalHeaderLabels(headers)

        layout = QVBoxLayout()
        layout.addWidget(table_widget)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    with open('Result.json', encoding='utf-8') as f:
            data = json.load(f)

# Выводим значение по ключу
            i = 0
            for key, value in data.items():
                data = {key: {'Нагрудный номер': value['Нагрудный номер'], 'Имя': value['Имя'], 'Фамилия': value['Фамилия'], 'Результат': value['Результат']} for key, value in data.items()}
                i += 1
                if i == 5:
                     break

    my_window = MyWindow(data)
    my_window.setGeometry(550, 300, 545, 350)
    my_window.show()
    app.exec()