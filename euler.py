import os
import cfg
import dxf
import numpy as np
import scipy.special as ss

def curve(wg, radius, angle, m):

  width = wg * 0.5
  
  s = np.sqrt(angle / 180)
  c = np.sqrt(np.pi * 0.5)
  n = round(m * s)
  t = np.linspace(0, s, n)
  
  xt, yt = ss.fresnel(t)
  
  x = yt * c * radius
  y = xt * c * radius

  p = t * c

  px = np.sin(p * p)
  py = np.cos(p * p)

  rc = np.array([0] + (radius / p[1:] * 0.5).tolist())
  dx = x - rc * px
  dy = y + rc * py

  xinner = dx + (rc - width) * px
  yinner = dy - (rc - width) * py
  xouter = dx + (rc + width) * px
  youter = dy - (rc + width) * py

  xp = np.append(xinner, xouter[::-1])
  yp = np.append(yinner, youter[::-1])

  df = {}
  df['n'] = n
  df['x'] = xp
  df['y'] = yp
  df['dx'] = dx[-1]
  df['dy'] = dy[-1]

  return df

def rotate(df, oxt, rxt):

  dx = df['dx'] - oxt[0]
  dy = df['dy'] - oxt[1]

  cvt = rxt @ np.array([-df['x'], df['y']])
  cvt = cvt + np.array([dx, dy]).reshape(2,1)

  n = df['n']

  xp = np.array(df['x'][:n])
  yp = np.array(df['y'][:n])
  xp = np.append(xp, cvt[0][:n][::-1])
  yp = np.append(yp, cvt[1][:n][::-1])
  xp = np.append(xp, cvt[0][n:][::-1])
  yp = np.append(yp, cvt[1][n:][::-1])
  xp = np.append(xp, df['x'][n:])
  yp = np.append(yp, df['y'][n:])

  return xp, yp

def save(fp, wg, radius, angle, m):
  
  rxt = dxf.rxt(angle)
  obj = curve(wg, radius, angle, m)
  oxt = rxt @ np.array([-obj['dx'], obj['dy']]).reshape(2,1)

  xp, yp = rotate(obj, oxt, rxt)

  n = obj['n'] * 2

  df = {}
  df['n'] = n
  df['m'] = m
  df['x'] = xp
  df['y'] = yp
  df['r'] = radius
  df['w'] = wg
  df['dx'] = (xp[n-1] + xp[n]) * 0.5
  df['dy'] = (yp[n-1] + yp[n]) * 0.5
  df['angle'] = angle

  np.save(fp, df)

  print('euler', wg, radius, angle, m)

  return df
  
def update(wg, radius, angle, draft):

  m = 50 if draft != 'mask' else 1000
  w = wg if draft != 'edge' else cfg.eg

  ip = str(radius) + '_' + str(angle) + '_' + draft
  fp = cfg.libs + 'euler_' + ip + '.npy'

  changed = False
  if os.path.isfile(fp):
    df = np.load(fp, allow_pickle=True).item()
    if df['m'] != m: changed = True
    if df['w'] != w: changed = True
  else: changed = True
  
  return save(fp, w, radius, angle, m) if changed else df