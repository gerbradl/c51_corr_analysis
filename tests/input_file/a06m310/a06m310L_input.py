import gvar as gv
import numpy as np

data_file = '../data/c51_2pt_octet_decuplet.h5'

fit_states = ['mres-L','mres-S', 'pion', 'kaon', 'omega']
#fit_states = ['pion', 'kaon', 'proton', 'omega']
bs_seed = 'a06m310L'
plot_name = 'a06m310L'
data_seed = 'a06m310L'
Tmax = 96
Tmid = 48

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
        'ylim'     :[0.09,0.1025],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'cosh',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.055,0.26],
        'eff_ylim' :[0.17,0.2],
        # optimal fit params
        'n_state'  :1,
        'T'        :Tmax,
        't_range'  :np.arange(21,Tmid),
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
        'ylim'     :[0.16,0.166],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'cosh',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.055,0.26],
        # fit params
        'n_state'  :2,
        'T'        :Tmax,
        't_range'  :np.arange(22,Tmid),
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
        'ylim'      :[1e-5,3e-5],
        'colors'    :'#70bf41',
        'type'      :'mres',
        # fit params
        't_range'   :np.arange(20,Tmid+1),
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
        'ylim'      :[1.0e-5,3.e-5],
        'colors'    :'#70bf41',
        'type'      :'mres',
        # fit params
        't_range'   :np.arange(20,Tmid+1),
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
        'ylim'     :[0.46,0.58],
        'colors'   :{'SS':'#70bf41','PS':'k'},
        'type'     :'exp',
        'ztype'    :'z_snk z_src',
        'z_ylim'   :[0.,0.0039],
        #'z_ylim'   :[0.,5],
        #'normalize':True,
        # fit params
        'n_state'  :3,
        't_range'  :np.arange(16,42),
        't_sweep'  :range(2,36),
        'n_sweep'  :range(1,6),
    },

}

priors = gv.BufferDict()
x      = dict()

priors['proton_E_0']  = gv.gvar(0.182, .005)
priors['proton_zS_0'] = gv.gvar(7.0e-4, 1.0e-4)
priors['proton_zP_0'] = gv.gvar(2.5e-3, 0.8e-3)

priors['omega_E_0']  = gv.gvar(0.5, .03)
priors['omega_zS_0'] = gv.gvar(3.2e-4, 7e-5)
priors['omega_zP_0'] = gv.gvar(6e-4, 3e-4)

priors['pion_E_0']  = gv.gvar(0.094, .002)
priors['pion_zS_0'] = gv.gvar(0.035, 0.005)
priors['pion_zP_0'] = gv.gvar(0.072,  0.006)

priors['kaon_E_0']  = gv.gvar(0.162, .001)
priors['kaon_zS_0'] = gv.gvar(0.03, 0.005)
priors['kaon_zP_0'] = gv.gvar(0.06, 0.005)

priors['mres-L']    = gv.gvar(2.3e-5, 2e-6)
priors['mres-S']    = gv.gvar(1.8e-5, 4e-6)

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
