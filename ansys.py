import cfg
import dxf
import dev

lwg = 10

def bend_45():
  
  x1, y1 = dev.sline(0, 0, lwg)
  x2, y2 = dev.sbend(x1, y1, 125, 45, 0, 1)
  x3, y3 = dev.sline(x2, y2, lwg)

  print('ANSYS Euler s-bend ...')
  dev.saveas('bend_45')

def bend_45_taper():
  
  x1, y1 = dev.srect(0, 0, lwg, cfg.wt)
  x2, y2 = dev.taper(x1, y1, cfg.ltpr, cfg.wt, cfg.wg)
  x3, y3 = dev.sbend(x2, y2, cfg.ch * 0.5, 45, 0, 1)
  x4, y4 = dev.taper(x3, y3, cfg.ltpr, cfg.wg, cfg.wt)
  x5, y5 = dev.srect(x4, y4, lwg, cfg.wt)

  print('ANSYS Euler s-bend ...')
  dev.saveas('bend_45_taper')

def bend_90():

  x1, y1 = dev.sline(0, 0, lwg)
  x2, y2 = dev.bends(x1, y1, 90, 0, 1)
  x3, y3 = dev.tline(x2, y2, lwg)

  print('ANSYS Euler bend with 90-deg rotation ...')
  dev.saveas('bend_90')

def bend_180():

  x1, y1 = dev.sline(0, 0, lwg)
  x2, y2 = dev.bends(x1, y1, 180, 0, 1)
  x3, y3 = dev.sline(x2, y2, -lwg)

  print('ANSYS Euler bend with 180-deg rotation ...')
  dev.saveas('bend_180')

def bend_180_taper():

  x1, y1 = dev.srect(0, 0, lwg, cfg.wt)
  x2, y2 = dev.taper(x1, y1, cfg.ltpr, cfg.wt, cfg.wg)
  x3, y3 = dev.bends(x2, y2, 180, 0, 1)
  x4, y4 = dev.taper(x3, y3, -cfg.ltpr, cfg.wg, cfg.wt)
  x5, y5 = dev.srect(x4, y4, -lwg, cfg.wt)

  print('ANSYS Euler bend with 180-deg rotation ...')
  dev.saveas('bend_180_taper')

def bend_90x2():
  
  x1, y1 = dev.sline(0, 0, lwg)
  x2, y2 = dev.bends(x1, y1, 90, 0, 1)
  x3, y3 = dev.tline(x2, y2, lwg)
  x4, y4 = dev.bends(x3, y3, 90, 90, 1)
  x5, y5 = dev.sline(x4, y4, -lwg)

  print('ANSYS Euler bend with 2 x 90-deg rotation ...')
  dev.saveas('bend_90x2')

import numpy as np

def wave(x, y, l, w, sign):

  t = np.linspace(0, 1, int(l * 100) + 1)

  xt = t * l
  yt = 0.5 * w * np.sin((t  + (1 - sign) * 0.5 ) * np.pi * 0.5)

  xp = np.concatenate([xt,  xt[::-1]]) + x
  yp = np.concatenate([yt, -yt[::-1]]) + y

  data = np.array([xp, yp]).transpose()
  cfg.data.append(['core'] + data.tolist())

  return x + l, y

def wave_tip():

  t = 25
  l = 20
  w = 0.5
  d = t - l

  x1, _ = dxf.srect('core', 0, 0, 10, w)
  x2, _ = wave(x1, 0, l, w, -1)

  for _ in range(5):
    x2, _ = wave(x2 + d * 2, 0, l, w,  1)
    x2, _ = wave(x2, 0, l, w, -1)

  dev.saveas('wave_tip')

if __name__ == '__main__':

  cfg.draft = 'mask'

  # bend_45()
  # bend_90()
  # bend_180()
  # bend_90x2()
  # bend_45_taper()

  wave_tip()
