from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wikapedia Race Solver")
        self.resize(700, 500)

        # splits screen into inputs on top and output on the bottom
        total_layout = QVBoxLayout()

        # splits the inputs into right and left
        top_layout = QHBoxLayout()
        total_layout.addLayout(top_layout)

        # holds everything to do with the start
        start_layout = QVBoxLayout()
        top_layout.addLayout(start_layout)

        # holds everything to do with the target
        target_layout = QVBoxLayout()
        top_layout.addLayout(target_layout)

        # holds the solution
        bottom_layout = QVBoxLayout()
        total_layout.addLayout(bottom_layout)


        # all start features
        self.start_enter_text_label = QLabel("Starting Page:", self)

        self.start_input = QLineEdit(self)

        start_layout.addWidget(self.start_enter_text_label)
        start_layout.addWidget(self.start_input)



        # all target features
        self.target_enter_text_label = QLabel("Target Page:", self)


        self.target_input = QLineEdit(self)


        target_layout.addWidget(self.target_enter_text_label)
        target_layout.addWidget(self.target_input)


        # output features

        self.output_header_label = QLabel("Output:", self)
        self.output_label  = QLabel("", self)


        self.output_style = """
            border: 3px solid black;
            font-size: 14px;
            padding: 5px;
        """
        self.error_output_style = """
            color: red;
            border: 3px solid black;
            font-size: 14px;
            padding: 5px;
        """

        self.output_label.setStyleSheet(self.output_style)

        self.solve_button = QPushButton("Solve", self)
        self.solve_button.clicked.connect(self.solve_button_pressed)

        total_layout.addWidget(self.solve_button)
        total_layout.addWidget(self.output_header_label)
        total_layout.addWidget(self.output_label)


        # sets the final layout
        self.setLayout(total_layout)

    # functionality of the solve button
    def solve_button_pressed(self):

        # checks if both inputs are valid Wikapedia articles
        valid = True
        self.output_label.setStyleSheet(self.error_output_style)
        if not self.check_input("pass"):
           
           self.output_label.setText(f"{self.output_label.text()}\nStart page name is invalid...")
           valid = False
        
        if not self.check_input("pass"):

           self.output_label.setText(f"{self.output_label.text()}\nTarget page name is invalid...")
           valid = False

        if not valid: return

        self.output_label.setStyleSheet(self.output_style)


            

    # TODO: make this check input against list of all names
    def check_input(self, page_name):
       return True
    
        



if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = Window()
  window.show()

  sys.exit(app.exec())