class AppleKeyboard:
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def set_keyboard_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_keyboard_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_keyboard_input()

