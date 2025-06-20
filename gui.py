import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QPushButton,
    QWidget,
)
from PyQt5.QtCore import Qt
from logic import randomize, handle_translation_input, handle_quiz_input


def resource_path(relative_path):
    """
    This function grabs absolute path to where images are saved
    so that images work for both .py and --onefile .exe executions


    Args:
        relative_path (str): Name of file in folder.

    Returns:
        (str): Absolute path of file location during .exe decompression or .py run.
    """

    # If code is executed through PyInstaller --onefile
    try:
        # _MEIPASS is where .exe's files are temporarily
        # decompressed during code execution
        base_path = sys._MEIPASS

    # This except runs when sys._MEIPASS is not used,
    # meaning when code is executed through .py
    except Exception:
        base_path = os.path.abspath(".")

    # Returns the path where .py is or where .exe is
    # decompressed joined with /L-Icon.png or /arrows.png
    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    """
    Class for the main window of the GUI.

    Contains a "WELCOME" label, buttons for translator, rules, quiz and exiting,
    and a "Made by Black Baron" label.
    """

    # Main window initialization
    def __init__(self):
        super().__init__()

        # Initializing quiz streak property
        self.quiz_streak = 0

        # Window Properties
        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon(resource_path("L-Icon.png")))
        # Different Height for different window scaling settings
        self.setMinimumSize(370, 240)
        self.setMaximumSize(370, 300)

        # Menu Title
        label = QLabel("WELCOME")
        font = label.font()
        font.setFamily("Old English Text MT")
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        label.setMinimumSize(350, 50)

        # Buttons
        translator_btn = QPushButton("Numerals Translator")
        translator_btn.clicked.connect(self.on_translator_btn_clicked)

        rules_btn = QPushButton("Numerals Rules")
        rules_btn.clicked.connect(self.on_rules_btn_clicked)

        quiz_btn = QPushButton("Quiz")
        quiz_btn.clicked.connect(self.on_quiz_btn_clicked)

        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.on_exit_btn_clicked)

        # Made_by_label
        made_by_label = QLabel("Made by Black Baron")
        font.setPointSize(12)
        made_by_label.setFont(font)

        all_btns = [translator_btn, rules_btn, quiz_btn, exit_btn]

        font.setPointSize(16)
        font.setFamily("Times New Roman")

        # Main window layout
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Modifying and adding buttons
        for btn in all_btns:
            btn.setFixedWidth(230)
            btn.setFont(font)
            layout.addWidget(btn, alignment=Qt.AlignCenter)
        layout.addWidget(
            made_by_label, alignment=Qt.AlignRight | Qt.AlignBottom
        )

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def on_translator_btn_clicked(self):
        """
        Main menu translator button function.

        Creates secondary window for translator.
        Window displays translation flow, contains a button for reversing
        translation flow, an entry form to read input and a button to
        translate, and a field to display results.
        """
        # Translator window
        self.translator_wnd = QWidget()
        self.translator_wnd.setWindowTitle("Translator")
        self.translator_wnd.setWindowIcon(QIcon(resource_path("L-Icon.png")))
        self.translator_wnd.setMinimumSize(450, 250)
        self.translator_wnd.setMaximumSize(600, 260)

        # Translate FROM side
        self.translator_wnd.entry_title = QLabel("Latin Numeral")
        font = self.translator_wnd.entry_title.font()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.translator_wnd.entry_title.setFont(font)
        self.translator_wnd.entry_title.setMinimumSize(150, 30)
        self.translator_wnd.entry_title.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )

        # Reverse translation btn
        self.translator_wnd.reverse_btn = QPushButton()
        self.translator_wnd.reverse_btn.setCheckable(True)
        self.translator_wnd.reverse_btn.setIcon(
            QIcon(resource_path("arrows.png"))
        )
        self.translator_wnd.reverse_btn.clicked.connect(
            self.on_reverse_clicked
        )
        self.translator_wnd.reverse_btn.setMinimumSize(30, 30)

        # Translate TO side
        self.translator_wnd.output_title = QLabel("Decimal Number")
        self.translator_wnd.output_title.setFont(font)
        self.translator_wnd.output_title.setMinimumSize(150, 30)
        self.translator_wnd.output_title.setAutoFillBackground(True)
        self.translator_wnd.output_title.setAlignment(
            Qt.AlignRight | Qt.AlignVCenter
        )

        # Upper line, from + reverse + to
        central_upper_layout = QHBoxLayout()
        central_upper_layout.addWidget(self.translator_wnd.entry_title)
        central_upper_layout.addWidget(self.translator_wnd.reverse_btn)
        central_upper_layout.addWidget(self.translator_wnd.output_title)
        central_upper_layout.setAlignment(Qt.AlignCenter)

        # Entry field for translation
        self.translator_wnd.entry = QLineEdit()
        self.translator_wnd.entry.setFont(font)
        self.translator_wnd.entry.setAlignment(Qt.AlignHCenter)
        self.translator_wnd.entry.setMinimumSize(245, 30)

        # translate_btn
        self.translator_wnd.translate_btn = QPushButton("Translate")
        self.translator_wnd.translate_btn.setFont(font)
        self.translator_wnd.translate_btn.setShortcut("Return")
        self.translator_wnd.translate_btn.clicked.connect(
            self.on_translate_clicked
        )
        self.translator_wnd.translate_btn.setMinimumSize(100, 30)

        # Middle line, field + BTN
        middle_layout = QHBoxLayout()
        middle_layout.addWidget(self.translator_wnd.entry)
        middle_layout.addWidget(self.translator_wnd.translate_btn)
        middle_layout.setAlignment(Qt.AlignCenter)
        middle_layout.setSpacing(7)

        # Lower line, result Label
        self.translator_wnd.output = QLabel("Type a latin numeral to begin")
        self.translator_wnd.output.setFont(font)
        self.translator_wnd.output.setAlignment(
            Qt.AlignHCenter | Qt.AlignVCenter
        )
        self.translator_wnd.output.setMinimumSize(350, 100)

        # General layout nesting other line layouts
        translator_wnd_layout = QVBoxLayout()
        # Upper Line
        translator_wnd_layout.addLayout(central_upper_layout)
        # Middle Line
        translator_wnd_layout.addLayout(middle_layout)
        # Lower Line
        translator_wnd_layout.addWidget(self.translator_wnd.output)

        translator_wnd_layout.setContentsMargins(25, 25, 25, 25)
        translator_wnd_layout.setSpacing(30)

        self.translator_wnd.setLayout(translator_wnd_layout)
        self.translator_wnd.show()
        # setFocus() *HAS* to be after .show() to overwrite general .show() focus
        # FYI general .show() focus is highest placed Widget
        self.translator_wnd.entry.setFocus()

    def on_translate_clicked(self):
        """
        Translate button in translator window. Takes user input, checks if it's
        not empty, checks current translation direction and calls
        handle_translation_input() to get a message to display, either the
        translation of the input or a relative "input error" message,
        indicating the mistake in the input.
        """
        user_input = self.translator_wnd.entry.text()
        self.translator_wnd.entry.setFocus()

        # In case of being pressed with no string
        if not user_input:
            return

        # Checks what it must translate *FROM*
        if self.translator_wnd.entry_title.text() == "Latin Numeral":
            direction = "Latin to Decimal"
        else:
            direction = "Decimal to Latin"

        message = handle_translation_input(user_input, direction)

        self.translator_wnd.output.setText(message)
        self.translator_wnd.entry.clear()

    def on_reverse_clicked(self, status):
        """
        Reverse button function in translator window.

        Reverses flow of translation and updates tags in window accordingly.
        """
        if status:
            self.translator_wnd.entry_title.setText("Decimal Number")
            self.translator_wnd.output_title.setText("Latin Numeral")
            self.translator_wnd.output.setText(
                "Type a decimal number to begin"
            )
        else:
            self.translator_wnd.entry_title.setText("Latin Numeral")
            self.translator_wnd.output_title.setText("Decimal Number")
            self.translator_wnd.output.setText("Type a latin numeral to begin")
        self.translator_wnd.entry.clear()
        self.translator_wnd.entry.setFocus()

    def on_rules_btn_clicked(self):
        """
        Main menu Rules button function.

        Creates a window containing values of Latin numerals and the rules of
        writing Latin numerals.
        """
        self.rules_wnd = QWidget()

        # Window Properties
        self.rules_wnd.setWindowTitle("Rules")
        self.rules_wnd.setWindowIcon(QIcon(resource_path("L-Icon.png")))
        self.rules_wnd.setMinimumSize(600, 230)

        # Latin title
        self.rules_wnd.numerals_title = QLabel("Latin")
        font = self.rules_wnd.numerals_title.font()
        font.setFamily("Times New Roman")

        # Font properties for both titles
        font.setPointSize(20)
        font.setBold(True)
        self.rules_wnd.numerals_title.setFont(font)
        # Decimal Title
        self.rules_wnd.decimals_title = QLabel("Decimal")
        self.rules_wnd.decimals_title.setFont(font)

        # Latin table contents
        self.rules_wnd.numerals_box = QLabel(
            """I
V
X
L
C
D
M"""
        )
        # Decimal table contents
        self.rules_wnd.decimals_box = QLabel(
            """1
5
10
50
100
500
1000"""
        )
        # Font for both tables' contents
        font.setPointSize(16)
        font.setBold(False)
        self.rules_wnd.numerals_box.setFont(font)
        self.rules_wnd.decimals_box.setFont(font)

        # Note for 5.000/10.000 etc
        self.rules_wnd.note = QLabel(
            """Note: 5.000/10.000 used to be depicted with repeating M, later V̅/X̅ were 
            used instead. This app uses the repeating M version."""
        )
        font.setPointSize(12)
        font.setItalic(True)
        self.rules_wnd.note.setFont(font)
        font.setItalic(False)

        # Top part, latin numerals table
        numerals_layout = QVBoxLayout()
        numerals_layout.addWidget(self.rules_wnd.numerals_title)
        numerals_layout.addWidget(self.rules_wnd.numerals_box)
        numerals_layout.setSpacing(0)

        # Top part, decimals table
        decimals_layout = QVBoxLayout()
        decimals_layout.addWidget(self.rules_wnd.decimals_title)
        decimals_layout.addWidget(self.rules_wnd.decimals_box)
        decimals_layout.setSpacing(0)

        # Table containing both
        table_layout = QHBoxLayout()
        table_layout.addLayout(numerals_layout)
        table_layout.addLayout(decimals_layout)
        table_layout.setSpacing(0)
        table_layout.setContentsMargins(125, 5, 5, 5)

        # Lower part, rules
        self.rules_wnd.rules_title = QLabel("Rules:")
        font.setPointSize(20)
        font.setBold(True)
        self.rules_wnd.rules_title.setFont(font)

        self.rules_wnd.rules_text = QLabel(
            """
1.     Numerals I, X, C and M  can be repeated to add up their 
        value up to 3 times, but never more than 3 times. 
        Numerals V, L and D are never repeated.
        Example: III = 1 + 1 + 1 = 3
                        CXXVIII = 100 + 10 + 10 + 5 + 1 + 1 + 1 = 128
   
2.     If the next numeral is of higher value and current numeral
        is not repeated, current numeral is subtracted from next 
        numeral's value. 
        Numerals V, L and D are never subtracted from another 
        value and should never be before a numeral of higher value.
        Example: XL = 50 - 10 = 40
                         XIV = 10 + 5 - 1 = 14
                         VL is not 45 and is incorrect,
        Instead: XLV = XL + V = (50 - 10) + 5 = 45
   
3.     Rule #2 does not apply for numerals with less than
        1/10 of next numeral's value.
        Example: IC is not 99, because 'I' is 1/100 of Cs value.
        Instead: 99 = XCIX = 90 + 9 = (100 - 10) + (10 - 1) 
"""
        )

        font.setPointSize(16)
        font.setBold(False)
        self.rules_wnd.rules_text.setFont(font)

        rules_layout = QVBoxLayout()
        rules_layout.addWidget(self.rules_wnd.rules_title)
        rules_layout.addWidget(self.rules_wnd.rules_text)

        # Inner general layout to be scrollable
        inner_rules_wnd_layout = QVBoxLayout()
        inner_rules_wnd_layout.addLayout(table_layout)
        inner_rules_wnd_layout.addWidget(self.rules_wnd.note)
        inner_rules_wnd_layout.addLayout(rules_layout)
        inner_rules_wnd_layout.setSpacing(0)

        # Widget to contain window layout
        scroll_widget = QWidget()
        scroll_widget.setLayout(inner_rules_wnd_layout)

        # Creating a scroll area
        scroll_area = QScrollArea(self.rules_wnd)
        scroll_area.setWidgetResizable(True)
        # Disabling innate border
        scroll_area.setStyleSheet("QScrollArea {border: none;}")
        # Adding widget
        scroll_area.setWidget(scroll_widget)
        # A layout for the window with scroll_area as its widget
        outter_rules_wnd_layout = QVBoxLayout()
        outter_rules_wnd_layout.addWidget(scroll_area)

        # Setting layout window
        self.rules_wnd.setLayout(outter_rules_wnd_layout)

        self.rules_wnd.show()
        # Needs to update after scroll_area addition
        self.rules_wnd.numerals_title.updateGeometry()

    def on_quiz_btn_clicked(self):
        """
        Main menu Quiz button function.

        Creates Quiz window with a random number in either Latin or Decimal,
        an antry field and a check button, and a result field.
        Displays correct answers streak after 5 consecutive correct answers.
        """

        self.quiz_wnd = QWidget()
        # Window Properties
        self.quiz_wnd.setWindowTitle("Quiz")
        self.quiz_wnd.setWindowIcon(QIcon(resource_path("L-Icon.png")))
        self.quiz_wnd.setMinimumSize(375, 400)
        self.quiz_wnd.setMaximumSize(675, 500)

        # Title
        self.quiz_wnd.quiz_title = QLabel("Quiz\n")
        font = self.quiz_wnd.quiz_title.font()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        self.quiz_wnd.quiz_title.setFont(font)
        self.quiz_wnd.quiz_title.setAlignment(Qt.AlignHCenter)

        # Instruction
        self.quiz_wnd.question = QLabel("Translate the following:\n")
        font.setPointSize(16)
        font.setBold(False)
        self.quiz_wnd.question.setFont(font)

        # Placeholder for randomized number
        self.quiz_wnd.question_number = QLabel("")
        font.setBold(True)
        font.setPointSize(18)
        self.quiz_wnd.question_number.setFont(font)
        self.quiz_wnd.question_number.setAlignment(Qt.AlignCenter)
        # Calls randomize() to get random number
        self.quiz_wnd.question_number.setText(randomize())

        # Answer's title label
        self.quiz_wnd.answer_title = QLabel("\nYour answer:")
        font.setBold(False)
        font.setPointSize(16)
        self.quiz_wnd.answer_title.setFont(font)

        # Entry field of answer
        self.quiz_wnd.answer = QLineEdit()
        self.quiz_wnd.answer.setAlignment(Qt.AlignCenter)
        self.quiz_wnd.answer.setFont(font)
        # Register answer BTN
        self.quiz_wnd.register_answer = QPushButton("Check")
        self.quiz_wnd.register_answer.setFont(font)
        self.quiz_wnd.register_answer.clicked.connect(
            self.on_quiz_answer_btn_clicked
        )
        self.quiz_wnd.register_answer.setShortcut("Return")

        # Box with entry + BTN
        answer_layout = QHBoxLayout()
        answer_layout.addWidget(self.quiz_wnd.answer)
        answer_layout.addWidget(self.quiz_wnd.register_answer)

        # Result Title
        self.quiz_wnd.result_title = QLabel("\nResult:")
        self.quiz_wnd.result_title.setFont(font)

        # Result text
        self.quiz_wnd.result = QLabel("No answer yet")
        self.quiz_wnd.result.setFont(font)

        # A little something to make result area stand out
        self.quiz_wnd.result.setStyleSheet(
            """border-color: rgb(170,170,170);
            border-width: 5px; 
            border-style: groove;"""
        )
        self.quiz_wnd.result.setMinimumSize(350, 75)

        # General layout for quiz window
        quiz_wnd_layout = QVBoxLayout()
        quiz_wnd_layout.addWidget(self.quiz_wnd.quiz_title)
        quiz_wnd_layout.addWidget(self.quiz_wnd.question)
        quiz_wnd_layout.addWidget(self.quiz_wnd.question_number)
        quiz_wnd_layout.addWidget(self.quiz_wnd.answer_title)
        quiz_wnd_layout.addLayout(answer_layout)
        quiz_wnd_layout.addWidget(self.quiz_wnd.result_title)
        quiz_wnd_layout.addWidget(self.quiz_wnd.result)
        quiz_wnd_layout.setAlignment(Qt.AlignTop)

        self.quiz_wnd.setLayout(quiz_wnd_layout)
        self.quiz_wnd.show()

    def on_quiz_answer_btn_clicked(self):
        """
        Quiz window "Check" button function. If user input is empty, clears it
        and returns. Calls handle_quiz_input() to display the relative result.
        """

        # Grabs entry text
        user_input = self.quiz_wnd.answer.text()

        # If the input contains nothing other than whitespace
        if not user_input.strip():
            self.quiz_wnd.answer.clear()
            self.quiz_wnd.answer.setFocus()
            return

        # Saves result to be displayed and current quiz streak
        result, self.quiz_streak = handle_quiz_input(
            self.quiz_wnd.question_number.text(), user_input, self.quiz_streak
        )
        self.quiz_wnd.result.setText(result)
        # Reroll a quiz number
        self.quiz_wnd.question_number.setText(randomize())

        self.quiz_wnd.answer.clear()
        self.quiz_wnd.answer.setFocus()

    def on_exit_btn_clicked(self):
        """
        Main window exit button function.

        Closes window and app.
        """
        self.close()
