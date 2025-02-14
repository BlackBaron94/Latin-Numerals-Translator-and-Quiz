import os 
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QLabel, QLineEdit, 
    QVBoxLayout, QHBoxLayout, QPushButton, QWidget)
from PyQt5.QtCore import Qt
from logic import (quiz_streak, randomize, purify_input, lat2dec, 
    dec2lat)

# This function grabs absolute path to where images are saved
# so that images work for both .py and --onefile .exe executions
def resource_path(relative_path):
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
    
    # Main window initialization
    def __init__(self):
        super().__init__()
        
        # Window Properties
        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon(resource_path('L-Icon.png')))
        self.setFixedSize(350,250)

        # Menu Title
        label = QLabel("WELCOME")
        font = label.font()
        font.setFamily("Old English Text MT")
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        
        # Buttons
        translatorBTN = QPushButton("Numerals Translator")
        translatorBTN.clicked.connect(self.translatorBTN_clicked)
        
        rulesBTN = QPushButton("Numerals Rules")
        rulesBTN.clicked.connect(self.rulesBTN_clicked)
        
        quizBTN = QPushButton("Quiz")
        quizBTN.clicked.connect(self.quizBTN_clicked)
        
        exitBTN = QPushButton("Exit")
        exitBTN.clicked.connect(self.exitBTN_clicked)
        
        # Made_by_label
        made_by_label = QLabel('Made by Black Baron')
        font.setPointSize(12)
        made_by_label.setFont(font)
        
        
        allBTNS = [
            translatorBTN,
            rulesBTN,
            quizBTN,
            exitBTN]
        
        font.setPointSize(16)
        font.setFamily("Times New Roman")
        
        # Main window layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        
        # Modifying and adding buttons
        for btn in allBTNS:
            btn.setFixedSize(200,35)
            btn.setFont(font)
            layout.addWidget(btn, alignment=Qt.AlignCenter)
        layout.addWidget(made_by_label, alignment = Qt.AlignRight | Qt.AlignBottom)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
    # Main menu translatorBTN function    
    def translatorBTN_clicked(self):
        # Translator window
        self.translator_wnd = QWidget()
        self.translator_wnd.setWindowTitle("Translator")
        self.translator_wnd.setWindowIcon(QIcon(resource_path('L-Icon.png')))
        self.translator_wnd.setFixedSize(450,235)
        
        # Translate FROM side
        self.translator_wnd.entry_title = QLabel("Latin Numeral")
        font = self.translator_wnd.entry_title.font()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.translator_wnd.entry_title.setFont(font)
        self.translator_wnd.entry_title.setFixedSize(150,30)
        self.translator_wnd.entry_title.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        # Reverse translation BTN
        self.translator_wnd.reverseBTN = QPushButton()
        self.translator_wnd.reverseBTN.setCheckable(True)
        self.translator_wnd.reverseBTN.setIcon(QIcon(resource_path('arrows.png')))
        self.translator_wnd.reverseBTN.clicked.connect(self.reverse_clicked)
        self.translator_wnd.reverseBTN.setFixedSize(30,30)
        
        # Translate TO side
        self.translator_wnd.output_title = QLabel("Decimal Number")
        self.translator_wnd.output_title.setFont(font)
        self.translator_wnd.output_title.setFixedSize(150,30)
        self.translator_wnd.output_title.setAutoFillBackground(True)
        self.translator_wnd.output_title.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        # Upper line, from + reverse + to
        central_upper_layout = QHBoxLayout()
        central_upper_layout.addWidget(self.translator_wnd.entry_title)
        central_upper_layout.addWidget(self.translator_wnd.reverseBTN)
        central_upper_layout.addWidget(self.translator_wnd.output_title)
        central_upper_layout.setAlignment(Qt.AlignCenter)
        
        
        # Entry field for translation
        self.translator_wnd.entry = QLineEdit()
        self.translator_wnd.entry.setFont(font)
        self.translator_wnd.entry.setAlignment(Qt.AlignHCenter)
        self.translator_wnd.entry.setFixedSize(245,30)
        
        # TranslateBTN
        self.translator_wnd.translateBTN = QPushButton("Translate")
        self.translator_wnd.translateBTN.setFont(font)
        self.translator_wnd.translateBTN.setShortcut("Return")
        self.translator_wnd.translateBTN.clicked.connect(self.translate_clicked)
        self.translator_wnd.translateBTN.setFixedSize(100,30)
        
        # Middle line, field + BTN
        middle_layout = QHBoxLayout()
        middle_layout.addWidget(self.translator_wnd.entry)
        middle_layout.addWidget(self.translator_wnd.translateBTN)
        middle_layout.setAlignment(Qt.AlignCenter)
        middle_layout.setSpacing(7)
        
        # Lower line, result Label
        self.translator_wnd.output = QLabel("Type a latin numeral to begin")
        self.translator_wnd.output.setFont(font)
        self.translator_wnd.output.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        
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
        
        
    # TranslateBTN in translator window
    def translate_clicked(self):
        user_input = self.translator_wnd.entry.text()
        self.translator_wnd.entry.setFocus()
        
        # In case of being pressed with no string
        if not user_input:
            return
        
        # Checks what it must translate *FROM*
        if self.translator_wnd.entry_title.text() == "Latin Numeral":
            
            result = lat2dec(user_input)
            
            # Checks if string is free of mistakes
            if result[0]:
                # Purifies input to display correctly
                purified_input = purify_input(str(user_input))
                self.translator_wnd.output.setText(
                    'Result: '+str(purified_input+' is '+str(result[1]))
                    )
            # String has mistakes
            else:
                # Checks secondary mistake flag (non numeral strings)
                if not result[1]:
                    self.translator_wnd.output.setText('Invalid input')
                # Main case of mistake
                elif len(result) == 2:
                    self.translator_wnd.output.setText("Invalid input,\n'"+result[1]+"' wrongfully used.")
                # Special case of rule #3 mistake
                else:
                    self.translator_wnd.output.setText("Invalid input,\n'"+result[1]+"' wrongfully used before '"+result[2]+"'. \nCheck rule #3.")
            
        else:
            result = dec2lat(user_input)
            if result:
                self.translator_wnd.output.setText('Result: '+str(user_input+' is '+str(result)))
            elif result == False:
                self.translator_wnd.output.setText('Invalid input')
        self.translator_wnd.entry.clear()
    
    # ReverseBTN in translator window
    def reverse_clicked(self, status):
        if status:
            self.translator_wnd.entry_title.setText("Decimal Number")
            self.translator_wnd.output_title.setText("Latin Numeral")
            self.translator_wnd.output.setText("Type a decimal number to begin")
        else:
            self.translator_wnd.entry_title.setText("Latin Numeral")
            self.translator_wnd.output_title.setText("Decimal Number")
            self.translator_wnd.output.setText("Type a latin numeral to begin")
        self.translator_wnd.entry.clear()
        self.translator_wnd.entry.setFocus()
    
    # Main menu RulesBTN function
    def rulesBTN_clicked(self):
        self.rules_wnd = QWidget()
        
        # Window Properties
        self.rules_wnd.setWindowTitle("Rules")
        self.rules_wnd.setWindowIcon(QIcon(resource_path('L-Icon.png')))
        self.rules_wnd.setFixedSize(555,805)
        
        # Latin title
        self.rules_wnd.numerals_title = QLabel('Latin')
        font = self.rules_wnd.numerals_title.font()
        font.setFamily("Times New Roman")
        
        # Font properties for both titles
        font.setPointSize(20)
        font.setBold(True)
        self.rules_wnd.numerals_title.setFont(font)
        
        # Decimal Title
        self.rules_wnd.decimals_title = QLabel('Decimal')
        self.rules_wnd.decimals_title.setFont(font)
        
        # Latin table contents
        self.rules_wnd.numerals_box = QLabel('''I
V
X
L
C
D
M''')
        # Decimal table contents
        self.rules_wnd.decimals_box = QLabel('''1
5
10
50
100
500
1000''')
        # Font for both tables' contents
        font.setPointSize(16)        
        font.setBold(False)
        self.rules_wnd.numerals_box.setFont(font)
        self.rules_wnd.decimals_box.setFont(font)
        
        # Note for 5.000/10.000 etc
        self.rules_wnd.note = QLabel(
            '''Note: 5.000/10.000 used to be depicted with repeating M, later V̅/X̅ were 
            used instead. This app uses the repeating M version.''')
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
        table_layout.setContentsMargins(125,5,5,5)
        
        # Lower part, rules
        self.rules_wnd.rules_title = QLabel('Rules:')
        font.setPointSize(20)
        font.setBold(True)
        self.rules_wnd.rules_title.setFont(font)
        
        self.rules_wnd.rules_text = QLabel(
'''
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
''')
        
        font.setPointSize(16)
        font.setBold(False)
        self.rules_wnd.rules_text.setFont(font)
        
        rules_layout = QVBoxLayout()
        rules_layout.addWidget(self.rules_wnd.rules_title)
        rules_layout.addWidget(self.rules_wnd.rules_text)
        
        # General layout
        rules_wnd_layout = QVBoxLayout()
        rules_wnd_layout.addLayout(table_layout)
        rules_wnd_layout.addWidget(self.rules_wnd.note)
        rules_wnd_layout.addLayout(rules_layout)
        rules_wnd_layout.setSpacing(0)
        
        self.rules_wnd.setLayout(rules_wnd_layout)
        self.rules_wnd.show()
    
    
    # Main menu QuizBTN function
    def quizBTN_clicked(self):
        
        self.quiz_wnd = QWidget()
        # Window Properties
        self.quiz_wnd.setWindowTitle("Quiz")
        self.quiz_wnd.setWindowIcon(QIcon(resource_path('L-Icon.png')))
        self.quiz_wnd.setFixedSize(355,425)
        
        # Title
        self.quiz_wnd.quiz_title = QLabel('Quiz\n')
        font = self.quiz_wnd.quiz_title.font()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        self.quiz_wnd.quiz_title.setFont(font)
        self.quiz_wnd.quiz_title.setAlignment(Qt.AlignHCenter)
        
        # Instruction
        self.quiz_wnd.question = QLabel('Translate the following:\n')
        font.setPointSize(16)
        font.setBold(False)
        self.quiz_wnd.question.setFont(font)
        
        # Placeholder for randomized number
        self.quiz_wnd.question_number = QLabel('')
        font.setBold(True)
        font.setPointSize(18)
        self.quiz_wnd.question_number.setFont(font)
        self.quiz_wnd.question_number.setAlignment(Qt.AlignCenter)
        # Calls randomize()
        self.quiz_wnd.question_number.setText(randomize())
        
        # Answer's title label
        self.quiz_wnd.answer_title = QLabel('\nYour answer:')
        font.setBold(False)
        font.setPointSize(16)
        self.quiz_wnd.answer_title.setFont(font)
        
        # Entry field of answer
        self.quiz_wnd.answer = QLineEdit()
        self.quiz_wnd.answer.setAlignment(Qt.AlignCenter)
        self.quiz_wnd.answer.setFont(font)
        # Register answer BTN
        self.quiz_wnd.register_answer = QPushButton('Check')
        self.quiz_wnd.register_answer.setFont(font)
        self.quiz_wnd.register_answer.clicked.connect(self.quiz_answerBTN)
        self.quiz_wnd.register_answer.setShortcut('Return')
        
        # Box with entry + BTN
        answer_layout = QHBoxLayout()
        answer_layout.addWidget(self.quiz_wnd.answer)
        answer_layout.addWidget(self.quiz_wnd.register_answer)
        
        # Result Title
        self.quiz_wnd.result_title = QLabel('\nResult:')
        self.quiz_wnd.result_title.setFont(font)
        
        # Result text
        self.quiz_wnd.result = QLabel('No answer yet')
        self.quiz_wnd.result.setFont(font)
        
        # A little something to make result area stand out
        self.quiz_wnd.result.setStyleSheet(
            '''border-color: rgb(170,170,170);
            border-width: 5px; 
            border-style: groove;''')

        
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
        
    # Function for pressing quiz answerBTN        
    def quiz_answerBTN(self):
        # Grabs entry text
        user_input = self.quiz_wnd.answer.text()
        
        # If the input contains nothing other than whitespace
        if not user_input.strip():
            self.quiz_wnd.answer.clear()
            self.quiz_wnd.answer.setFocus()
            return
        
        # Retains initial input before purify to show user 
        # their entry when wrong
        initial_input = user_input
        
        # Checks if first string character is latin in question text
        if self.quiz_wnd.question_number.text()[0] in "IVXLCDM":
            correct_answer = lat2dec(self.quiz_wnd.question_number.text())
            # lat2dec returns array, since question text is controlled
            # it's always len = 2, [0] = True, [1] = *translation*
            correct_answer = str(correct_answer[1])
        else:
            # Purifies user's latin input
            user_input = purify_input(user_input)
            correct_answer = dec2lat(self.quiz_wnd.question_number.text())
        
        # If user input is latin, it's been purified so it matches perfectly
        if user_input == correct_answer:
            
            self.quiz_wnd.result.setText(
                'Your answer is correct!\n{0} is {1}'.format(
                    self.quiz_wnd.question_number.text(), 
                    user_input))
            # Adds +1 to correct streak
            global quiz_streak
            quiz_streak += 1
            
        else:
            # Shows input's correct answer as opposed to user's wrong answer
            self.quiz_wnd.result.setText(
                "Your answer is wrong.\n{0} is {1}, not '{2}'".format(
                    self.quiz_wnd.question_number.text(), 
                    correct_answer, 
                    initial_input))
            # Resets correct streak
            quiz_streak = 0
        self.quiz_wnd.question_number.setText(randomize())
        
        # Displays streak # and a message for high correct streaks
        if quiz_streak > 19:
            self.quiz_wnd.result.setText(self.quiz_wnd.result.text()+'\n'+str(quiz_streak)+" correct answers streak!!! \nYou're on FIRE!!!")
        elif quiz_streak > 9:
            self.quiz_wnd.result.setText(self.quiz_wnd.result.text()+'\n'+str(quiz_streak)+" correct answers streak!! \nYou're on a roll!!")
        elif quiz_streak > 4:
            self.quiz_wnd.result.setText(self.quiz_wnd.result.text()+'\n'+str(quiz_streak)+' correct answers streak!')
                
        self.quiz_wnd.answer.clear()
        self.quiz_wnd.answer.setFocus()
    
    
    def exitBTN_clicked(self):
        self.close()