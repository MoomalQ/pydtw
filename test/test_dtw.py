# -*- coding: utf-8 -*-
from unittest import TestCase
# from nose.tools import eq_
import numpy as np

from pydtw import dtw1d, dtw2d


class DtwTest(TestCase):
    def test_dtw1d(self):
        a = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0], dtype=np.float64)
        b = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0], dtype=np.float64)
        cost, al_a, al_b = dtw1d(a, b)
        assert (al_a == np.array([0, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9])).all(), al_a
        assert (al_b == np.array([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9])).all(), al_b

    def test_dtw2d(self):
        a = np.array([[0.30590702, 0.71122566, 0.87785326, 0.41896773, 0.27411357],
                      [0.78599928, 0.13459698, 0.7441022, 0.79060971, 0.9681483],
                      [0.67467294, 0.65713991, 0.06253549, 0.2692394, 0.34000727],
                      [0.79171092, 0.05383535, 0.85633251, 0.79434776, 0.07521822],
                      [0.04116069, 0.93189229, 0.56063383, 0.15773727, 0.41580332],
                      [0.88198997, 0.70688883, 0.04622127, 0.6324347, 0.94977589],
                      [0.45343914, 0.58697004, 0.56443057, 0.53493055, 0.03360396],
                      [0.53693851, 0.34162195, 0.26667218, 0.44254594, 0.08195404],
                      [0.63299858, 0.54636604, 0.15679107, 0.53235207, 0.10908979],
                      [0.94692708, 0.03055877, 0.52066543, 0.15592486, 0.90842773],
                      [0.63713889, 0.13715326, 0.12382141, 0.18114644, 0.64222287],
                      [0.18344581, 0.36095063, 0.04299809, 0.93636622, 0.97176932],
                      [0.46324373, 0.03592446, 0.2815672, 0.024673, 0.03278622],
                      [0.40219816, 0.37011199, 0.89306112, 0.69104287, 0.65363817],
                      [0.12373541, 0.66056791, 0.72306298, 0.51247937, 0.89520386],
                      [0.62731672, 0.06151905, 0.20113791, 0.54437935, 0.24038752],
                      [0.6650012, 0.93281123, 0.45220594, 0.5920064, 0.84662455],
                      [0.35575232, 0.53527631, 0.26486243, 0.05665991, 0.37931886],
                      [0.7680193, 0.38466873, 0.42141126, 0.43820938, 0.18742516],
                      [0.02902629, 0.61636535, 0.14813542, 0.80206397, 0.96151947]])
        b = np.array([[0.37700537, 0.06839722, 0.90342088, 0.67260341, 0.21236238],
                      [0.81431271, 0.30039987, 0.7422115, 0.81856106, 0.73533936],
                      [0.0785568, 0.20518932, 0.37183274, 0.66525787, 0.91777226],
                      [0.26032762, 0.43689793, 0.50414443, 0.62953974, 0.26879355],
                      [0.0772129, 0.6953331, 0.94603823, 0.04144669, 0.64313459],
                      [0.33403999, 0.58964715, 0.85784944, 0.1092154, 0.90425047],
                      [0.57409039, 0.99600997, 0.5179884, 0.39531699, 0.14252428],
                      [0.79165219, 0.57988299, 0.62778483, 0.69332613, 0.63002323],
                      [0.0249018, 0.73852518, 0.98462038, 0.24437005, 0.89890168],
                      [0.37329552, 0.7420235, 0.51391262, 0.18437844, 0.34257216],
                      [0.7842619, 0.21165934, 0.95643329, 0.399339, 0.93537423],
                      [0.13890876, 0.32683409, 0.90477286, 0.82666108, 0.01006905],
                      [0.90557923, 0.28472431, 0.09018984, 0.86671066, 0.90903727],
                      [0.54199152, 0.83542679, 0.65840321, 0.95418474, 0.87883887],
                      [0.18411973, 0.78678018, 0.39588103, 0.92501485, 0.87820573],
                      [0.83208939, 0.70154756, 0.96767817, 0.16727018, 0.49564328],
                      [0.47970899, 0.59563789, 0.25823924, 0.43123425, 0.16967742],
                      [0.83565957, 0.35983831, 0.73003322, 0.38112664, 0.61784956],
                      [0.89832668, 0.45160468, 0.56442061, 0.47974733, 0.39944765],
                      [0.68100611, 0.26754648, 0.79144153, 0.14882468, 0.29260584],
                      [0.49658543, 0.88300153, 0.4789712, 0.75601603, 0.64980613],
                      [0.98528348, 0.4945167, 0.60385308, 0.64908159, 0.40022932],
                      [0.7663773, 0.73506873, 0.94322472, 0.72975117, 0.23751136],
                      [0.00794367, 0.72420966, 0.07036621, 0.5213072, 0.60074303],
                      [0.78067221, 0.48692555, 0.38134388, 0.16889658, 0.47186969]])

        cost, al_a, al_b = dtw2d(a, b)
        assert (al_a == np.array([0, 0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11,
                                  11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 19])).all(), al_a
        assert (al_b == np.array([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])).all(), al_b
