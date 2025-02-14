## App that translates latin numerals back OR FORTH
## Shows rules and numerals table, uses randint to quiz players


from gui import MainWindow
from PyQt5.QtWidgets import QApplication



def main():

    # Show main window on run    
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == "__main__":
    main()