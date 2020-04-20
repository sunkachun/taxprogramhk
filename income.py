import unittest
from pair import IncomeTax


def isValid(income, income2):
    try:
        income = float(income)
        income2 = float(income2)

        if income <= 0 or income2 <= 0:
            raise Exception("Please enter the correct income (must greater than 0)")

    except ValueError:
        raise ValueError


class IncomeTest(unittest.TestCase):
    def test_normal_MPF(self):
        test = IncomeTax(7000, 7000)
        test.MPF()
        test.soulMPF()
        self.assertEqual(test.printMPF(), ("Your mandatory contribution is HKD 0",
                                           "Soul mate mandatory contribution is HKD 0"))

    def test_normal_MPF2(self):
        test = IncomeTax(45000, 35000)
        test.MPF()
        test.soulMPF()
        self.assertEqual(test.printMPF(), ("Your mandatory contribution is HKD 18000",
                                           "Soul mate mandatory contribution is HKD 18000"))

    def test_normal_MPF3(self):
        test = IncomeTax(35000, 7000)
        test.MPF()
        test.soulMPF()
        self.assertEqual(test.printMPF(), ("Your mandatory contribution is HKD 18000",
                                           "Soul mate mandatory contribution is HKD 0"))

    def test_normal_MPF4(self):
        test = IncomeTax(25000, 45000)
        test.MPF()
        test.soulMPF()
        self.assertEqual(test.printMPF(), ("Your mandatory contribution is HKD 15000.0",
                                           "Soul mate mandatory contribution is HKD 18000"))

    def test_separate(self):
        run = IncomeTax(45000, 35000)
        run.MPF()
        run.soulMPF()
        run.calcNetincome()
        run.calcSoulNetincome()
        self.assertEqual(run.printTaxbracket(), ("Your tax payable is HKD 48300.0",
                                                 "Your soul mate tax payable is HKD 27900.0",
                                                 "Total tax payable: HKD 76200.0"))

    def test_separate_low_income(self):
        run = IncomeTax(0, 0)
        run.MPF()
        run.soulMPF()
        run.calcNetincome()
        run.calcSoulNetincome()
        self.assertEqual(run.printTaxbracket(), ("Your tax payable is HKD 0",
                                                 "Your soul mate tax payable is HKD 0",
                                                 "Total tax payable: HKD 0"))
        
    def test_separate_low_income2(self):
        run = IncomeTax(100000, 73000)
        run.MPF()
        run.soulMPF()
        run.calcNetincome()
        run.calcSoulNetincome()
        self.assertEqual(run.printTaxbracket(), ("Your tax payable is HKD 160500.0",
                                                 "Your soul mate tax payable is HKD 105420.0",
                                                 "Total tax payable: HKD 265920.0"))

    def test_joint(self):
        run = IncomeTax(45000, 35000)
        run.MPF()
        run.soulMPF()
        run.CalcJointNetIncome()
        self.assertEqual(run.printJoint(), "Total tax payable: HKD 94200.0")

    def test_none_float(self):
        with self.assertRaises(ValueError):
            isValid('abc', 'qwe')

    def test_negative(self):
        with self.assertRaises(Exception):
            isValid(-1, -2)


if __name__ == '__main__':
    unittest.main()

