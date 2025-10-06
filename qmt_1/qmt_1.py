import sys
import random
from PySide6.QtCore import QRect, QTimer  # <-- Добавил QTimer для задержки
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_qmt_1 import Ui_MainWindow

# count_of_square = 3
#
grid = [
    [50, 50, 40, 50],
    [110, 50, 40, 50],
    [170, 50, 40, 50],
    [50, 110, 40, 50],
    [110, 110, 40, 50],
    [170, 110, 40, 50],
    [50, 170, 40, 50],
    [110, 170, 40, 50],
    [170, 170, 40, 50]
]

class SimpleMemory(QMainWindow):
    def __init__(self):
        super(SimpleMemory, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # все мои переменные

        self.progress = 0
        self.sequence_len = 0
        self.record = 0
        self.grid = grid

        self.time_sleep = 1  # сколько секунд показываются цифры

        self.is_showing = False

        self.buttons = [
            self.ui.square_button_1,
            self.ui.square_button_2,
            self.ui.square_button_3,
            self.ui.square_button_4,
            self.ui.square_button_5,
            self.ui.square_button_6,
            self.ui.square_button_7,
            self.ui.square_button_8,
            self.ui.square_button_9
        ]

        # подключаем все кнопки

        self.ui.start_button.clicked.connect(self.start_handler)

        for i, button in enumerate(self.buttons):
            button.clicked.connect(lambda checked, idx=i: self.user_click(idx))

        # скрываем квадраты
        for i in range(len(self.buttons)):
            self.buttons[i].hide()

        self.ui.label.setText('Нажмите "Начать"')
        self.ui.start_button.setText('Начать')

        print('__init__'.rjust(13, ' '), f'| ok')

    def start_handler(self):
        text = self.ui.start_button.text()
        print('start_handler'.rjust(13, ' '), f'| button text = {text}')
        if text == 'Начать' or text == 'Рестарт':
            self.start_page()
        elif text == 'Старт':
            self.start_game()

    def start_page(self):
        print('start_page'.rjust(13, ' '), f'| len = {self.sequence_len}, rec = {self.record}')

        # text
        self.ui.label.setGeometry(QRect(50, 10, 161, 96))
        if self.sequence_len <= self.record:
            # стандартная надпись
            self.ui.label.setText(f'Нажми на квадраты \nв правильной \nпоследовательности\n\n'
                                  f'Текущая длинна: {self.sequence_len}\nРекорд: {self.record}')
        else:
            # новый рекорд
            self.record = self.sequence_len
            self.ui.label.setText(f'Нажми на квадраты \nв правильной \nпоследовательности\n\n'
                                  f'Поздравляю!\nНовый рекорд: {self.record}')

        # подготовка к старту
        self.sequence_len = 3

        self.ui.start_button.setText('Старт')

        for i in range(len(self.buttons)):
            self.buttons[i].hide()

    def start_game(self):
        print('start_game'.rjust(13, ' '), f'| ts = {self.time_sleep}')

        self.ui.start_button.setText('Рестарт')

        self.ui.label.setGeometry(QRect(50, 10, 161, 31))
        self.ui.label.setText(f'Текущая длинна: {self.sequence_len}\n'
                              f'Рекорд: {self.record}')

        # обновляем значения
        self.progress = 0
        # self.sequence_len = 3

        for i in range(len(self.buttons)):
            self.buttons[i].hide()

        # формируем случайную последовательность
        sequence = list(range(0, self.sequence_len))
        random.shuffle(sequence)
        # print(1, *range(0, self.progress), list(range(0, self.progress)))
        # print(2, sequence)

        self.is_showing = True

        # показываем цифры
        for i in range(self.sequence_len):
            # print('q', self.grid[i])
            self.buttons[sequence[i]].setGeometry(QRect(*self.grid[i]))
            self.buttons[sequence[i]].setText(str(sequence[i]+1))
            self.buttons[sequence[i]].show()

        QTimer.singleShot((self.time_sleep * 1000), self.hide_text)

    def hide_text(self):
        # скрываем текст на кнопках
        for i in range(self.sequence_len):
            self.buttons[i].setText('')

        self.is_showing = False

    def user_click(self, index):
        # print('user_click'.rjust(13, ' '), f'| index = {index}')
        if self.is_showing:  # если идёт показ, игнорируем клики
            return
        else:
            if index < self.progress:  # повтороные клики игнорируем
                return
            elif index == self.progress:
                if index == self.sequence_len - 1:
                    self.sequence_len += 1
                    self.start_game()
                    print('user_click'.rjust(13, ' '), f'| win | len = {self.sequence_len - 1}')
                else:
                    self.progress += 1
                    self.buttons[index].setText(str(index + 1))
                    print('user_click'.rjust(13, ' '), f'| correct_click | progress = {self.progress}')

            else:
                # go to end
                print('user_click'.rjust(13, ' '), f'| go to end')
                self.end_game()

    def end_game(self):
        # рестарт
        print('end_game'.rjust(13, ' '), f'| go to start_page')
        self.start_page()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleMemory()
    window.show()
    sys.exit(app.exec())

