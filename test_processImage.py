from unittest import TestCase
from filterImage import processImage
import sympy as sp
import os.path

# for 'resources/example.jpg'-------------------------------------------------------
convexVerts = [42, 43, 45, 46, 47, 48, 51, 52, 53, 54, 191, 212,
               213, 214, 215, 513, 3129, 3476, 4069, 4992, 5152, 5182, 5633, 5642,
               6143, 6302, 6303, 6625, 6782, 6784, 7103, 7615, 7632, 8410, 9479, 10128,
               10160, 11965, 11967, 12791, 13111, 15439, 15596, 15597, 15599, 15756, 15919, 17053,
               17854, 17855, 18014, 18703, 19023, 19655, 23936]

q1 = sp.Point3D(16225229 / 87608, 39961 / 376, 955489 / 10951)
q2 = sp.Point3D(47231167 / 262824, 165443 / 1128, 2756587 / 32853)
q3 = sp.Point3D(25482215 / 131412, 101203 / 564, 3791551 / 32853)
q4 = sp.Point3D(8734825 / 43804, 26141 / 188, 1300477 / 10951)
q5 = sp.Point3D(13152587 / 87608, 31183 / 376, 832939 / 10951)
q6 = sp.Point3D(38013241 / 262824, 139109 / 1128, 2388937 / 32853)
q7 = sp.Point3D(5218313 / 32853, 22009 / 141, 3423901 / 32853)
q8 = sp.Point3D(1799626 / 10951, 5438 / 47, 1177927 / 10951)

# ------------------------------------------------------------------------------------

# for 'resources/example2.jpg'--------------------------------------------------------
convexVerts2 = [134,   455,   615,  1393,  2375,  3180,  3499,  4783,  4784,  4946,  5264,  6067,
                6168,  6176,  6188,  6328,  6336,  6647,  6807,  6966,  7109,  7266,  7286,  7297,
                7428,  7440,  7441,  7737,  7755,  7769, 7897,  7910, 7914 , 7924  ,7929  ,7976,
                8078,  8249,  8399,  8719,  8720,  9204,  9859, 10915, 10917, 11075, 11239, 11402,
                13490, 13649, 13650, 14047, 14618, 16686, 16846, 18428, 18444, 19283, 19292, 19443,
                20341, 20940, 23686, 23749, 23846, 24185, 24488]

v1 = sp.Point3D(1666397/7542, 187285/838, 237734/1257)
v2 = sp.Point3D(1868483/7542, 198839/838, 267818/1257)
v3 = sp.Point3D(3785797/15084, 415543/1676, 243998/1257)
v4 = sp.Point3D(3381625/15084, 392435/1676, 213914/1257)
v5 = sp.Point3D(548489/2514, 118515/838, 70773/419)
v6 = sp.Point3D(615851/2514, 130069/838, 80801/419)
v7 = sp.Point3D(415993/1676, 278003/1676, 72861/419)
v8 = sp.Point3D(371085/1676, 254895/1676, 62833/419)

# ------------------------------------------------------------------------------------


# for 'resources/example3.jpg'--------------------------------------------------------

convexVerts3 = [34,   596,  1941,  2277,  2292,  2294,  2436,  2454,  2595,  4719,  4869, 5027,
                6030,  7697,  7699,  7773,  7775,  7858,  8175,  9032,  9331,  9464,  9491,  9515,
                10592, 10752, 11553, 11581, 11591, 12115, 12435, 13504, 13507, 13508, 13509, 13664,
                13665, 13666, 13667, 13939, 13983, 13984, 14800, 14801, 14931, 14960, 16727, 17077,
                17237, 17970, 19485, 19486, 19487, 19762, 21010, 21168, 21207, 21367, 23192, 23467,
                23512, 23565, 23567, 24799, 24959, 25235, 25587]

