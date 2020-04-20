# -*- coding: UTF-8 -*-
'''
Created on 2020年4月8日

@author: sunka
'''

class IncomeTax:

    def __init__(self, income, income2):
        self.income = float(income)
        self.income2 = float(income2)
        self.first = 0.02
        self.next1 = 0.06
        self.next2 = 0.1
        self.next3 = 0.14
        self.next4 = 0.17
        self.tax_reduction = 0
        self.x = "0"
        self.y = "0"
        self.basic_allow = 132000
        self.contribution = 0
        self.contribution2 = 0
        self.netincome = 0
        self.netincome2 = 0
        self.jointnetincome = 0
        self.standardincome = 0
        self.standardincome2 = 0

    # -------------------------------------------MPF-------------------------------------------------#

    def MPF(self):
        # First income calculation
        if (self.income - 30000) > 0:
            self.contribution = 1500 * 12
        elif (self.income - 7100) >= 0:
            self.contribution = (self.income * 0.05) * 12
        else:
            self.contribution = 0

    def soulMPF(self):
        if (self.income2 - 30000) > 0:
            self.contribution2 = 1500 * 12
        elif (self.income2 - 7100) >= 0:
            self.contribution2 = (self.income2 * 0.05) * 12
        else:
            self.contribution2 = 0

    def printMPF(self):

        x = "Your mandatory contribution is HKD " + str(self.contribution)
        y = "Soul mate mandatory contribution is HKD " + str(self.contribution2)

        return x, y

    # -------------------------------------------MPF-------------------------------------------------#

    # -------------------------------------------NetIncome-------------------------------------------------#

    def calcNetincome(self):
        self.netincome = self.income * 12 - self.contribution - self.basic_allow

    def calcSoulNetincome(self):
        self.netincome2 = self.income2 * 12 - self.contribution2 - self.basic_allow
    '''   
    def calcStandardincome(self):
        self.standardincome = self.income * 12 - self.contribution
        
    def calcSoulStandardincome(self):
        self.standardincome2 = self.income2 * 12 - self.contribution2
    '''

        # -------------------------------------------NetIncome-------------------------------------------------#

    # -------------------------------------------Taxbracket-------------------------------------------------#

    def Taxbracket(self, net_income):
        if (net_income - 50000 * 4) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + 50000 * self.next3 + (
                        net_income - 50000 * 4) * self.next4
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 3) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + (
                        net_income - 50000 * 3) * self.next3
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 2) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + (net_income - 50000 * 2) * self.next2
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 1) >= 0:
            separate_tax = 50000 * self.first + (net_income - 50000 * 1) * self.next1
            separate_tax -= self.tax_reduction

        elif net_income >= 0:
            separate_tax = net_income * self.first
            separate_tax -= self.tax_reduction
            if separate_tax <= 0:
                separate_tax = 0

        elif net_income <= 0:
            separate_tax = 0

        if separate_tax <= 0:
            separate_tax = 0

        standard_tax = (self.income * 12-self.contribution) * 0.15

        if standard_tax < separate_tax:
            separate_tax = standard_tax
        else:
            separate_tax = separate_tax

        return separate_tax

    def Taxbracket2(self, net_income):
        if (net_income - 50000 * 4) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + 50000 * self.next3 + (
                        net_income - 50000 * 4) * self.next4
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 3) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + (
                        net_income - 50000 * 3) * self.next3
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 2) >= 0:
            separate_tax = 50000 * self.first + 50000 * self.next1 + (net_income - 50000 * 2) * self.next2
            separate_tax -= self.tax_reduction

        elif (net_income - 50000 * 1) >= 0:
            separate_tax = 50000 * self.first + (net_income - 50000 * 1) * self.next1
            separate_tax -= self.tax_reduction

        elif net_income >= 0:
            separate_tax = net_income * self.first
            separate_tax -= self.tax_reduction
            if separate_tax <= 0:
                separate_tax = 0

        elif net_income <= 0:
            separate_tax = 0

        if separate_tax <= 0:
            separate_tax = 0

        standard_tax = (self.income2 * 12-self.contribution2) * 0.15

        if standard_tax < separate_tax:
            separate_tax = standard_tax
        else:
            separate_tax = separate_tax

        return separate_tax

    def printTaxbracket(self):
        x = 'Your tax payable is HKD ' + str(self.Taxbracket(self.netincome))  # Separate Tax
        y = 'Your soul mate tax payable is HKD ' + str(self.Taxbracket2(self.netincome2))  # Separate Tax
        z = "Total tax payable: HKD " + str(self.Taxbracket(self.netincome) + self.Taxbracket2(self.netincome2))
        return x, y, z

    # -------------------------------------------Taxbracket-------------------------------------------------#

    # -------------------------------------------JointTax-------------------------------------------------#

    def joint(self, net_income):
        if (net_income - 50000 * 4) >= 0:
            tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + 50000 * self.next3 + (
                        net_income - 50000 * 4) * self.next4
            tax -= self.tax_reduction

        elif (net_income - 50000 * 3) >= 0:
            tax = 50000 * self.first + 50000 * self.next1 + 50000 * self.next2 + (net_income - 50000 * 3) * self.next3
            tax -= self.tax_reduction

        elif (net_income - 50000 * 2) >= 0:
            tax = 50000 * self.first + 50000 * self.next1 + (net_income - 50000 * 2) * self.next2
            tax -= self.tax_reduction

        elif (net_income - 50000 * 1) >= 0:
            tax = 50000 * self.first + (net_income - 50000 * 1) * self.next1
            tax -= self.tax_reduction

        elif net_income >= 0:
            tax = net_income * self.first
            tax -= self.tax_reduction
            if tax <= 0:
                tax = 0

        elif net_income <= 0:
            tax = 0

        if tax <= 0:
            tax = 0

        standard_tax = ((self.income+self.income2)*12-self.contribution-self.contribution2) * 0.15

        if standard_tax < tax:
            tax = standard_tax
        else:
            tax = tax

        return tax

    def CalcJointNetIncome(self):
        self.jointnetincome = (self.income * 12 + self.income2 * 12) - (self.contribution + self.contribution2) - (
                    self.basic_allow * 2)

    def printJoint(self):
        x = "Total tax payable: HKD " + str(self.joint(self.jointnetincome))
        return x

    # -------------------------------------------JointTax-------------------------------------------------#

    # -------------------------------------------CommandTax-------------------------------------------------#
    def comment(self):
        jointtax = self.joint(self.jointnetincome)
        separate_tax = self.Taxbracket(self.netincome) + self.Taxbracket2(self.netincome2)

        if jointtax < separate_tax:
            return "Joint assessment is better," + str(jointtax) + "<" + str(separate_tax)
        elif jointtax == separate_tax:
            return "Both assessment is ok (Same tax payment)," + str(jointtax) + "==" + str(separate_tax)
        else:
            return "Joint assessment is not recommended," + str(jointtax) + ">" + str(separate_tax)


