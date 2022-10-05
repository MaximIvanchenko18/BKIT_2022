from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import sys
from PyQt6.QtWidgets import QApplication, QPushButton


def main():
    r = Rectangle("синего", 5, 10)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

    # Проверяем работу pyqt6:
    app = QApplication(sys.argv)
    window = QPushButton("Hello, world!")
    window.show()
    app.exec()
    #


if __name__ == "__main__":
    main()
