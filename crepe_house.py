from enum import Enum
import time

CrepeProgress = Enum('CrepeProgress',
                     'in_queue batter_preparating batter_frying adding_filling adding_toppings adding_syrup rolling_up serving')
CrepeBatterState = Enum('CrepeBatterState', 'raw fried')
CrepeSyrup = Enum('CrepeSyrup', 'sour_cream bbq balsamic_glaze tomato chocolate caramel maple')
CrepeTopping = Enum('CrepeTopping', 'chives dill lemon green_onions basil parmesan_cheese whipped_cream powdered_sugar'
                                    ' mint vanilla_ice_cream fresh_berries')
CrepeFilling = Enum('CrepeFilling', 'ham cheese mushrooms salmon creamy_cheese chicken bell_peppers yellow_cheese'
                                    ' grilled_vegetables feta_cheese spinach ricotta_cheese banana chocolate strawberries'
                                    ' whipped_cream honey nuts apple cinnamon nutella hazelnuts')
STEP_DELAY = 3


class Crepe:
    def __init__(self, name):
        self.batter = ""
        self.batter_state = None
        self.filling = []
        self.syrup = []
        self.toppings = []
        self.name = name
        self.crepe_progress = CrepeProgress.in_queue

    def __str__(self):
        return self.name

    def add_batter(self, batter):
        self.crepe_progress = CrepeProgress.batter_preparating
        self.batter = batter
        self.batter_state = CrepeBatterState.raw

    def add_filling(self, filling):
        self.crepe_progress = CrepeProgress.adding_filling
        self.filling = filling

    def add_syrup(self, syrup):
        self.crepe_progress = CrepeProgress.adding_syrup
        self.syrup = syrup

    def add_toppings(self, toppings):
        self.crepe_progress = CrepeProgress.adding_toppings
        self.toppings = toppings

    def fry_batter(self):
        self.crepe_progress = CrepeProgress.batter_frying
        self.batter_state = CrepeBatterState.fried

    def roll_up(self):
        self.crepe_progress = CrepeProgress.rolling_up

    def serve_crepe(self):
        self.crepe_progress = CrepeProgress.serving


class SavoryCrepeBuilder1:
    def __init__(self):
        self.crepe = Crepe('Crepe with ham, cheese, and mushrooms')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.ham, CrepeFilling.cheese, CrepeFilling.mushrooms]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.sour_cream
        syrup_name = CrepeSyrup.sour_cream.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.chives]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder2:
    def __init__(self):
        self.crepe = Crepe('Crepe with salmon and creamy cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.salmon, CrepeFilling.creamy_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        pass

    def add_toppings(self):
        toppings = [CrepeTopping.dill, CrepeTopping.lemon]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder3:
    def __init__(self):
        self.crepe = Crepe('Crepe with chicken, bell peppers, and yellow cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.chicken, CrepeFilling.bell_peppers, CrepeFilling.yellow_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.bbq
        syrup_name = CrepeSyrup.bbq.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.green_onions]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder4:
    def __init__(self):
        self.crepe = Crepe('Crepe with grilled vegetables and feta cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.grilled_vegetables, CrepeFilling.feta_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.balsamic_glaze
        syrup_name = CrepeSyrup.balsamic_glaze.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.basil]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder5:
    def __init__(self):
        self.crepe = Crepe('Crepe with spinach and ricotta cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.spinach, CrepeFilling.ricotta_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.tomato
        syrup_name = CrepeSyrup.tomato.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.parmesan_cheese]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder1:
    def __init__(self):
        self.crepe = Crepe('Crepe with ham, cheese, and mushrooms')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.ham, CrepeFilling.cheese, CrepeFilling.mushrooms]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.sour_cream
        syrup_name = CrepeSyrup.sour_cream.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.chives]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder2:
    def __init__(self):
        self.crepe = Crepe('Crepe with salmon and creamy cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.salmon, CrepeFilling.creamy_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        pass

    def add_toppings(self):
        toppings = [CrepeTopping.dill, CrepeTopping.lemon]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder3:
    def __init__(self):
        self.crepe = Crepe('Crepe with chicken, bell peppers, and yellow cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.chicken, CrepeFilling.bell_peppers, CrepeFilling.yellow_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.bbq
        syrup_name = CrepeSyrup.bbq.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.green_onions]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder4:
    def __init__(self):
        self.crepe = Crepe('Crepe with grilled vegetables and feta cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.grilled_vegetables, CrepeFilling.feta_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.balsamic_glaze
        syrup_name = CrepeSyrup.balsamic_glaze.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.basil]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SavoryCrepeBuilder5:
    def __init__(self):
        self.crepe = Crepe('Crepe with spinach and ricotta cheese')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, salt, pepper"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.spinach, CrepeFilling.ricotta_cheese]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.tomato
        syrup_name = CrepeSyrup.tomato.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.parmesan_cheese]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SweetCrepeBuilder1:
    def __init__(self):
        self.crepe = Crepe('Crepe with banana and chocolate')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, sugar, salt"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.banana, CrepeFilling.chocolate]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.chocolate
        syrup_name = CrepeSyrup.chocolate.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.whipped_cream]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SweetCrepeBuilder2:
    def __init__(self):
        self.crepe = Crepe('Crepe with strawberries and whipped cream')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, sugar, salt"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.strawberries, CrepeFilling.whipped_cream]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        pass

    def add_toppings(self):
        toppings = [CrepeTopping.powdered_sugar, CrepeTopping.mint]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe


class SweetCrepeBuilder3:
    def __init__(self):
        self.crepe = Crepe('Crepe with honey and nuts')

    def prepare_batter(self):
        batter_ingr = "flour, milk, eggs, sugar, salt"
        print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
        self.crepe.add_batter(batter_ingr)
        time.sleep(STEP_DELAY)
        print(f'Done with the batter ingredients: {batter_ingr}')

    def fry_batter(self):
        print(f'Frying batter for your {self.crepe.name}')
        self.crepe.fry_batter()
        time.sleep(STEP_DELAY)
        print(f'Frying done')

    def add_filling(self):
        filling = [CrepeFilling.honey, CrepeFilling.nuts]
        filling_keys = ', '.join(filling_item.name for filling_item in filling)
        print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
        self.crepe.add_filling(filling)
        time.sleep(STEP_DELAY)
        print(f'Done with the filling ({filling_keys})')

    def roll_up(self):
        print(f'Rolling up your {self.crepe.name}')
        self.crepe.roll_up()
        time.sleep(STEP_DELAY)
        print(f'Rolling up done')

    def pour_syrup(self):
        syrup = CrepeSyrup.caramel
        syrup_name = CrepeSyrup.caramel.name
        print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
        self.crepe.add_syrup(syrup)
        time.sleep(STEP_DELAY)
        print(f'Pouring the syrup done')

    def add_toppings(self):
        toppings = [CrepeTopping.vanilla_ice_cream]
        topping_keys = ', '.join(topping_item.name for topping_item in toppings)
        print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
        self.crepe.add_toppings(toppings)
        time.sleep(STEP_DELAY)
        print(f'Done with the toppings ({topping_keys})')

    def serve_crepe(self):
        self.crepe.serve_crepe()
        print(f'Serving...')
        return self.crepe

class SweetCrepeBuilder4:
        def __init__(self):
            self.crepe = Crepe('Crepe with apple and cinnamon')

        def prepare_batter(self):
            batter_ingr = "flour, milk, eggs, sugar, salt"
            print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
            self.crepe.add_batter(batter_ingr)
            time.sleep(STEP_DELAY)
            print(f'Done with the batter ingredients: {batter_ingr}')

        def fry_batter(self):
            print(f'Frying batter for your {self.crepe.name}')
            self.crepe.fry_batter()
            time.sleep(STEP_DELAY)
            print(f'Frying done')

        def add_filling(self):
            filling = [CrepeFilling.apple, CrepeFilling.cinnamon]
            filling_keys = ', '.join(filling_item.name for filling_item in filling)
            print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
            self.crepe.add_filling(filling)
            time.sleep(STEP_DELAY)
            print(f'Done with the filling ({filling_keys})')

        def roll_up(self):
            print(f'Rolling up your {self.crepe.name}')
            self.crepe.roll_up()
            time.sleep(STEP_DELAY)
            print(f'Rolling up done')

        def pour_syrup(self):
            syrup = CrepeSyrup.maple
            syrup_name = CrepeSyrup.maple.name
            print(f'Pouring the syrup ({syrup_name}) over your {self.crepe.name}')
            self.crepe.add_syrup(syrup)
            time.sleep(STEP_DELAY)
            print(f'Pouring the syrup done')

        def add_toppings(self):
            toppings = [CrepeTopping.whipped_cream]
            topping_keys = ', '.join(topping_item.name for topping_item in toppings)
            print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
            self.crepe.add_toppings(toppings)
            time.sleep(STEP_DELAY)
            print(f'Done with the toppings ({topping_keys})')

        def serve_crepe(self):
            self.crepe.serve_crepe()
            print(f'Serving...')
            return self.crepe

