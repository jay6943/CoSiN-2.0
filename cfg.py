work = '../mask/'
libs = '../mask/lib/'

data = []

draft = 'draft' # draft: 100, mask: 1000

phase = 90

wg = 2
wt = 1
eg = 30
ch = 250

sarg = 27
w1x2 = 5.6 * 2
l1x2 = 18 * 2
d1x2 = 1.46 * 2
w2x2 = 8.4 * 2
l2x2 = 51.5 * 2
d2x2 = 1.46 * 2
lpbs = 56.5
wpbs = 1.8
ltpr = 5
wtpr = 3
targ = 58
lvoa = 500

size = 10000
mask = 10900
area = [[1, 0], [-1, 0], [0, 0], [-1, -1], [0, -1]]

layer = {} # 2 for (0, 0) mask position
layer['core'] = 2
layer['edge'] = 2
layer['slab'] = 2
layer['fill'] = 2
layer['gold'] = 2
layer['keys'] = 2
layer['bars'] = 2
layer['hole'] = 2
layer['recs'] = 2
layer['tops'] = 2
layer['cuts'] = 2
layer['text'] = 2