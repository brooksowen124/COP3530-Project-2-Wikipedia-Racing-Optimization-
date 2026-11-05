from GUI import Window
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = Window()
  window.show()

  window.load_pickles()

  sys.exit(app.exec())