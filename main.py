import sys
import argparse
from gematria import GematriaDecoder
from isopsephy import IsopsephyDecoder

from PyQt5.QtWidgets import QApplication
from gui import MyWidget

def gematria(word) -> int:
    return GematriaDecoder.decode_word(word)


def isopsephy(word) -> int:
    return IsopsephyDecoder.decode_word(word)


parser = argparse.ArgumentParser(description="Calculate gematria or isopsephia")
parser.add_argument("text", metavar="TEXT", type=str, nargs=1,
                    help="a text which gematria or isopsephia will be calculated")
parser.add_argument("-m", dest="method",
                    choices=["gematria", "isopsephy"],
                    help="method for calculating value")
parser.add_argument("--gui", dest="gui", action="store_true")


args = parser.parse_args()
method = args.method

if args.gui:
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

if method == "gematria":
    print(gematria(args.text[0]))
elif method == "isopsephy":
    print(isopsephy(args.text[0]))