w1 = sp.Point3D(2186804247/8726134, 2042237055/8726134, 1933017869/8726134)
w2 = sp.Point3D(1913574399/8726134, 2092129437/8726134, 1623426041/8726134)
w3 = sp.Point3D(1008368053/4363067, 989641169/4363067, 736795987/4363067)
w4 = sp.Point3D(1144982977/4363067, 964694978/4363067, 891591901/4363067)
w5 = sp.Point3D(1014666092/4363067, 667741663/4363067, 835476345/4363067)
w6 = sp.Point3D(878051168/4363067, 692687854/4363067, 680680431/4363067)
w7 = sp.Point3D(1859264043/8726134, 1272528609/8726134, 1211526795/8726134)
w8 = sp.Point3D(2132493891/8726134, 1222636227/8726134, 1521118623/8726134)
# ------------------------------------------------------------------------------------


# for 'resources/example4.jpg' --------------------------------------------------------
convexVerts4 = [225,   385,   387,  1554,  2089,  2127,  2146,  2147,  2148,  2307,  3832, 3993,
                5502,  8838,  8998,  9002,  9166,  9318, 10887, 10959, 11203, 11209, 11365, 11439,
                11465, 11758, 11760, 11917, 11918, 12070, 12081, 12230, 12267, 12555, 12556, 12558,
                12562, 12996, 13372, 13638, 13639, 13799, 14139, 14621, 14777, 14940, 15350, 15750,
                15886, 16046, 16198, 16358, 18426, 18586, 19710, 19967, 20359, 20519, 22025, 23233,
                23234, 23393, 24397, 24483]

p1 = sp.Point3D(604168559/3014528, 365847001/3014528, 434531725/3014528)
p2 = sp.Point3D(667332817/3014528, 422798823/3014528, 532459571/3014528)
p3 = sp.Point3D(727605977/3014528, 701123231/3014528, 609120459/3014528)
p4 = sp.Point3D(664441719/3014528, 644171409/3014528, 511192613/3014528)
p5 = sp.Point3D(675203305/3014528, 383365391/3014528, 433322491/3014528)
p6 = sp.Point3D(738367563/3014528, 440317213/3014528, 531250337/3014528)
p7 = sp.Point3D(798640723/3014528, 718641621/3014528, 607911225/3014528)
p8 = sp.Point3D(735476465/3014528, 661689799/3014528, 509983379/3014528)

# ------------------------------------------------------------------------------------

# for 'resources/example5.jpg' --------------------------------------------------------

convexVerts5 = [ 805,   829,  1008,  1128,  1181,   1288,  1341,  3073,  4675,  4835,  4968,  5130,
                5190,  5192,  5274,  6306,  6432,   6478,  7025,  7338,  7419,  7450,  7720,  8136,
                8552,  8725,  8814,  8974, 9006,   10136, 10461, 10650, 10940, 10965, 11254, 11286,
                11287, 11443, 11444, 11603, 11605, 11610, 11765, 11766, 11926, 11927, 11930, 11974,
                12083, 12247, 12849, 12885, 12886, 12901, 13656, 13816, 13854, 13976, 14135, 14720,
                15058, 16187, 16347, 17532, 17573, 17733, 19894, 20862, 20863, 20875, 21279, 21366,
                21500, 21525, 21686, 21845, 22225, 23277, 23292, 24139, 24393, 24930]

a1 = sp.Point3D(957182623/4115015, 490729411/4115015, 644025782/4115015)
a2 = sp.Point3D(1049511192/4115015, 501122104/4115015, 660393138/4115015)
a3 = sp.Point3D(993200392/4115015, 452582704/4115015, 521463438/4115015)
a4 = sp.Point3D(900871823/4115015, 442190011/4115015, 505096082/4115015)
a5 = sp.Point3D(987565167/4115015, 943212099/4115015, 744978918/4115015)
a6 = sp.Point3D(1079893736/4115015, 953604792/4115015, 761346274/4115015)
a7 = sp.Point3D(1023582936/4115015, 905065392/4115015, 622416574/4115015)
a8 = sp.Point3D(931254367/4115015, 894672699/4115015, 606049218/4115015)

# ------------------------------------------------------------------------------------

