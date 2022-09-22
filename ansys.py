import cfg
import dxf
import dev
import euler

lwg = 10

def bend_45():

  df = euler.r125['45_' + cfg.draft]
  
  x1, y1 = dxf.sline('core', 0, 0, lwg)
  x2, y2 = dxf.sbend('core', x1, y1, 125, df, 0, 1)
  x3, y3 = dxf.sline('core', x2, y2, lwg)

  print('ANSYS Euler s-bend ...')
  dev.saveas('45')

def bend_45_taper():
  
  df = euler.r125['45_' + cfg.draft]
  
  x1, y1 = dxf.srect('core', 0, 0, lwg, cfg.wt)
  x2, y2 = dxf.taper('core', x1, y1, cfg.ltpr, cfg.wt, cfg.wg)
  x3, y3 = dxf.sbend('core', x2, y2, cfg.ch * 0.5, df, 0, 1)
  x4, y4 = dxf.taper('core', x3, y3, cfg.ltpr, cfg.wg, cfg.wt)
  x5, y5 = dxf.srect('core', x4, y4, lwg, cfg.wt)

  print('ANSYS Euler s-bend ...')
  dev.saveas('45_taper')

def bend_90():

  df = euler.r125['90_' + cfg.draft]

  x1, y1 = dxf.sline('core', 0, 0, lwg)
  x2, y2 = dxf.bends('core', x1, y1, df, 0, 1)
  x3, y3 = dxf.tline('core', x2, y2, lwg)

  print('ANSYS Euler bend with 90-deg rotation ...')
  dev.saveas('90')

def bend_180():

  df = euler.r125['180_' + cfg.draft]

  x1, y1 = dxf.sline('core', 0, 0, lwg)
  x2, y2 = dxf.bends('core', x1, y1, df, 0, 1)
  x3, y3 = dxf.sline('core', x2, y2, -lwg)

  print('ANSYS Euler bend with 180-deg rotation ...')
  dev.saveas('180')

def bend_180_taper():

  df = euler.r125['180_' + cfg.draft]

  x1, y1 = dxf.srect('core', 0, 0, lwg, cfg.wt)
  x2, y2 = dxf.taper('core', x1, y1, cfg.ltpr, cfg.wt, cfg.wg)
  x3, y3 = dxf.bends('core', x2, y2, df, 0, 1)
  x4, y4 = dxf.taper('core', x3, y3, -cfg.ltpr, cfg.wg, cfg.wt)
  x5, y5 = dxf.srect('core', x4, y4, -lwg, cfg.wt)

  print('ANSYS Euler bend with 180-deg rotation ...')
  dev.saveas('180_taper')

def bend_90x2():
  
  df = euler.r125['90_' + cfg.draft]
  
  x1, y1 = dxf.sline('core', 0, 0, lwg)
  x2, y2 = dxf.bends('core', x1, y1, df, 0, 1)
  x3, y3 = dxf.tline('core', x2, y2, lwg)
  x4, y4 = dxf.bends('core', x3, y3, df, 90, 1)
  x5, y5 = dxf.sline('core', x4, y4, -lwg)

  print('ANSYS Euler bend with 2 x 90-deg rotation ...')
  dev.saveas('90x2')

if __name__ == '__main__':

  cfg.work = 'D:/ansys/Euler/'

  cfg.draft = 'mask'

  bend_45()
  # bend_90()
  # bend_180()
  # bend_90x2()
  # bend_45_taper()