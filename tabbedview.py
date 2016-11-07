from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
Builder.load_file('tabbedview.kv')


class Test(TabbedPanel):
    pass

class CustomDropDown(BoxLayout):
    pass

class TabbedPanelApp(App):
    def build(self):
        a = Test()

        return a

if __name__ == '__main__':
    TabbedPanelApp().run()
