from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from gematria import GematriaDecoder
from isopsephy import IsopsephyDecoder


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resources/main_window.ui", self)

        self.gematria_source_edit.editingFinished.connect(self.process_gematry)
        self.isopsephy_source_edit.editingFinished.connect(self.process_isopsephy)

    def process_gematry(self):
        text = self.gematria_source_edit.text()
        self.gematria_result_edit.setText(str(GematriaDecoder.decode_word(text)))

    def process_isopsephy(self):
        text = self.isopsephy_source_edit.text()
        self.isopsephy_result_edit.setText(str(IsopsephyDecoder.decode_word(text)))