"""Calculation history Class"""
from calc.calculations.add import Addition
from calc.calculations.divide import Division
from calc.calculations.subtract import Subtraction
from calc.calculations.multiply import Multiplication
import csv
import os
import pandas as pd
class Calculations: # pylint: disable=too-few-public-methods
    """Calculation history Class"""

    history = []
    @staticmethod
    def clear_history():
        """ clear the history list"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """ get the length of history list"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """get the last calculation object from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """ get the first calculation from the history"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(number):
        """ get a specific calculation from history"""
        return Calculations.history[number]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        Calculations.write_csv(calculation);
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True

    @staticmethod
    def write_csv(calc):
        """Add a division object to history using factory method create"""
        isfileExist = os.path.exists('calculation_list.csv')

        with open('calculation_list.csv', mode='a') as csv_file:
            fieldnames = ['id', 'operation','value0', 'value1','result']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if not isfileExist:
                writer.writeheader();
            writer.writerow({'id': Calculations.calc_id(),   'operation':calc.operation, 'value0':calc.values[0],'value1': calc.values[1],'result':calc.get_result()})
        return True

    @staticmethod
    def read_csv():
        isfileExist = os.path.exists('calculation_list.csv')
        if not isfileExist:
            # return null
            return None
        dataCalculations = pd.read_csv('calculation_list.csv')
        return dataCalculations.iterrows()

    @staticmethod
    def calc_id():
        dataCalculations = pd.read_csv('calculation_list.csv')
        id = len(dataCalculations.index)
        return id+1;
