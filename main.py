from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'Body Mass Index Calc'
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: 'BMI_Calc'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
        
        MDTextField:
            id: val2
            input_filter: 'float'
            hint_text: "Enter your weight in KG"
            color_mode: 'custom'
            helper_text_mode: "on_focus"
        MDTextField:
            id: val3
            input_filter: 'float'
            hint_text: "Enter your height in meters"
            color_mode: 'custom'
            helper_text_mode: "on_focus"
        MDTextField:
            id: val4
            hint_text: "Your BMI"
            readonly : "True"
            color_mode: 'custom'
            icon_right_color: app.theme_cls.primary_color
            icon_right: 'equal-box'
        
        MDRoundFlatIconButton:
            id:add
            text: "Calculate"
            pos_hint: {"center_x": .5, "center_y": .6}
            on_press: app.calc()
        MDSpinner:
            id: rc_spin
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .5}
            active: False
        MDLabel:
            id: result
        MDBottomNavigation:
    
            MDBottomNavigationItem:
                name: 'Body Mass Index Calc'
                text: 'BMI CALC'
                icon: 'calculator'
                
    '''

class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name='BMI_Calc'))


class MainApp(MDApp):
    
    dialog = None

    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        self.title = 'Body Mass Index Calc'
        return self.help_string

    def calc(self):
        
        try:
            val1 = float(self.help_string.get_screen('Body Mass Index Calc').ids.val2.text)
        except ValueError:
            val1 = 0
            if not self.dialog:
                self.dialog = MDDialog(title = "Error", text = "Weight or Height can't be blank", buttons =[MDRectangleFlatButton(text="OK", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog),])
            self.dialog.open()
        try:
            val2 = float(self.help_string.get_screen('Body Mass Index Calc').ids.val3.text) 
        except ValueError:
            val2 = 0
            if not self.dialog:
                self.dialog = MDDialog(title = "Error", text = "Weight or Height can't be blank", buttons =[MDRectangleFlatButton(text="OK", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog),])
            self.dialog.open()
        
        if 0 in (val1, val2):
            if not self.dialog:
                self.dialog = MDDialog(title = "Error", text = "Weight or Height can't be blank or 0", buttons =[MDRectangleFlatButton(text="OK", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog),])
            self.dialog.open()
        else:
            res = val1/val2**2
            res_typ = ""
            if res == 0:
                if not self.dialog:
                    self.dialog = MDDialog(title = "Error", text = "Weight or Height can't be 0", buttons =[MDRectangleFlatButton(text="OK", text_color=self.theme_cls.primary_color, on_release = self.neat_dialog),])
                self.dialog.open()
            elif res < 18.5:
                res_typ = "Underweight"
            elif res > 18.5 and res < 24.9:
                res_typ = "Healthy"
            elif res > 25.0 and res < 30.0:
                res_typ = "Obese"
            elif res > 30.0:
                res_typ = "not a human."

            format_res = "{:.2f}".format(res)

            self.help_string.get_screen('Body Mass Index Calc').ids.val4.text = "Your BMI is "+str(format_res)+f". You are {res_typ}"

    def close_dialog(self, obj):
        self.dialog.dismiss()
	
    def neat_dialog(self, obj):
	self.dialog.dismiss()

MainApp().run()
