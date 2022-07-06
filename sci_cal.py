


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import math
from math import pi,log,sqrt,sinh,cosh,tanh,exp,log10,e

Window.size=(380,730)

Builder.load_file('sci_cal.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text='0'

    def button_press(self,x):
        #create a variable

        prior=self.ids.calc_input.text
        if 'Error' in prior:
            prior=''

        if prior=='0':
            self.ids.calc_input.text=''
            self.ids.calc_input.text=f'{x}'
        else:
            self.ids.calc_input.text=f'{prior}{x}'
    
    def math_sign(self,sign):
        prior=self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}{sign}'
    
    def point(self):
        prior=self.ids.calc_input.text
        prior=prior.split('+')
        if '.' in prior[-1]:
            pass
        else:
            self.ids.calc_input.text=f'{self.ids.calc_input.text}.'
    
    def sign_change(self):
        prior=self.ids.calc_input.text
        if float(prior) >0:
            self.ids.calc_input.text=f'-{prior}'
        if float(prior) < 0:
            self.ids.calc_input.text=prior[1:]

    def back(self):
        prior=self.ids.calc_input.text
        if prior!='0':
            self.ids.calc_input.text=prior[:-1]
    
    def convert(self):
        prior=self.ids.rad.text

        if prior == 'rad':
            self.ids.rad.text='deg'
        if prior == 'deg':
            self.ids.rad.text='rad'        

    
    ans=float(0)

    def equal(self):
        prior=self.ids.calc_input.text
        
        global ans

        def cbrt(a):
            return a**(1/3)

        def fact(a):
            return math.factorial(a)


        def sin(a):
            if self.ids.rad.text=='rad':
                return math.sin(a)
            
            else:
                return math.sin(math.radians(a))

        def cos(a):
            if self.ids.rad.text=='rad':
                return math.cos(a)
            else:
                return math.cos(math.radians(a))

        def tan(a):
            if self.ids.rad.text=='rad':
                return math.tan(a)
            else:
                return math.tan(math.radians(a))
        
        #addition symbol
        #eval is function that evaluate the string
        try:
            answer=eval(prior)
            ans=answer
            self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text='Error'



    def give_back(self):
        global ans
        if self.ids.calc_input.text=='0' :
            self.ids.calc_input.text=f'ans'
        else:
            self.ids.calc_input.text+=f'ans'





class Calculator(App):
    def build(self):
        Window.clearcolor =(1,1,1,1)
        return MyLayout()

    
if __name__=='__main__':
    Calculator().run()