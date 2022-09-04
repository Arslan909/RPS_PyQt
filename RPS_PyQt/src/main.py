from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("rps.ui", self)  
        self.show()
        self.winCount = 0
        self.loseCount = 0
        self.drawCount = 0
        self.totalGames = 0
        
        
        self.play.clicked.connect(self.gotoPage_2)
        self.result.clicked.connect(self.gotoResult)
        self.ROCK.clicked.connect(lambda:self.clicker(self.ROCK))
        self.PAPER.clicked.connect(lambda:self.clicker(self.PAPER))
        self.SCISSORS.clicked.connect(lambda:self.clicker(self.SCISSORS))
   
   
    def gotoPage_2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
    def gotoResult(self):
        self.stackedWidget.setCurrentWidget(self.page_4)
        
    
    def clicker(self, button_text):
        
        self.computerChoice = (random.choice(["ROCK", "PAPER", "SCISSORS"]))
        
        if button_text.text() == self.computerChoice:
            self.stackedWidget.setCurrentWidget(self.page_3)
            self.computerChoice_label.setText(f"Computer choose {self.computerChoice}")
            self.result_label.setText("Game Draw!")
            self.drawCount += 1
            self.Draw_Count.setText(f"Draws = {self.drawCount}")
            
        elif (button_text.text() == "ROCK" and self.computerChoice == "SCISSORS") or (button_text.text() == "PAPER" and self.computerChoice == "ROCK") or (button_text.text() == "SCISSORS" and self.computerChoice == "PAPER"):
            self.stackedWidget.setCurrentWidget(self.page_3)
            self.computerChoice_label.setText(f"Computer choose {self.computerChoice}")
            self.result_label.setText("You Win!")
            self.winCount += 1
            self.Win_Count.setText(f"Wins = {self.winCount}")

        elif (button_text.text() == "ROCK" and self.computerChoice == "PAPER") or (button_text.text() == "PAPER" and self.computerChoice == "SCISSORS") or (button_text.text() == "SCISSORS" and self.computerChoice == "ROCK"):
            self.stackedWidget.setCurrentWidget(self.page_3)
            self.computerChoice_label.setText(f"Computer choose {self.computerChoice}")
            self.result_label.setText("You Lose!")
            self.loseCount += 1
            self.Lose_Count.setText(f"Loses = {self.loseCount}")            
        self.totalGames = self.drawCount + self.winCount + self.loseCount
        self.Total_Games.setText(f"Total Games = {self.totalGames}")
            
            
    
        self.Play_Again.clicked.connect(self.restart)
    def restart(self):
        self.stackedWidget.setCurrentWidget(self.page)
    
    
    
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()