from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout


class ChooseDietWorkOutPlanScreen(Screen):
    checks = []

    def checkbox_click(self, instance, value, Types_of_Diet):

        if value == True:
            ChooseDietWorkOutPlanScreen.checks.append(Types_of_Diet)
            diets = ""
            for x in ChooseDietWorkOutPlanScreen.checks:
                diets = f'{diets}{x}'
            # self.ids.output_label.text= f"you selected:{diets}"
        else:
            ChooseDietWorkOutPlanScreen.checks.remove(Types_of_Diet)
            diets = ""
            for x in ChooseDietWorkOutPlanScreen.checks:
                diets = f'{diets}{x}'
            # self.ids.output_label.text= f"you selected:{diets}"


class DailyCalorieNeeded(Screen):
    pass
class Macro_RATIOS(Screen):
    pass

class WindowManager(ScreenManager):
    pass


a = Builder.load_file("DietAndWorkout.kv")



class MyMainApp(App):
    def build(self):
        return a




if __name__ == "__main__":
    MyMainApp().run()
