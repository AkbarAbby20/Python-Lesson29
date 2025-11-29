import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi simple")
        
        # widget
        self.label = QLabel("Halo algonova, ini aplikasi PyQt ke-empat kita!":, self)
        self.button = QPushButton("Klik Saya!", self)
        self.button.clicked.connect(self.show_message)

        #Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        #fungsi
        def show_message(self):
            QMessageBox.information(self, "Pesan", "Tombol telah diklik!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
