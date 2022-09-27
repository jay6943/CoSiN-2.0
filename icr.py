import cfg
import dev
import pbs
import voa
import psk
import tip
import tap

yqpsk = 2400

xsize = cfg.size
ysize = 8000

def fiber_pd(x, y, lchip):

  x1, _ = tip.fiber(x, y, lchip * 0.5, -1)
  x2, _ = tip.pd(x1, y, lchip * 0.5, 1)

  return x2, y

def chip(x, y, lchip):
  
  ch = cfg.ch * 0.5

  y1 = y + ch
  y2 = y - ch
  
  ltip = tip.ltip + 100

  x1, _ = tip.fiber(x, y1, ltip, -1)
  x1, _ = tip.fiber(x, y2, ltip, -1)
  
  x2, y3 = dev.sbend(x1, y1, ch * 4, 45, 0,  1)
  x2, y4 = dev.sbend(x1, y2, ch * 4, 45, 0, -1)

  x3, _ = tap.device(x2, y3, ysize * 0.5 + ch * 5, -1)
  x4, _ = voa.device(x3, y3)
  x4, _ = dev.sline(x2, y4, x4 - x2)

  x5, y5 = dev.sbend(x4, y3, ch * 3, cfg.sarg, 0, -1)
  x5, y6 = dev.sbend(x4, y4, ch * 3, cfg.sarg, 0,  1)

  x6, _ = dev.sline(x5, y5, 500)
  x6, _ = dev.sline(x5, y6, 500)

  x7, y61, y62 = pbs.device(x6, y5)
  x7, y63, y64 = pbs.device(x6, y6)

  x9, y71 = dev.sbend(x7, y61, ch * 2, 45, 0,  2)
  x8, y72 = dev.sbend(x7, y62, ch * 4, 45, 0, -2)
  x8, y73 = dev.sbend(x7, y63, ch * 4, 45, 0,  2)
  x9, y74 = dev.sbend(x7, y64, ch * 2, 45, 0, -2)

  h1 = y + yqpsk - ch - y71 - (y71 - y61)
  h2 = y + yqpsk + ch - y73 - (y73 - y63)

  _, y81 = dev.tline(x9, y71,  h1)
  _, y82 = dev.tline(x8, y72, -h2)
  _, y83 = dev.tline(x8, y73,  h2)
  _, y84 = dev.tline(x9, y74, -h1)

  x10, _ = dev.sbend(x9, y81,  ch * 4, 45, 90, -2)
  x10, _ = dev.sbend(x8, y82, -ch * 2, 45, 90, -2)
  x10, _ = dev.sbend(x8, y83,  ch * 2, 45, 90, -2)
  x10, _ = dev.sbend(x9, y84, -ch * 4, 45, 90, -2)

  x11, y7 = psk.device(x10, y + yqpsk)
  x11, y8 = psk.device(x10, y - yqpsk)

  ltip = lchip - x11 + x

  for i in [-3,-1,1,3]:
    x12, _ = tip.pd(x11, y7 + i * ch, ltip, 1)
    x12, _ = tip.pd(x11, y8 + i * ch, ltip, 1)

  print('ICR chip length =', int(x12 - x))

  return x12, y

def chips(x, y):

  chip(x, y, xsize)

  fiber_pd(x, y + cfg.ch * 3.5 + yqpsk, xsize)
  voa.chip(x, y - cfg.size * 0.5 + cfg.ch * 2, xsize)
  pbs.chip(x, y + cfg.ch * 5 + yqpsk, xsize)
  psk.chip(x, y + 4500, xsize)

  dev.sline(x, y + ysize * 0.5, xsize)
  dev.sline(x, y - ysize * 0.5, xsize)

  return x + xsize, y
  
if __name__ == '__main__':

  chip(0, 0, xsize)

  dev.saveas('icr')