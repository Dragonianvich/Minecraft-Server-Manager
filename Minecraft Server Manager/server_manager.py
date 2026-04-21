import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QSlider, QToolTip
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QCursor


class ServerThread(QThread):
    log_signal = Signal(str)

    def __init__(self, ram_gb):
        super().__init__()
        self.process = None
        self.ram_gb = ram_gb

    def run(self):
        self.process = subprocess.Popen(
            ["java",
            f"-Xmx{self.ram_gb}G",
            f"-Xms{max(1, self.ram_gb // 2)}G",
            "-jar",
            "Minecraft Server Manager/server.jar",
            "nogui"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            text=True
        )
        for line in self.process.stdout:
            self.log_signal.emit(line)

    def stop(self):
        if self.process:
            self.process.stdin.write("stop\n")
            self.process.stdin.flush()

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minecraft Server Manager - v1.0")

        self.layout= QVBoxLayout()

        self.start_btn = QPushButton("Start server")
        self.stop_btn = QPushButton("Stop server")
        self.slider = QSlider(Qt.Horizontal)
        self.log_box = QTextEdit()
        
        self.layout.addWidget(self.start_btn)
        self.layout.addWidget(self.stop_btn)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.log_box)
        self.setLayout(self.layout)


        self.start_btn.clicked.connect(self.start_server)
        self.stop_btn.clicked.connect(self.stop_server)
        self.slider.setMinimum(2)
        self.slider.setMaximum(32)
        self.slider.setValue(8)
        self.slider.valueChanged.connect(self.on_slider_change)
        self.ram_value = self.slider.value()

    def start_server(self):
        if not hasattr(self, "server_thread") or not self.server_thread.isRunning():
            self.server_thread = ServerThread(self.ram_value)  # pass slider value
            self.server_thread.log_signal.connect(self.update_log)
            self.server_thread.start()

    def stop_server(self):
        if hasattr(self, "server_thread") and self.server_thread.process:
            self.server_thread.stop()

    def update_log(self, text):
        self.log_box.append(text.strip())

    def on_slider_change(self, value):
        self.ram_value = value
        #pos = self.slider.mapToGlobal(self.slider.rect().center())
       #QToolTip.showText(pos, f"{value} GB")
        QToolTip.showText(QCursor.pos(), f"{value} GB")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())