import cfg
import dxf
import dev
import cir
import euler as elr

lwg = 10

def angle_45(filename):

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.sbend(x, y, 0, 45, 0, 1)
  x, y = dev.sline(x, y, lwg)

  dev.saveas(filename)

def angle_45_taper(filename):

  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.sbend(x, y, cfg.ch * 0.5, 45, 0, 1)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, lwg, cfg.wt)

  dev.saveas(filename)

def angle_90(filename):

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)

  dev.saveas(filename)

def angle_180(filename):

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas(filename)

def angle_180_taper(filename):

  x, y = dev.srect(0, 0, lwg, cfg.wt)
  x, y = dev.taper(x, y, cfg.ltpr, cfg.wt, cfg.wg)
  x, y = dev.bends(x, y, 180, 0, 1)
  x, y = dev.taper(x, y, -cfg.ltpr, cfg.wg, cfg.wt)
  x, y = dev.srect(x, y, -lwg, cfg.wt)

  dev.saveas(filename)

def angle_90x2(filename):

  x, y = dev.sline(0, 0, lwg)
  x, y = dev.bends(x, y, 90, 0, 1)
  x, y = dev.tline(x, y, lwg)
  x, y = dev.bends(x, y, 90, 90, 1)
  x, y = dev.sline(x, y, -lwg)

  dev.saveas(filename)

def sbend(filename, angle):

  r = 50
  s = elr.update(r)[str(r) + '_' + angle + '_mask']

  x, y = dxf.sline('core', 0, 0, lwg)
  x, y = dxf.sbend('core', x, y, 50, s, angle, 1)
  x, y = dxf.sline('core', x, y, lwg)

  dev.saveas(filename)

def dc_in_out(filename):

  df = cir.r5['0_90_' + cfg.draft]

  dxf.bends('core', 0, 0, df, 90, 1)
  dev.saveas(filename + '-1.2w-in')

  dxf.bends('core', 0, 0, df, 270, 1)
  dev.saveas(filename + '-1.2w-out')

  r = 50
  s = elr.update(r)[str(r) + '_3_mask']

  x, y = dxf.sbend('core', 0, 0, 1, s, 0, 1)
  x, y = dxf.sline('core', x, y, 50)
  dev.saveas(filename, 'sbend-out-1')

  x, y = dxf.sbend('core', 0, 0, 1, s, 0, -1)
  x, y = dxf.sline('core', x, y, 50)
  dev.saveas(filename, 'sbend-out-2')

def pbs_euler(filename):

  r = 20
  g = 2.5
  
  s1 = elr.update(r)[str(r) + '_90_mask']
  s2 = elr.update(r + g)[str(r + g) + '_90_mask']

  df = cir.r5['0_90_' + cfg.draft]

  dxf.sline('core', 0, g, -10)
  x, y = dxf.bends('core', 0, g, s1, 0, 1)
  dxf.tline('core', x, y, 10)

  dxf.bends('core', 0, 0, df, 90, 1)
  x, y = dxf.bends('core', 0, 0, s2, 0, 1)
  dxf.tline('core', x, y, 10)

  dev.saveas(filename)

def pbs_cir(filename):

  r = 10
  g = 1.2

  s1 = cir.update(cfg.wg, r, 0, 90)['0_90_mask']
  s2 = cir.update(cfg.wg, r + g, 0, 90)['0_90_mask']

  df = cir.r5['0_90_' + cfg.draft]

  dxf.sline('core', 0, g, -10)
  x, y = dxf.bends('core', 0, g, s1, 270, 1)
  dxf.tline('core', x, y, 10)

  dxf.bends('core', 0, 0, df, 90, 1)
  x, y = dxf.bends('core', 0, 0, s2, 270, 1)
  dxf.tline('core', x, y, 10)

  dev.saveas(filename)

def soa(filename):

  s = cir.update(cfg.wg, 4000, 0, 9)['0_9_mask']

  x, y = dxf.sline('core', 0, 0, 10)
  x, y = dxf.bends('core', x, y, s, 270, -1)

  dev.saveas(filename)

def tap(filename):

  r = 50
  s = elr.update(r)[str(r) + '_9_mask']

  x1, y1 = dxf.sline('core', 0, 0, 10)
  x2, y2 = dxf.sbend('core', x1, y1, 5, s, 0, 1)
  x2, y1 = dxf.sline('core', x1, y1, x2 - x1)
  x1, y1 = dxf.sline('core', x2, y1, 10)
  x1, y2 = dxf.sline('core', x2, y2, 10)

  dev.saveas(filename)

if __name__ == '__main__':

  cfg.draft = 'mask'

  # angle_45('D:/ansys/Euler/45')
  # angle_90('D:/ansys/Euler/90')
  # angle_180('D:/ansys/Euler/180')
  # angle_90x2('D:/ansys/Euler/90x2')
  # sbend('D:/ansys/tap/sbend', 45)
  # dc_in_out('D:/ansys/tap/dc')
  # pbs_euler('D:/ansys/PBS/euler')
  # pbs_cir('D:/ansys/PBS/cir')
  # soa('D:/ansys/LD/soa')
  tap('D:/ansys/tap/tap9')