# for 'resources/example6.jpg' -------------------------------------------------------
convexVerts6 = [1128,  1288,  1385,  2932,  2933,  3943,  7273,  7274,  7753,  7856,  9925,  9969,
                10128, 10456, 10593, 10595, 11195, 11353, 13920, 13921, 13923, 14080, 14081, 14233,
                14560, 14720, 14721, 14880, 14881, 15040, 16236, 17816, 18301, 18308, 18465, 18467,
                18468, 18613, 18614, 18625, 18627, 18784, 18787, 18901, 18930, 19091, 19429, 20062,
                20222, 21360, 21679, 21840, 22160, 22797]

f1 = sp.Point3D(627508814/2537521, 23409780/110327, 477579633/2537521)
f2 = sp.Point3D(547820484/2537521, 29023205/110327, 382158843/2537521)
f3 = sp.Point3D(429113771/2537521, 20734926/110327, 779422382/7612563)
f4 = sp.Point3D(508802101/2537521, 15121501/110327, 1065684752/7612563)
f5 = sp.Point3D(699938516/2537521, 17274828/110327, 471549797/2537521)
f6 = sp.Point3D(620250186/2537521, 22888253/110327, 376129007/2537521)
f7 = sp.Point3D(501543473/2537521, 14599974/110327, 761332874/7612563)
f8 = sp.Point3D(581231803/2537521, 8986549/110327, 1047595244/7612563)
# -------------------------------------------------------------------------------------


# for 'resources/example7.jpg' -------------------------------------------------------
convexVerts7 = [83,  1884,  1890,  1891,  1893,  2378,  3011,  3170,  3492,  3493, 3494,  3655,
                3814,  4116,  4121,  4281,  4435,  5083,  8891,  9051, 10348, 10987, 11144, 11145,
                11146, 11147, 11170, 11171, 11306, 11330, 11464, 11473, 11623, 11815, 11947, 11975,
                12098, 12118, 12278, 12437, 12598, 12638, 12798, 12903, 12907, 13243, 13383, 14498,
                14995, 15768, 15963, 16123, 17388, 18523, 20556, 20579, 20931, 21086, 21244, 21246,
                21247, 21251, 21253, 21256, 21257, 22166, 22526, 22530, 22534, 22860, 23324, 23325,
                23484, 23485, 23963, 24608, 24767, 24927]

z1 = sp.Point3D(31797874/145823, 16235887/145823, 43293941/291646)
z2 = sp.Point3D(37042104/145823, 20601448/145823, 26424082/145823)
z3 = sp.Point3D(36493491/145823, 19490676/145823, 43345645/291646)
z4 = sp.Point3D(31249261/145823, 15125115/145823, 16895711/145823)
z5 = sp.Point3D(32667094/145823, 32221633/145823, 25618384/145823)
z6 = sp.Point3D(37911324/145823, 36587194/145823, 60790991/291646)
z7 = sp.Point3D(37362711/145823, 35476422/145823, 25644236/145823)
z8 = sp.Point3D(32118481/145823, 31110861/145823, 41734249/291646)

# -------------------------------------------------------------------------------------

