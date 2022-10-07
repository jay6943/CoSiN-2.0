import cfg
import dxf
import dev
import cir

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

if __name__ == '__main__':

  cfg.draft = 'mask'

  # angle_45()
  # angle_90()
  # angle_180()
  # angle_90x2()

  # sbend(27)
  
  dc_in_out()
