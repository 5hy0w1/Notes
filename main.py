import sys
import os.path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from window import Ui_MainWindow


standart_note_path = os.path.abspath("/home/5hy0w1/notes/Notes")


class Note(QtWidgets.QListWidgetItem):
    def __init__(self, text="", name="Новая заметка", path=False):
        super().__init__(name)
        self.name = name
        self.text = text
        if not path:
            path = os.path.join(standart_note_path, name)
        if not os.path.exists(standart_note_path):
            os.mkdir(standart_note_path)
        '''if os.path.exists(path):
            i = 1
            while os.path.exists(path):
                path = os.path.join(standart_note_path, self.name + str(i))
                i += 1'''
        self.name = self.name  # #+ str(i)
        self.path = path


class Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.note = False
        self.notes = []
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.save_note)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+N"), self, self.new_note)
        self.notes_list.itemClicked.connect(self.set_current_note)
        self.new_button.clicked.connect(self.new_note)
        self.del_button.clicked.connect(self.del_note)
        self.italicButton.clicked.connect(lambda: self.setTextStyle("Italic"))
        self.boldButton.clicked.connect(lambda: self.setTextStyle("Bold"))
        self.underButton.clicked.connect(lambda: self.setTextStyle("Under"))
        self.fontsizeSpinBox.valueChanged.connect(lambda x: self.setTextStyle({"size":x}))
        self.fontSelector.currentFontChanged.connect(lambda x: self.setTextStyle({"family":x}))
        self.markedList.clicked.connect(lambda: self.addList(-1))
        self.numList.clicked.connect(lambda: self.addList(-4))
        self.get_notes()

    def del_note(self, b):
        path = os.path.join(standart_note_path, self.note.name)
        os.remove(path)
        for item in self.notes_list.selectedItems():
            self.notes_list.takeItem(self.notes_list.row(item))

    def set_current_note(self, item):
        p = os.path.join(standart_note_path, item.text())
        self.load_note(p)
        self.show_note(self.note)

    def get_notes(self):
        for note_name in os.listdir(standart_note_path):
            self.notes.append(Note(text="",
                                   name=note_name,
                                   path=os.path.join(standart_note_path, note_name)))
            self.notes_list.addItem(QtWidgets.QListWidgetItem(note_name))

    def save_note(self):
        with open(self.note.path, 'w') as file:
            text = self.textEdit.toHtml()
            file.write(text)

    def show_note(self, note):
        self.textEdit.setCurrentCharFormat(QtGui.QTextCharFormat())
        self.textEdit.setText(note.text)

    def load_note(self, path):
        name = os.path.basename(path)
        with open(path) as file:
            text = file.read()
        print(type(Note()))
        self.note = Note(text, name, path)
        # #self.show_note(self.note)

    def new_note(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "Введите название заметки", "Название:")
        path = os.path.join(standart_note_path, name)
        if ok:
            open(path, 'w').close()
            '''self.notes.append(Note(text="",
                                   name=name,
                                   path=path))'''
            self.notes_list.addItem(QtWidgets.QListWidgetItem(name))
            self.load_note(path)

    def setTextStyle(self, style):
        cursor = self.textEdit.textCursor()
        char_format = cursor.charFormat()
        if cursor.hasSelection():
            if style == "Italic":
                char_format.setFontItalic(not char_format.fontItalic())
            elif style == "Bold":
                char_format.setFontWeight(300 if char_format.fontWeight() == 700 else 700)
            elif style == "Under":
                char_format.setFontUnderline(not char_format.fontUnderline())
            elif style.get("size"):
                char_format.setFontPointSize(style["size"])
            elif style.get("family"):
                char_format.setFontFamily(style["family"].family())

        cursor.setCharFormat(char_format)
        #else cursor.add:

    def addList(self, style):
        cursor = self.textEdit.textCursor()
        qlist = QtGui.QTextListFormat()
        qlist.setStyle(style)
        cursor.createList(qlist)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
