import cfg
import dxf
import dev
import key
import ohm
import pbs
import psk
import tip
import tap
import icr
import y1x2
import y2x2

# key.frame(layer, quadrant, key position)
# 'recs' layer : stress released patterns
# 'fill' layer : filled with soild
# 'none' layer : not filled

x = key.wbar + key.wkey
y = key.wbar + key.wkey

def mask_1(fp):

  key.frame(1, 1)
  tip.scuts(x, y)
  dev.rectangles(x, y)

  cfg.layer['core'] = 1
  cfg.layer['edge'] = 1
  cfg.layer['cuts'] = 1
  cfg.layer['recs'] = 1

  dev.sline(x, y + cfg.ch * 0.5, cfg.size)
  ohm.chips(x, y + cfg.ch * 1.5)
  tip.chips(x, y + cfg.ch * 11.5, 0.16, 0.41, 0.05)
  y2x2.chips(x, y + cfg.ch * 19, 50.5, 52.5, 1)
  y1x2.chips(x, y + cfg.ch * 24.5, 16, 18, 1)
  tap.chips(x, y + cfg.ch * 35.5)
  dev.sline(x, y + cfg.ch * 39.5, cfg.size)

  dxf.conversion(fp)

def mask_2(fp):

  key.frame(2, 1)
  tip.scuts(x, y)
  dev.rectangles(x, y)

  cfg.layer['core'] = 2
  cfg.layer['edge'] = 2
  cfg.layer['cuts'] = 2
  cfg.layer['recs'] = 2
  
  psk.chips(x, y + cfg.ch * 2, 70, 75, 5)
  psk.chip(x, y + cfg.ch * 10, cfg.size)
  psk.chips(x, y + cfg.ch * 14, 80, 90,  10)
  psk.chips(x, y + cfg.ch * 22, 90, 80, -10)
  psk.chip(x, y + cfg.ch * 30, cfg.size)
  psk.chips(x, y + cfg.ch * 34, 95, 100, 5)

  for l in [tip.ltip + 100, cfg.size - tip.ltip]:
    dev.texts(x + l, y + cfg.ch * 10, '1', 0.5, 'lc')
    dev.texts(x + l, y + cfg.ch * 14, '1', 0.5, 'lc')
    dev.texts(x + l, y + cfg.ch * 18, '2', 0.5, 'lc')
    dev.texts(x + l, y + cfg.ch * 22, '3', 0.5, 'lc')
    dev.texts(x + l, y + cfg.ch * 26, '2', 0.5, 'lc')
    dev.texts(x + l, y + cfg.ch * 30, '4', 0.5, 'lc')
  
  dxf.conversion(fp)

def mask_3(fp):

  key.frame(3, 1)
  tip.scuts(x, y)
  dev.rectangles(x, y)

  cfg.layer['core'] = 3
  cfg.layer['edge'] = 3
  cfg.layer['cuts'] = 3
  cfg.layer['recs'] = 3

  pbs.chips(x, y + cfg.ch, 20, 58, 2)

  dxf.conversion(fp)

def mask_4(fp):

  key.frame(4, 1)
  tip.scuts(x, y)
  dev.rectangles(x, y)

  cfg.layer['core'] = 4
  cfg.layer['edge'] = 4
  cfg.layer['gold'] = 4
  cfg.layer['cuts'] = 4
  cfg.layer['recs'] = 4

  icr.chips(x, y + cfg.size * 0.5)

  dxf.conversion(fp)

if __name__ == '__main__':

  cfg.draft = 'draft' # draft or mask

  fp = dxf.start(cfg.work + cfg.draft)
  key.cross(0, 0)
  dxf.conversion(fp)

  mask_1(fp)
  mask_2(fp)
  mask_3(fp)
  mask_4(fp)

  dxf.close(fp)
  dev.removes('__pycache__/')