class TestProcessImage(TestCase):
    def test_filter_1(self):

        imgPath = 'resources/example.jpg'
        targetColor = (172, 140, 89)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 25,
            'maxG': 20
        }

        preconditions = {
            'convexVerts': convexVerts,
            'parallelepipedPoints': [q1, q2, q3, q4, q5, q6, q7, q8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, True, preconditions)

        self.assertEqual(os.path.exists('resources/results/example_filtered.png'), True)

    def test_binarize_1(self):
        imgPath = 'resources/example.jpg'
        targetColor = (172, 140, 89)
        isBinzrization = True
        deltaParams = {
            'minR': 34,
            'maxR': 34,
            'minG': 34,
            'maxG': 34
        }

        preconditions = {
            'convexVerts': convexVerts,
            'parallelepipedPoints': [q1, q2, q3, q4, q5, q6, q7, q8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, True, preconditions)

        self.assertEqual(os.path.exists('resources/results/example_binarized.png'), True)

    def test_filter_2(self):
        imgPath = 'resources/example2.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 40
        }

        isFarthestPointOrientation = False
        preconditions = {
            'convexVerts': convexVerts2,
            'parallelepipedPoints': [v1, v2, v3, v4, v5, v6, v7, v8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example2_filtered.png'), True)

    def test_binarize_2(self):
        imgPath = 'resources/example2.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 40
        }

        isFarthestPointOrientation = False
        preconditions = {
            'convexVerts': convexVerts2,
            'parallelepipedPoints': [v1, v2, v3, v4, v5, v6, v7, v8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example2_filtered.png'), True)

    def test_filter_3(self):
        imgPath = 'resources/example3.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 40
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts3,
            'parallelepipedPoints': [w1, w2, w3, w4, w5, w6, w7, w8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example3_filtered.png'), True)

    def test_binarize_3(self):
        imgPath = 'resources/example3.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 45
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts3,
            'parallelepipedPoints': [w1, w2, w3, w4, w5, w6, w7, w8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example3_binarized.png'), True)

    def test_filter_4(self):
        imgPath = 'resources/example4.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 40
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts4,
            'parallelepipedPoints': [p1, p2, p3, p4, p5, p6, p7, p8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example4_filtered.png'), True)

    def test_binarize_4(self):
        imgPath = 'resources/example4.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 50
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts4,
            'parallelepipedPoints': [p1, p2, p3, p4, p5, p6, p7, p8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example4_binarized.png'), True)

    def test_filter_5(self):
        imgPath = 'resources/example5.bmp'
        targetColor = (245, 222, 170)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 30,
            'maxG': 20
        }

        isFarthestPointOrientation = True

        preconditions = {
            'convexVerts': convexVerts5,
            'parallelepipedPoints': [a1, a2, a3, a4, a5, a6, a7, a8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example5_filtered.png'), True)

    def test_binarize_5(self):
        imgPath = 'resources/example5.bmp'
        targetColor = (245, 222, 170)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 30,
            'maxG': 20
        }

        isFarthestPointOrientation = True

        preconditions = {
            'convexVerts': convexVerts5,
            'parallelepipedPoints': [a1, a2, a3, a4, a5, a6, a7, a8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example4_binarized.png'), True)

    def test_filter_6(self):
        imgPath = 'resources/example6.bmp'
        targetColor = (228, 212, 166)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 30,
            'maxG': 55
        }

        isFarthestPointOrientation = True

        preconditions = {
            'convexVerts': convexVerts6,
            'parallelepipedPoints': [f1, f2, f3, f4, f5, f6, f7, f8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example6_filtered.png'), True)

    def test_binarize_6(self):
        imgPath = 'resources/example6.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 30,
            'maxG': 55
        }

        isFarthestPointOrientation = True

        preconditions = {
            'convexVerts': convexVerts6,
            'parallelepipedPoints': [f1, f2, f3, f4, f5, f6, f7, f8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example6_binarized.png'), True)

    def test_filter_7(self):
        imgPath = 'resources/example7.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = False
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 45
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts7,
            'parallelepipedPoints': [z1, z2, z3, z4, z5, z6, z7, z8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example7_filtered.png'), True)

    def test_binarize_7(self):
        imgPath = 'resources/example7.bmp'
        targetColor = (236, 222, 195)
        isBinzrization = True
        deltaParams = {
            'minR': 20,
            'maxR': 20,
            'minG': 0,
            'maxG': 60
        }

        isFarthestPointOrientation = False

        preconditions = {
            'convexVerts': convexVerts7,
            'parallelepipedPoints': [z1, z2, z3, z4, z5, z6, z7, z8]
        }

        processImage(imgPath, targetColor, deltaParams, isBinzrization, isFarthestPointOrientation, preconditions)

        self.assertEqual(os.path.exists('resources/results/example6_binarized.png'), True)
