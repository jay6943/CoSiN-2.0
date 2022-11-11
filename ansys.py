import cfg
import dxf
import dev
import cir
import euler as elr

lwg = 10

def angle_45(folder):

  cfg.work = folder
  
  x, y = dev.sline(0, 0, lwg)
  x, y = dev.sbend(x, y, 0, 45, 0, 1)
  x, y = dev.sline(x, y, lwg)

  dev.saveas('45')

def angle_45_taper(folder):

  cfg.work = folder
  
  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.sbend(x, y, cfg.ch * 0.5, 45, 0, 1)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, lwg, cfg.wt)

  dev.saveas('45-taper')

def angle_90(folder):

  cfg.work = folder

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)

  dev.saveas('90')

def angle_180(folder):

  cfg.work = folder

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas('180')

def angle_180_taper(folder):

  cfg.work = folder

  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.taper(x, y, -cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, -lwg, cfg.wt)

  dev.saveas('180-taper')

def angle_90x2(folder):

  cfg.work = folder
  
  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)
  x, y = dev.bends(x, y, 90, 90, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas('90x2')

def sbend(folder, angle):

  cfg.work = folder

  r = 50
  s = elr.update(r)[str(r) + '_' + angle + '_mask']

  x, y = dxf.sline('core', 0, 0, lwg)
  x, y = dxf.sbend('core', x, y, 50, s, angle, 1)
  x, y = dxf.sline('core', x, y, lwg)

  dev.saveas('sbend')

def dc_in_out(folder):

  cfg.work = folder

  df = cir.r5['0_90_' + cfg.draft]

  dxf.bends('core', 0, 0, df, 90, 1)
  dev.saveas('wg-1.2w-in')

  dxf.bends('core', 0, 0, df, 270, 1)
  dev.saveas('wg-1.2w-out')

  r = 50
  s = elr.update(r)[str(r) + '_3_mask']

  x, y = dxf.sbend('core', 0, 0, 1, s, 0, 1)
  x, y = dxf.sline('core', x, y, 50)
  dev.saveas('sbend-out-1')

  x, y = dxf.sbend('core', 0, 0, 1, s, 0, -1)
  x, y = dxf.sline('core', x, y, 50)
  dev.saveas('sbend-out-2')

def pbs_euler(folder):

  cfg.work = folder

  r = 20
  g = 2.5
  
  s1 = elr.update(r)[str(r) + '_90_mask']
  s2 = elr.update(r + g)[str(r + g) + '_90_mask']

  df = cir.r5['0_90_' + cfg.draft]

  dxf.sline('core', 0, g, -10)
  x1, y1 = dxf.bends('core', 0, g, s1, 0, 1)
  dxf.tline('core', x1, y1, 10)

  dxf.bends('core', 0, 0, df, 90, 1)
  x1, y1 = dxf.bends('core', 0, 0, s2, 0, 1)
  dxf.tline('core', x1, y1, 10)

  dev.saveas('euler')

def pbs_cir(folder):

  cfg.work = folder

  r = 10
  g = 1.2

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

def soa(folder):

  cfg.work = folder

  s = cir.update(cfg.wg, 4000, 0, 9)['0_9_mask']

  x1, y1 = dxf.sline('core', 0, 0, 10)
  x1, y1 = dxf.bends('core', x1, y1, s, 270, -1)

  dev.saveas('soa')

if __name__ == '__main__':

  cfg.draft = 'mask'

  # angle_45('D:/ansys/Euler/')
  # angle_90('D:/ansys/Euler/')
  # angle_180('D:/ansys/Euler/')
  # angle_90x2('D:/ansys/Euler/')
  # sbend('D:/ansys/tap/', 45)
  dc_in_out('D:/ansys/tap/')
  # pbs_euler('D:/ansys/PBS/')
  # pbs_cir('D:/ansys/PBS/')

  # soa('D:/ansys/LD/')