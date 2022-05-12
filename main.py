from controller import *


def main() -> None:
    """
    Function to run the Module file as well as the GUI file
    :return: Nothing
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
