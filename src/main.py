from GUI import Window
from PySide6.QtWidgets import QApplication
import sys
import threading

if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = Window()
  window.show()


  file_load_thread = threading.Thread(target=window.load_pickles)
  file_load_thread.start()

  sys.exit(app.exec())