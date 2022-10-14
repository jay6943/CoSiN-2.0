import cfg
import dxf
import dev
import cir
import euler as el

lwg = 10

def angle_45():

  cfg.work = 'D:/ansys/Euler/'
  
  x, y = dev.sline(0, 0, lwg)
  x, y = dev.sbend(x, y, 0, 45, 0, 1)
  x, y = dev.sline(x, y, lwg)

  dev.saveas('45')

def angle_45_taper():

  cfg.work = 'D:/ansys/Euler/'
  
  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.sbend(x, y, cfg.ch * 0.5, 45, 0, 1)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, lwg, cfg.wt)

  dev.saveas('45-taper')

def angle_90():

  cfg.work = 'D:/ansys/Euler/'

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)

  dev.saveas('90')

def angle_180():

  cfg.work = 'D:/ansys/Euler/'

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas('180')

def angle_180_taper():

  cfg.work = 'D:/ansys/Euler/'

  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.taper(x, y, -cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, -lwg, cfg.wt)

  dev.saveas('180-taper')

def angle_90x2():

  cfg.work = 'D:/ansys/Euler/'
  
  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)
  x, y = dev.bends(x, y, 90, 90, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas('90x2')

def sbend(angle):

  cfg.work = 'D:/ansys/Euler/'

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.sbend(x, y, cfg.ch * 0.5, angle, 0, 1)
  x, y = dev.sline(x, y, lwg)

  dev.saveas('sbend')

def dc_in_out():

  cfg.work = 'D:/ansys/DC/'

  df = cir.r5['0_90_' + cfg.draft]

  dxf.bends('core', 0, 0, df, 90, 1)
  dev.saveas('wg-1w-in')
  dxf.bends('core', 0, 0, df, 270, -1)
  dev.saveas('wg-1w-out')

def pbs_euler():

  r = 20
  g = 2.5

  cfg.work = 'D:/ansys/PBS/'
  
  s1 = el.update(r)[str(r) + '_90_mask']
  s2 = el.update(r + g)[str(r + g) + '_90_mask']

  df = cir.r5['0_90_' + cfg.draft]

  dxf.sline('core', 0, g, -10)
  x1, y1 = dxf.bends('core', 0, g, s1, 0, 1)
  dxf.tline('core', x1, y1, 10)

  dxf.bends('core', 0, 0, df, 90, 1)
  x1, y1 = dxf.bends('core', 0, 0, s2, 0, 1)
  dxf.tline('core', x1, y1, 10)

  dev.saveas('euler')

def pbs_cir():

  r = 10
  g = 1.2

  cfg.work = 'D:/ansys/PBS/'
  
  s1 = cir.update(cfg.wg, r, 0, 90)['0_90_mask']
  s2 = cir.update(cfg.wg, r + g, 0, 90)['0_90_mask']

  df = cir.r5['0_90_' + cfg.draft]

  dxf.sline('core', 0, g, -10)
  x1, y1 = dxf.bends('core', 0, g, s1, 270, 1)
  dxf.tline('core', x1, y1, 10)

  dxf.bends('core', 0, 0, df, 90, 1)
  x1, y1 = dxf.bends('core', 0, 0, s2, 270, 1)
  dxf.tline('core', x1, y1, 10)

  dev.saveas('cir')

if __name__ == '__main__':

  cfg.draft = 'mask'

  # angle_45()
  # angle_90()
  # angle_180()
  # angle_90x2()

  # sbend(27)
  
  # dc_in_out()

  # pbs_euler()
  pbs_cir()
