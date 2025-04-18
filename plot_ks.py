#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import util as u

# ========================================= #
# plot all k2 tidal's over the evolution    #
# ========================================= #

# ========================================= #
# INITIAL SET UP                            #
# ========================================= #

s     = np.logspace(-5,5,100)
nrun  = 2
ntime = 40
ldeg  = 2

# ========================================= #
# READ IN MODE AND CALCULATE HS             #
# ========================================= #

kf = np.zeros((ntime,nrun))

color = plt.cm.winter(np.linspace(0,1,ntime))
for irun in range(nrun):
  plt.figure(irun+1,figsize=(6,3))
  for j in range(ntime):
    id  = '_run'+str(irun)+'_time'+str(j)
    fin = 'love/prem'+id
    [l,nm,sk,\
       el,vl,\
       et,vt,\
       rl,rt] = u.jxmin(fin)
    idx = np.where(l==ldeg)[0][0]
    kt  = et[idx,-1]
    rk  = rt[idx][:,-1]
    ks  = u.calc_hs(kt,rk,\
                    sk[idx],s)
    kf[j,irun] = vt[idx,-1]
    plt.semilogx(s,ks,color=color[j],lw=1)
    if (j==0):
      plt.semilogx(s,ks,color='k',lw=2)
  plt.xlabel(r'$s$ (ky$^{-1}$)')
  plt.ylabel(r'$k_2^T$')
  plt.tight_layout()
  #plt.savefig('ks_run'+str(irun)+'.pdf')

# plot stiffer:
plt.figure(1)
id  = '_run77_time0'
fin = 'love/prem'+id
[l,nm,sk,\
   el,vl,\
   et,vt,\
   rl,rt] = u.jxmin(fin)
idx = np.where(l==ldeg)[0][0]
kt  = et[idx,-1]
rk  = rt[idx][:,-1]
ks  = u.calc_hs(kt,rk,\
                sk[idx],s)
plt.semilogx(s,ks,'k--',lw=1)


plt.figure(nrun+1,figsize=(6,3))
t = np.linspace(0.5,4.0,ntime)
plt.plot(t,kf[:,0],'k-')
plt.plot(t,kf[:,1],'k--')
plt.xlabel(r'$t$ (Gy)')
plt.ylabel(r'$k_2^T$')
plt.legend(['run 1','run 2'],frameon=False)
plt.tight_layout()

plt.show()