class SweetCrepeBuilder5:
            def __init__(self):
                self.crepe = Crepe('Crepe with nutella and hazelnuts')

            def prepare_batter(self):
                batter_ingr = "flour, milk, eggs, sugar, salt"
                print(f'Preparing savory batter using ({batter_ingr}) for your {self.crepe.name}')
                self.crepe.add_batter(batter_ingr)
                time.sleep(STEP_DELAY)
                print(f'Done with the batter ingredients: {batter_ingr}')

            def fry_batter(self):
                print(f'Frying batter for your {self.crepe.name}')
                self.crepe.fry_batter()
                time.sleep(STEP_DELAY)
                print(f'Frying done')

            def add_filling(self):
                filling = [CrepeFilling.nutella, CrepeFilling.hazelnuts]
                filling_keys = ', '.join(filling_item.name for filling_item in filling)
                print(f'Adding filling ({filling_keys}) to your {self.crepe.name}')
                self.crepe.add_filling(filling)
                time.sleep(STEP_DELAY)
                print(f'Done with the filling ({filling_keys})')

            def roll_up(self):
                print(f'Rolling up your {self.crepe.name}')
                self.crepe.roll_up()
                time.sleep(STEP_DELAY)
                print(f'Rolling up done')

            def pour_syrup(self):
                pass

            def add_toppings(self):
                toppings = [CrepeTopping.vanilla_ice_cream, CrepeTopping.fresh_berries]
                topping_keys = ', '.join(topping_item.name for topping_item in toppings)
                print(f'Adding the toppings ({topping_keys}) to your {self.crepe.name}')
                self.crepe.add_toppings(toppings)
                time.sleep(STEP_DELAY)
                print(f'Done with the toppings ({topping_keys})')

            def serve_crepe(self):
                self.crepe.serve_crepe()
                print(f'Serving...')
                return self.crepe


class CrepeHouse:
    def __init__(self):
        self.menu = {}

    def create_menu(self):
        self.menu[1] = "Crepe with ham, cheese, and mushrooms"
        self.menu[2] = "Crepe with salmon and creamy cheese"
        self.menu[3] = "Crepe with chicken, bell peppers, and yellow cheese"
        self.menu[4] = "Crepe with grilled vegetables and feta cheese"
        self.menu[5] = "Crepe with spinach and ricotta cheese"
        self.menu[6] = "Crepe with banana and chocolate"
        self.menu[7] = "Crepe with strawberries and whipped cream"
        self.menu[8] = "Crepe with honey and nuts"
        self.menu[9] = "Crepe with apple and cinnamon"
        self.menu[10] = "Crepe with nutella and hazelnuts"

    def display_menu(self):
        print("╔═════════════════════════════════════════╗")
        print("║             CrepeHouse Menu             ║")
        print("╠═════════════════════════════════════════╣")
        for num, crepe in self.menu.items():
            print(f"  {num}. {crepe} ")
        print("╚═════════════════════════════════════════╝")



class Waiter:
    def __init__(self):
        self.builder = None

    def prepare_crepe(self, builder):
        self.builder = builder
        steps = (builder.prepare_batter,
                 builder.fry_batter,
                 builder.add_filling,
                 builder.roll_up,
                 builder.pour_syrup,
                 builder.add_toppings,
                 builder.serve_crepe
                 )
        [step() for step in steps]

    def wish_you_delicious(self):
        print(f'\n\nHere is your {self.crepe}. Enjoy :)')

    @property
    def crepe(self):
        return self.builder.crepe


def main():
    # Main program
    crepe_house = CrepeHouse()
    crepe_house.create_menu()
    waiter = Waiter()

    while True:
        crepe_house.display_menu()
        option = input("\nEnter the number of the crepe you want to order from menu (or 'q' to quit): ")
        if option == 'q':
            break
        if int(option) > 0 and int(option) <= 10:
            crepe_builder = None
            if int(option) == 1:
                crepe_builder = SavoryCrepeBuilder1()
            elif int(option) == 2:
                crepe_builder = SavoryCrepeBuilder2()
            elif int(option) == 3:
                crepe_builder = SavoryCrepeBuilder3()
            elif int(option) == 4:
                crepe_builder = SavoryCrepeBuilder4()
            elif int(option) == 5:
                crepe_builder = SavoryCrepeBuilder5()
            elif int(option) == 6:
                crepe_builder = SweetCrepeBuilder1()
            elif int(option) == 7:
                crepe_builder = SweetCrepeBuilder2()
            elif int(option) == 8:
                crepe_builder = SweetCrepeBuilder3()
            elif int(option) == 9:
                crepe_builder = SweetCrepeBuilder4()
            elif int(option) == 10:
                crepe_builder = SweetCrepeBuilder5()

            waiter.prepare_crepe(crepe_builder)
            waiter.wish_you_delicious()
            time.sleep(10)


if __name__ == '__main__':
    main()


