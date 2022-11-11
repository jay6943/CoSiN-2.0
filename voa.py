import cfg
import dev
import tip
import pad
import y1x2

xsize = cfg.size
ysize = cfg.ch * 4

def arm(x, y, sign):

  x1, y = dev.sline(x, y, cfg.lvoa)
  
  pad.electrode('gold', x, y, cfg.lvoa, cfg.wg + 2, sign)
  pad.electrode('edge', x, y, cfg.lvoa, cfg.eg, sign)

  return x1, y

def device(x, y):

  ch = cfg.ch * 0.5

  x2, y1, y2 = y1x2.device(x, y, 1)

  x3, y3 = dev.sbend(x2, y1,  ch, cfg.sarg, 0, 1)
  x3, y4 = dev.sbend(x2, y2, -ch, cfg.sarg, 0, 1)

  x5, y3 = arm(x3, y3,  1)
  x5, y4 = arm(x3, y4, -1)

  x9, y1 = dev.sbend(x5, y3, -ch, cfg.sarg, 0, 1)
  x9, y2 = dev.sbend(x5, y4,  ch, cfg.sarg, 0, 1)

  x10, y1, y2 = y1x2.device(x9, y, -1)

  return x10, y

def chip(x, y, lchip):

  ch = cfg.ch * 0.5

  idev = len(cfg.data)
  x1, _ = device(x, y)
  x2, ltip = dev.move(idev, x, x1, lchip)

  x3, t2 = tip.fiber(x, y, ltip, -1)
  x3, t3 = tip.fiber(x2, y, ltip, 1)

  s = 'voa-' + str(int(cfg.lvoa))
  dev.texts(t2, y + ch, s, 0.5, 'lc')
  dev.texts(t2, y - ch, s, 0.5, 'lc')
  dev.texts(t3, y + ch, s, 0.5, 'rc')
  dev.texts(t3, y - ch, s, 0.5, 'rc')
  print(s, int(x3 - x))

  return x3, y + ysize

def chips(x, y, start, stop, step):

  var = cfg.lvoa

  for cfg.lvoa in dev.arange(start, stop, step): _, y = chip(x, y, xsize)

  cfg.lvoa = var

  return x + xsize, y

if __name__ == '__main__':

  # chip(0, 0, 0)
  
  chips(0, 0, 500, 700, 100)

  dev.saveas(cfg.work + 'voa')