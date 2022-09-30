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

def inner(x, y, yorg, sign):

  ch = cfg.ch * 0.5

  x1, y1 = dev.sbend(x, y, ch * 5, 45, 0, sign * 2)
  x2, y2 = dev.tline(x1, y1, sign * (yorg + yqpsk) - y1 * 2 + y)
  x3, y3 = dev.sbend(x2, y2, sign * ch * 4, 45, 90, -2)

  return x3, y3

def outer(x, y, yorg, sign):

  ch = cfg.ch * 0.5

  x1, y1 = dev.sbend(x, y, ch * 4, 45, 0, sign * 2)
  x2, y2 = dev.tline(x1, y1, sign * (yorg + yqpsk) - y1 * 2 + y)
  x3, y3 = dev.sbend(x2, y2, sign * ch * 5, 45, 90, -2)
  
  return x3, y3

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
  
  x2, y3 = dev.sbend(x1, y1, ch * 3, 45, 0,  1)
  x2, y4 = dev.sbend(x1, y2, ch * 3, 45, 0, -1)

  x3, _ = tap.device(x2, y3, ysize * 0.5 + ch * 5, -1)
  x4, _ = voa.device(x3, y3)
  x4, _ = dev.sline(x2, y4, x4 - x2)

  x5, y5 = dev.sbend(x4, y3, ch * 2, 45, 0, -1)
  x5, y6 = dev.sbend(x4, y4, ch * 2, 45, 0,  1)

  x7, y61, y62 = pbs.device(x5, y5)
  x7, y63, y64 = pbs.device(x5, y6)

  x10, _ = outer(x7, y61, y,  1)
  x10, _ = inner(x7, y62, y, -1)
  x10, _ = inner(x7, y63, y,  1)
  x10, _ = outer(x7, y64, y, -1)

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