def option():
    print("\n" + "Please choose a function:")
    print("1 Find MPF mandatory contribution")
    print("2 Calculate Salaries Tax (Separate assessment)")
    print("3 Calculate Salaries Tax (Joint assessment)")
    print("4 Recommend if Joint assessment should be used")
    print("0 Exit")
    return input("Function:" + "\n")


def main():
    while True:
        try:
            income = float(input("Pleas enter your monthly income: HKD"))
            income2 = float(input("Please input your soul mate monthly income: HKD"))

            if income <= 0 or income2 <= 0:
                raise Exception("Please enter the correct income (must greater than 0)")

            run = IncomeTax(income, income2)

            input_option = option()

            while input_option != '0':
                if input_option == '1':
                    run.MPF()
                    run.soulMPF()
                    for i in run.printMPF():
                        print(i)

                if input_option == '2':
                    run.MPF()
                    run.soulMPF()
                    run.calcNetincome()
                    run.calcSoulNetincome()
                    #run.calcStandardincome()
                    #run.calcSoulStandardincome()
                    for i in run.printTaxbracket():
                        print(i)

                if input_option == '3':
                    run.MPF()
                    run.soulMPF()
                    run.CalcJointNetIncome()
                    print(run.printJoint())

                if input_option == '4':
                    run.MPF()
                    run.soulMPF()
                    run.calcNetincome()
                    run.calcSoulNetincome()
                    run.CalcJointNetIncome()
                    print(run.comment())

                input("Please press enter to continue")
                input_option = option()
            print("The program finished")
            break

        except ValueError:
            print("Please enter number only")


if __name__ == "__main__":
    main()
