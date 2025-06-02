## App that translates latin numerals back OR FORTH
## Shows rules and numerals table, uses randint to quiz players

import sys
from gui import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    """
    Main function.
    Runs the app creating main window.
    """

    # Show main window on run    
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == "__main__":
    main()