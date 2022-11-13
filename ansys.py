import pya
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

def sbend(filename, radius, angle):

  df = elr.update(cfg.wg, radius, angle, 'mask')

  x, y = dxf.sline('core', 0, 0, lwg)
  x, y = dxf.sbend('core', x, y, 50, df, angle, 1)
  x, y = dxf.sline('core', x, y, lwg)

  dev.saveas(filename)

def dc_in_out(filename):

  df = cir.update(cfg.wg, 20, 90, 'mask')

  dxf.bends('core', 0, 0, df, 90, 1)
  dev.saveas(filename + '-in')

  dxf.bends('core', 0, 0, df, 270, 1)
  dev.saveas(filename + '-out')

  df = elr.update(cfg.wg, 20, 5, 'mask')

  x, y = dxf.sbend('core', 0, 0, 1, df, 0, 1)
  x, y = dxf.sline('core', x, y, 10)
  dev.saveas(filename + '-1')

  x, y = dxf.sbend('core', 0, 0, 1, df, 0, -1)
  x, y = dxf.sline('core', x, y, 10)
  dev.saveas(filename + '-2')

def soa(filename):

  df = cir.update(cfg.wg, 4000, 0, 9)['0_9_mask']

  x, y = dxf.sline('core', 0, 0, 10)
  x, y = dxf.bends('core', x, y, df, 270, -1)

  dev.saveas(filename)

def tap_device(x, y, df, sign):

  ch = 5
  wg = 0.4
  l = 10
  t = 20

  x1, y1 = dxf.srect('core', x, y, l, cfg.wg)
  x2, y1 = dxf.taper('core', x1, y1, l, cfg.wg, wg)
  x3, y2 = dxf.sbend('core', x2, y1, -sign * ch, df, 0, 1)
  x4, y2 = dxf.srect('core', x3, y2, t, wg)
  x5, y1 = dxf.sbend('core', x4, y2, sign * ch, df, 0, 1)
  x6, y1 = dxf.taper('core', x5, y1, l, wg, cfg.wg)
  x7, y1 = dxf.srect('core', x6, y1, l, cfg.wg)

  return x7, y1

def tap(filename):

  df = elr.update(cfg.wg, 10, 15, 'mask')

  tap_device(0, 0, df, 1)
  dev.saveas(filename + '-1')

  tap_device(0, 0, df, -1)
  dev.saveas(filename + '-2')

def y2x2(filename):

  ch = cfg.ch * 0.5
  dy = 6

  s1 = elr.update(cfg.wg, 125, 45, 'mask')
  s2 = elr.update(0.4, 10, 15, 'mask')

  x1, y1 = dxf.sbend('core', 0,  ch, ch - dy, s1, 0, -1)
  x1, y2 = dxf.sbend('core', 0, -ch, ch - dy, s1, 0,  1)
  x2, y1 = tap_device(x1, y1, s2,  1)
  x2, y2 = tap_device(x1, y2, s2, -1)
  x3, y3 = dxf.sbend('core', x2, y1, ch - dy, s1, 0,  1)
  x3, y4 = dxf.sbend('core', x2, y2, ch - dy, s1, 0, -1)
  dev.saveas(filename)

if __name__ == '__main__':

  cfg.draft = 'mask'

  # angle_45('D:/ansys/Euler/45')
  # angle_90('D:/ansys/Euler/90')
  # angle_180('D:/ansys/Euler/180')
  # angle_90x2('D:/ansys/Euler/90x2')
  # sbend('D:/ansys/tap/sbend', 45)
  # dc_in_out('C:/Git/mask/v2.0/dc')
  # pbs_euler('D:/ansys/PBS/euler')
  # pbs_cir('D:/ansys/PBS/cir')
  # soa('D:/ansys/LD/soa')
  # tap('C:/Git/mask/v2.0/tap')
  y2x2('C:/Git/mask/v2.0/2x2')