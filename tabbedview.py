from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
Builder.load_string("""

<CustomDropDown>:
    thevalue: 'ratatata'

<Test>:
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'first tab'
        BoxLayout:
            Label:
                text: 'Enter Node Name Here'
            TextInput:
                id: node_name

            Button:
                id: btn
                text: 'Press'
                on_release: dropdown.open(self)
                size_hint_y: None
                height: '48dp'

            DropDown:
                id: dropdown
                on_select: btn.text = '{}'.format(args[1])
                on_parent: self.dismiss()
                Button:
                    text: 'First Item'
                    size_hint_y: None
                    height: '48dp'
                    on_release: dropdown.select('First Item')
                Label:
                    text: 'Second Item'
                    size_hint_y: None
                    height: '48dp'
                Button:
                    text: 'Third Item'
                    size_hint_y: None
                    height: '48dp'
                    on_release: dropdown.select('Third Item')


    TabbedPanelItem:
        text: 'tab2'
        BoxLayout:
            Label:
                text: btn.text
            Button:
                text: 'Something Button'
            TextInput:
                id: tab2ti
    TabbedPanelItem:
        text: 'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))

""")


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
