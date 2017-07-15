# Program: hello_world.py
#
# Date: 7/14/17
#
# Description: Simple hello world application using Kivy
#
# Note: See docs in Kivy_Dev repo for notes on APK deployment
#
from kivy.app import App
from kivy.uix.button import Button

class Hello_World(App):
    def build(self):
        btn = Button(text="Hello World!")
        return btn

def main():
    Hello_World().run()

if __name__ == "__main__":
    main()