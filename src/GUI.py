from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import QCoreApplication
from adj_list import AdjacencyMap
import time

class Window(QWidget):

    def __init__(self):
        super().__init__()

        # GUI elements

        self.setWindowTitle("Wikipedia Race Solver")
        self.resize(700, 400)

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

        # holds the algorithm changer and solve button
        middle_layout = QVBoxLayout()
        total_layout.addLayout(middle_layout)


        algo_layout = QHBoxLayout()
        middle_layout.addLayout(algo_layout)

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


        self.button_enabled_style = """
            QPushButton {
                font-size: 14px;
                background-color: #ffffff;
            }
        """
        self.button_disabled_style = """
            QPushButton {
                font-size: 14px;
                background-color: #bbbbbb;
            }
        """
        self.solve_button = QPushButton("Solve", self)

        self.solve_button.clicked.connect(self.solve_button_pressed)
        self.solve_button.setStyleSheet(self.button_enabled_style)

        middle_layout.addWidget(self.solve_button)


        # change algorithm features



        self.algorithm_changer_label = QLabel("Algorithm:", self)
        self.algorithm_changer  = QPushButton("BFS")

        self.algorithm_changer.clicked.connect(self.change_algorithm)


        algo_layout.addWidget(self.algorithm_changer_label)
        algo_layout.addWidget(self.algorithm_changer)



        # output features

        self.output_style = """
            border: 3px solid black;
            font-size: 14px;
            padding: 5px;
            background-color: #ffffff;
        """
        self.error_output_style = """
            color: red;
            border: 3px solid black;
            font-size: 14px;
            padding: 5px;
            background-color: #ffffff;
        """

        self.output_header_label = QLabel("Output:", self)
        self.output_label  = QLabel("", self)

        self.output_label.setStyleSheet(self.output_style)

        bottom_layout.addWidget(self.output_header_label)
        bottom_layout.addWidget(self.output_label)


        # sets the final layout
        self.setLayout(total_layout)


        self.use_regular_BFS = True



        
    # loads the files into memory while still being able to see the screen
    def load_pickles(self):
        self.output_label.setText("Loading Files...")
        self.enable_solve_button(False)

        # update screen now
        QCoreApplication.processEvents()

        self.adjacency_map = AdjacencyMap()

        self.output_label.setText("Files Loaded")
        self.enable_solve_button(True)



    def enable_solve_button(self, enabled):
        self.solve_button.setEnabled(enabled)

        # gray out the solve button if disabled
        if enabled:
            self.solve_button.setStyleSheet(self.button_enabled_style)
        else:
            self.solve_button.setStyleSheet(self.button_disabled_style)

        

    # functionality of the solve button
    def solve_button_pressed(self):

        # clear the text box
        self.output_label.setText("")

        # disable further presses
        self.enable_solve_button(False)


        # preemptively sets the text color in the box to error mode
        self.output_label.setStyleSheet(self.error_output_style)

        # get text field input
        start_name = self.start_input.text()
        target_name = self.target_input.text()

        # checks if both inputs are valid Wikipedia articles
        valid = True
        if not self.adjacency_map.check_input(start_name):
           
           self.output_label.setText(f"\"{start_name}\" is an invalid Wikipedia page...")
           valid = False
        
        if not self.adjacency_map.check_input(target_name):

           self.output_label.setText(f"{self.output_label.text()}\n\"{target_name}\" is an invalid Wikipedia page...")
           valid = False

        

        if valid: 


            # resets text color
            self.output_label.setStyleSheet(self.output_style)

            self.output_label.setText("Solving...")

            # update screen now
            QCoreApplication.processEvents()


            # converts text inputs to their ID
            start_id = self.adjacency_map.name_to_id(start_name)
            target_id = self.adjacency_map.name_to_id(target_name)

            # TODO: make it be able to switch between algorithms

            # start timer
            start_time = time.perf_counter()

            # do BFS
            path = []
            dist = 0

            if self.use_regular_BFS:
                path, dist = self.adjacency_map.BFS(start_id, target_id)
            else:
                path, dist = self.adjacency_map.bidirectional_BFS(start_id, target_id)

            # get time since timer started
            search_time = time.perf_counter() - start_time

            path_string = ""
            for element in path:
                path_string += self.adjacency_map.id_to_name(element) + " -> "

            path_string = path_string[:-4]

            path_string = f"Path: {path_string}\nSearch Time: {str(search_time)[:-10]} seconds\nPath Length: {dist}"

            self.output_label.setText(path_string)


        self.enable_solve_button(True)


    def change_algorithm(self):
        self.use_regular_BFS = not self.use_regular_BFS

        if self.use_regular_BFS:
            self.algorithm_changer.setText("BFS")
        else:
            self.algorithm_changer.setText("Bidirectional BFS")


            



