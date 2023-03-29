# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:58:47 2023

@author: zhaiy
"""


import gvar as gv
import numpy as np

data_file = '../data/c51_2pt_octet_decuplet.h5'

fit_states = ['omega','pion','kaon','mres-L','mres-S']

bs_seed = 'a15m220'
plot_name = 'a15m220'

#give proton, lambda, sigma, xi the same t_range

corr_lst = {
    'omega':{
        'dsets'     :['a15m220/omega_m'],
        'xlim'      :[4,30],
        'ylim'      :[1.15,1.35],
        # optimal fit params
        'n_state'   :2,
        't_range'   :np.arange(8,16),
    },
    'pion':{
        'dsets'     :['a15m220/piplus'],
        'xlim'      :[3,40],
        'ylim'      :[0.16,0.18],
        # optimal fit params
        'n_state'   :3,
        't_range'   :np.arange(5,25),
    },
    'kaon':{
        'dsets'     :['a15m220/kplus'],
        'xlim'      :[5,40],
        'ylim'      :[0.384,0.395],
        # optimal fit params
        'n_state'   :3,
        't_range'   :np.arange(6,25),
    },
    'mres-L':{
        'corr_array':False,
        'dset_MP'   :['a15m220/mp_l'],
        'dset_PP'   :['a15m220/pp_l'],
        'xlim'      :[0,64.5],
        'ylim'      :[0.00052,0.00062],
        # optimal fit params
        't_range'   :np.arange(10,25),
    },
    'mres-S':{
        'corr_array':False,
        'dset_MP'   :['a15m220/mp_s'],
        'dset_PP'   :['a15m220/pp_s'],
        'xlim'      :[0,64.5],
        'ylim'      :[0.000325,0.00045],
        # optimal fit params
        't_range'   :np.arange(13,25),
    },
}
for corr in corr_lst:
    corr_lst[corr]['weights']   = [1]
    corr_lst[corr]['t_reverse'] = [False]
    if 'mres' in corr:
        corr_lst[corr]['snks']  = ['M', 'P']
        corr_lst[corr]['srcs']  = ['P']
        corr_lst[corr]['colors']= '#6a5acd'
    else:
        corr_lst[corr]['snks']  = ['S', 'P']
        corr_lst[corr]['srcs']  = ['S']
        corr_lst[corr]['colors']= {'SS':'#6a5acd','PS':'k'}
        corr_lst[corr]['ztype'] = 'z_snk z_src'
    if corr in ['pion', 'kaon'] or 'mres' in corr:
        corr_lst[corr]['fold']  = True
        corr_lst[corr]['T']     = 48
        if 'mres' in corr:
            corr_lst[corr]['type'] = 'mres'
        else:
            corr_lst[corr]['type'] = 'cosh'
            corr_lst[corr]['t_sweep'] = range(2,20)
            corr_lst[corr]['n_sweep'] = range(1,6)
    else:
        corr_lst[corr]['fold']  = False
        corr_lst[corr]['type']  = 'exp'
        corr_lst[corr]['t_sweep'] = range(2,15)
        corr_lst[corr]['n_sweep'] = range(1,6)


priors = gv.BufferDict()
x      = dict()


priors['omega_E_0']  = gv.gvar(1.2087, .04)
priors['omega_zS_0'] = gv.gvar(0.00217, 4e-4)
priors['omega_zP_0'] = gv.gvar(.0108, .002)

priors['pion_E_0']  = gv.gvar(0.165, .01)
priors['pion_zS_0'] = gv.gvar(0.09, 2e-2)
priors['pion_zP_0'] = gv.gvar(0.315, 10e-2)

priors['kaon_E_0']  = gv.gvar(0.3866, .004)
priors['kaon_zS_0'] = gv.gvar(0.059, 12e-3)
priors['kaon_zP_0'] = gv.gvar(0.201, 6e-2)

priors['mres-L']    = gv.gvar(0.0005747, 0.5e-4)
priors['mres-S']    = gv.gvar(0.0003878, 4e-5)


for corr in corr_lst:#[k for k in corr_lst if 'mres' not in k]:
    if 'mres' not in corr:
        for n in range(1,10):
            # use 2 mpi splitting for each dE

            # E_n = E_0 + dE_10 + dE_21 +...
            # use log prior to force ordering of dE_n
            priors['log(%s_dE_%d)' %(corr,n)] = gv.gvar(np.log(2*priors['pion_E_0'].mean), 0.7)

            # for z_P, no suppression with n, but for S, smaller overlaps
            zP_0 = priors['%s_zP_0' %(corr)]
            priors['%s_zP_%d' %(corr,n)] = gv.gvar(zP_0.mean, 3*zP_0.mean)

            zS_tag = 'S'
            zS_0 = priors['%s_z%s_0' %(corr, zS_tag)]
            if n <= 2:
                priors['%s_z%s_%d' %(corr, zS_tag, n)] = gv.gvar(zS_0.mean, 2*zS_0.mean)
            else:
                priors['%s_z%s_%d' %(corr, zS_tag, n)] = gv.gvar(0, zS_0.mean)
    # x-params
    for snk in corr_lst[corr]['snks']:
        sp = snk+corr_lst[corr]['srcs'][0]
        state = corr+'_'+sp
        x[state] = dict()
        x[state]['state'] = corr
        for k in ['type', 'T', 'n_state', 't_range', 'eff_ylim', 'ztype']:
            if k in corr_lst[corr]:
                x[state][k] = corr_lst[corr][k]
        if 't0' in corr_lst[corr]:
            x[state]['t0'] = corr_lst[corr]['t0']
        else:
            x[state]['t0'] = 0
        if 'mres' not in corr:
            x[state]['color'] = corr_lst[corr]['colors'][sp]
            x[state]['snk']   = snk
            x[state]['src']   = corr_lst[corr]['srcs'][0]
        else:
            x[state]['color'] = corr_lst[corr]['colors']





