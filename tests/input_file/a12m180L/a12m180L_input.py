import gvar as gv
import numpy as np

data_file = '../data/c51_2pt_octet_decuplet.h5'

fit_states = ['mres-L','mres-S', 'pion', 'kaon', 'omega']
#fit_states = ['omega']
bs_seed = 'a12m180L'
plot_name = 'a12m180L'
data_seed = 'a12m180L'
Tmax = 64
Tmid = 32

corr_lst = {
    # PION
    'pion':{
        'dsets':[data_seed + '/piplus'],
        'weights'  :[1],
        't_reverse':[False],
        'fold'     :True,
        'snks'     :['S', 'P'],
        'srcs'     :['S'],
        'xlim'     :[0,Tmid + 0.5],
        'ylim'     :[0.095,0.13],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'cosh',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.055,0.26],
        'eff_ylim' :[0.17,0.2],
        # optimal fit params
        'n_state'  :2,
        'T'        :Tmax,
        't_range'  :np.arange(15,Tmid),
        # stability fit parameters
        't_sweep'  :range(2,28),
        'n_sweep'  :range(1,6),
    },
    # KAON
    'kaon':{
        'dsets':[data_seed + '/kplus'],
        'weights'  :[1],
        't_reverse':[False],
        'fold'     :True,
        'snks'     :['S', 'P'],
        'srcs'     :['S'],
        'xlim'     :[0,Tmid+0.5],
        'ylim'     :[0.30,0.32],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'cosh',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.055,0.26],
        # fit params
        'n_state'  :2,
        'T'        :Tmax,
        't_range'  :np.arange(20,Tmid),
        't_sweep'  :range(2,28),
        'n_sweep'  :range(1,6),
        'eff_ylim' :[0.133,0.1349]
    },
    # MRES_L
    'mres-L':{
        'corr_array':False,
        'dset_MP'   :[data_seed + '/mp_l'],
        'dset_PP'   :[data_seed + '/pp_l'],
        'weights'   :[1],
        't_reverse' :[False],
        'fold'      :True,
        'T'         :Tmax,
        'snks'      :['M', 'P'],
        'srcs'      :['P'],
        'xlim'      :[0,Tmid + 0.5],
        'ylim'      :[2.6e-4,3.4e-4],
        'colors'    :'#70bf41',
        'type'      :'mres',
        # fit params
        't_range'   :np.arange(12,Tmid+1),
        't_sweep'   :range(2,28),
    },
    # MRES_S
    'mres-S':{
        'corr_array':False,
        'dset_MP'   :[data_seed + '/mp_s'],
        'dset_PP'   :[data_seed + '/pp_s'],
        'weights'   :[1],
        't_reverse' :[False],
        'fold'      :True,
        'T'         :Tmax,
        'snks'      :['M', 'P'],
        'srcs'      :['P'],
        'xlim'      :[0,Tmid + 0.5],
        'ylim'      :[1.4e-4,2.3e-4],
        'colors'    :'#70bf41',
        'type'      :'mres',
        # fit params
        't_range'   :np.arange(8,Tmid+1),
        't_sweep'   :range(2,28),
    },
    # PROTON
    'proton':{
        'dsets':[data_seed + '/proton'],
        'weights'  :[1.],
        't_reverse':[False],
        'phase'    :[1],
        'fold'     :False,
        'snks'     :['S', 'P'],
        'srcs'     :['S'],
        'xlim'     :[0,25.5],
        'ylim'     :[0.425,0.575],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'exp',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.,0.0039],
        # fit params
        'n_state'  :4,
        't_range'  :np.arange(6,20),
        't_sweep'  :range(2,18),
        'n_sweep'  :range(1,6),
    },
    # OMEGA
    'omega':{
        'dsets':[data_seed + '/omega_m'],
        'weights'  :[1.],
        't_reverse':[False],
        'phase'    :[1],
        'fold'     :False,
        'snks'     :['S', 'P'],
        'srcs'     :['S'],
        'xlim'     :[0,28.5],
        'ylim'     :[0.95,1.1],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'exp',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.,0.0039],
        #'z_ylim'   :[0.,5],
        #'normalize':True,
        # fit params
        'n_state'  :3,
        't_range'  :np.arange(10,20),
        't_sweep'  :range(2,16),
        'n_sweep'  :range(1,6),
    },

}

priors = gv.BufferDict()
x      = dict()

priors['proton_E_0']  = gv.gvar(0.182, .0055)
priors['proton_zS_0'] = gv.gvar(7.0e-4, 1.5e-4)
priors['proton_zP_0'] = gv.gvar(2.5e-3, 0.85e-3)

priors['omega_E_0']  = gv.gvar(0.99, .025)
priors['omega_zS_0'] = gv.gvar(0.0017, 0.0005)
priors['omega_zP_0'] = gv.gvar(0.0055, 0.001)

priors['pion_E_0']  = gv.gvar(0.11, .0065)
priors['pion_zS_0'] = gv.gvar(0.09, 0.015)
priors['pion_zP_0'] = gv.gvar(0.25,  0.025)

priors['kaon_E_0']  = gv.gvar(0.306, .003)
priors['kaon_zS_0'] = gv.gvar(0.055, 0.01)
priors['kaon_zP_0'] = gv.gvar(0.15, 0.025)

priors['mres-L']    = gv.gvar(3.05e-4, 1.5e-5)
priors['mres-S']    = gv.gvar(1.9e-4, 1.5e-5)

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