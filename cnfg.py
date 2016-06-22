# common imports
from __init__ import *

# internal functions
from main import init
from visu import *

def cnfg_ferm_psfn_expr(psfntype):
     
    init( \
         numbswep=100000, \
         factthin=1, \
         trueinfo=True, \
         datatype='inpt', \
         psfntype=psfntype, \
         maxmgang=10., \
         minmflux=array([1e-8]), \
         maxmflux=array([1e-7]), \
         regitype='ngal', \
         strgexpr='fermflux_ngal.fits', \
         strgexpo='fermexpo_ngal.fits', \
         maxmnormback=array([5., 5.]), \
         minmnormback=array([0.2, 0.2]), \
         probprop=array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), \
        )
                
    
def cnfg_ferm_info():
    
    minmflux = array([1e-9, 3e-10, 1e-10, 3e-11, 1e-11])
    maxmnumbpnts = zeros(5, dtype=int) + 500
    numbswep = zeros(5, dtype=int) + 1000000
    numbburn = numbswep / 2
    
    numbiter = minmflux.size

    listlevi = zeros(numbiter)
    listinfo = zeros(numbiter)
    
    strgexpo='fermexpo_cmp0_ngal.fits'
    strgexpr='fermflux_cmp0_ngal.fits'

    indxenerincl = arange(2, 3)
    indxevttincl = arange(3, 4)
    numbener = indxenerincl.size

    for k in range(numbiter):
        
        gridchan = init( \
                        psfntype='doubking', \
                        numbswep=numbswep[k], \
                        numbburn=numbburn[k], \
                        #probprop=array([0.1, 0.1, 0., 0.1, 0., 0., 0, 0, 1., 1., 1., 1.], dtype=float), \
                        trueinfo=True, \
                        randinit=False, \
                        makeplot=True, \
                        maxmgang=20., \
                        maxmnumbpnts=array([maxmnumbpnts[k]]), \
                        indxenerincl=indxenerincl, \
                        indxevttincl=indxevttincl, \
                        minmflux=minmflux[k], \
                        maxmflux=1e-7, \
                        regitype='ngal', \
                        maxmnormback=array([5., 5.]), \
                        minmnormback=array([0.2, 0.2]), \
                        strgexpo=strgexpo, \
                        datatype='inpt', \
                        strgexpr=strgexpr, \
                       )
        
        listlevi[k] = gridchan[-2]
        listinfo[k] = gridchan[-1]

    plot_minmfluxinfo(minmflux, listinfo, listlevi)


def cnfg_ferm_expr_igal(strgexpr='fermflux_cmp0_igal.fits', strgexpo='fermexpo_cmp0_igal.fits'):
      
    init( \
         psfntype='singking', \
         numbswep=200000, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=10., \
         indxenerincl=arange(1, 4), \
         indxevttincl=arange(2, 4), \
         minmflux=3e-11, \
         maxmflux=3e-6, \
         regitype='igal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo=strgexpo, \
         datatype='inpt', \
         strgexpr=strgexpr, \
        )
    
    
def cnfg_ferm_mock_igal():
     
    indxevttincl = arange(2, 4)
    indxenerincl = arange(1, 4)
    numbener = indxenerincl.size

    minmflux = 5e-11
    maxmflux = 3e-7
    mockfdfnslop = array([1.9])
      
    init( \
         psfntype='doubking', \
         numbswep=1000000, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=20., \
         indxevttincl=indxevttincl, \
         indxenerincl=indxenerincl, \
         numbsideheal=256, \
         mocknumbpnts=array([800]), \
         maxmnumbpnts=array([1200]), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         mocknormback=ones((2, numbener)), \
         maxmnormback=array([2., 2.]), \
         mockfdfnslop=mockfdfnslop, \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_igal.fits', \
         regitype='igal', \
         datatype='mock', \
        )


def intr_ferm_expr_ngal( \
                        strgexpr='fermflux_cmp0_ngal.fits', \
                        strgexpo='fermexpo_cmp0_ngal.fits', \
                        strgback=['fermisotflux.fits', 'fermfdfmflux_ngal.fits'] \
                       ): 
    karg = {}
    karg['psfntype'] = 'doubking'
    karg['numbswep'] = 2000000
    karg['randinit'] = False
    karg['maxmgang'] = 20.
    karg['maxmnumbpnts'] = array([500])
    karg['indxenerincl'] = arange(1, 4)
    karg['indxevttincl'] = arange(2, 4)
    karg['minmflux'] = 3e-11
    karg['maxmflux'] = 1e-7
    karg['regitype'] = 'ngal'
    karg['maxmnormback'] = array([2., 2.])
    karg['minmnormback'] = array([0.5, 0.5])
    karg['strgback'] = strgback
    karg['strgexpo'] = strgexpo
    karg['datatype'] = 'inpt'
    karg['strgexpr'] = strgexpr

    return karg


def cnfg_ferm_expr_ngal():
    karg = intr_ferm_expr_ngal(strgexpr='fermflux_cmp0_ngal.fits', strgexpo='fermexpo_cmp0_ngal.fits')
    init(**karg)


def cnfg_ferm_expr_ngal_cmp1():
    karg = intr_ferm_expr_ngal(strgexpr='fermflux_cmp1_ngal.fits', strgexpo='fermexpo_cmp1_ngal.fits')
    init(**karg)


def cnfg_ferm_expr_ngal_cmp2():
    karg = intr_ferm_expr_ngal(strgexpr='fermflux_cmp2_ngal.fits', strgexpo='fermexpo_cmp2_ngal.fits')
    init(**karg)


def cnfg_ferm_expr_ngal_cmp3():
    karg = intr_ferm_expr_ngal(strgexpr='fermflux_cmp3_ngal.fits', strgexpo='fermexpo_cmp3_ngal.fits')
    init(**karg)


def cnfg_ferm_expr_ngal_full():
    karg = intr_ferm_expr_ngal(strgexpr='fermflux_full_ngal.fits', strgexpo='fermexpo_full_ngal.fits')
    init(**karg)


def cnfg_ferm_expr_ngal_dust():
    karg = intr_ferm_expr_ngal(strgback=['fermisotflux.fits', 'fermdustflux_ngal.fits'])
    init(**karg)


def cnfg_test( \
              strgexpr='fermflux_cmp0_ngal.fits', \
              strgexpo='fermexpo_cmp0_ngal.fits', \
              strgback=['fermisotflux.fits', 'fermfdfmflux_ngal.fits'], \
             ):
   
    indxenerincl = arange(1, 4)
    indxevttincl = arange(2, 4)
    minmflux = 3e-11
    maxmflux = 1e-10
        
    init(psfntype='doubking', \
         numbswep=6000, \
         numbburn=0, \
         factthin=2000, \
         numbproc=3, \
         randinit=False, \
         maxmgang=20., \
         maxmnumbpnts=array([9]), \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         makeplot=True, \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgback=strgback, \
         strgexpo=strgexpo, \
         datatype='inpt', \
         strgexpr=strgexpr, \
        )
    
    
def cnfg_ferm_post():
     
    indxenerincl = arange(1, 3)
    indxevttincl = arange(2, 4)
    
    numbener = indxenerincl.size
    init(psfntype='gausking', \
		 numbswep=500000, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=1.5, \
         margsize=0., \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         maxmnumbpnts=array([3]), \
         mocknumbpnts=array([3]), \
         probprop=array([0., 0., 0., 0.1, 0., 0., 0, 0, 1., 1., 1., 1.], dtype=float), \
         minmflux=array([3e-8]), \
         maxmflux=array([1e-7]), \
         regitype='ngal', \
         maxmnormback=array([2.]), \
         minmnormback=array([0.5]), \
         strgback=['fermisotflux.fits'], \
         lablback=[r'$\mathcal{I}$'], \
         nameback=['normisot'], \
         strgexpo='fermexpo_ngal_cmp0.fits', \
         stdvback=0.3, \
         stdvlbhl=0.01, \
         stdvflux=0.05, \
         stdvsind=0.05, \
         datatype='mock', \
         numbsideheal=256, \
         mockfdfnslop=array([1.9]), \
         mocknormback=ones((1, numbener)), \
        )


def cnfg_test_spmr():
     
    indxenerincl = arange(1, 4)
    indxevttincl = arange(2, 4)
    numbener = indxenerincl.size

    minmflux = 3e-11
    maxmflux = 1e-7
    mockfdfnslop = array([1.9, 1.])
      
    init(psfntype='gausking', \
		 numbproc=1, \
		 numbswep=100, \
         makeplot=True, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=2., \
         fdfntype='powr', \
         verbtype=2, \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         maxmnumbpnts=array([3]), \
         #maxmnumbpnts=array([1000]), \
         minmfdfnnorm=array([1e-5]), \
         maxmfdfnnorm=array([1e2]), \
         probprop=array([0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0., 0.], dtype=float), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_ngal.fits', \
         datatype='mock', \
         mockfdfntype='powr', \
         mocknumbpnts=array([2]), \
         #mocknumbpnts=array([500]), \
         numbsideheal=256, \
         mockfdfnslop=mockfdfnslop, \
         mocknormback=ones((2, numbener)), \
        )


def cnfg_test_popl():
     
    indxenerincl = arange(1, 4)
    numbener = indxenerincl.size

    minmflux = 3e-11
    maxmflux = 1e-7
    mockfdfnslop = array([1.9, 1.1])
      
    init(psfntype='gausking', \
		 numbswep=100000, \
         makeplot=True, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=20., \
         fdfntype='powr', \
         #verbtype=2, \
         indxenerincl=indxenerincl, \
         indxevttincl=arange(2, 4), \
         maxmnumbpnts=array([500, 500]), \
         minmfdfnnorm=array([1e-5, 1e-5]), \
         maxmfdfnnorm=array([1e2, 1e2]), \
         minmfdfnslop=array([1., 1.]), \
         maxmfdfnslop=array([3., 3.]), \
         stdvsdfn=array([.5, .5]), \
         meansdfn=array([2., 2.]), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_ngal.fits', \
         datatype='mock', \
         mockfdfntype='powr', \
         mocknumbpnts=array([300, 200]), \
         numbsideheal=256, \
         mockfdfnslop=mockfdfnslop, \
         mocknormback=ones((2, numbener)), \
        )


def cnfg_test_errr():
     
    indxenerincl = arange(1, 4)
    indxevttincl = arange(2, 4)
    numbener = indxenerincl.size

    minmflux = 3e-11
    maxmflux = 1e-7
    mockfdfnslop = array([1.9])
      
    init(psfntype='gausking', \
		 numbswep=77, \
		 numbswepplot=2000, \
         factthin=1, \
         numbburn=0, \
         makeplot=True, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=20., \
         #verbtype=2, \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         probprop=array([0., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0.]), \
         maxmnumbpnts=array([3]), \
         minmfdfnnorm=array([1e-5]), \
         maxmfdfnnorm=array([1e2]), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_ngal.fits', \
         datatype='mock', \
         mocknumbpnts=array([3]), \
         numbsideheal=256, \
         mockfdfnslop=mockfdfnslop, \
         mocknormback=ones((2, numbener)), \
        )


def cnfg_test_brok():
     
    indxenerincl = arange(1, 4)
    indxevttincl = arange(2, 4)
    numbener = indxenerincl.size

    minmflux = 3e-11
    maxmflux = 1e-7
    mockfdfnslop = array([1.9])
    mockfdfnsloplowr = array([1.1])
    mockfdfnslopuppr = array([1.9])
    mockfdfnbrek = array([1e-9])
      
    init(psfntype='gausking', \
		 numbswep=3, \
         factthin=1, \
         randinit=False, \
         trueinfo=True, \
         #makeplot=False, \
         maxmgang=20., \
         fdfntype='brok', \
         verbtype=2, \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         maxmnumbpnts=array([100]), \
         minmfdfnnorm=array([1e-5]), \
         maxmfdfnnorm=array([1e2]), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_ngal.fits', \
         datatype='mock', \
         mockfdfntype='brok', \
         mocknumbpnts=array([100]), \
         numbsideheal=256, \
         mockfdfnslop=mockfdfnslop, \
         mockfdfnsloplowr=mockfdfnsloplowr, \
         mockfdfnslopuppr=mockfdfnslopuppr, \
         mockfdfnbrek=mockfdfnbrek, \
         mocknormback=ones((2, numbener)), \
        )


def cnfg_ferm_mock_ngal():
     
    indxenerincl = arange(1, 4)
    indxevttincl = arange(2, 4)
    numbener = indxenerincl.size

    minmflux = 3e-11
    maxmflux = 1e-7
    mockfdfnslop = array([1.9])
      
    init(psfntype='doubking', \
         numbswep=5000000, \
         randinit=False, \
         trueinfo=True, \
         maxmgang=20., \
         indxenerincl=indxenerincl, \
         indxevttincl=indxevttincl, \
         mocknumbpnts=array([300]), \
         maxmnumbpnts=array([600]), \
         minmflux=minmflux, \
         maxmflux=maxmflux, \
         regitype='ngal', \
         maxmnormback=array([2., 2.]), \
         minmnormback=array([0.5, 0.5]), \
         strgexpo='fermexpo_cmp0_ngal.fits', \
         datatype='mock', \
         numbsideheal=256, \
         mockfdfnslop=mockfdfnslop, \
         mocknormback=ones((2, numbener)), \
        )

    
def cnfg_sdss_mock():

    indxenerincl = arange(3)
    indxevttincl = arange(1)
    numbener = indxenerincl.size
    numbener = indxenerincl.size

    init(psfntype='doubgaus', \
         numbswep=100000, \
         minmflux=array([1e3]), \
         maxmflux=array([1e5]), \
         initnumbpnts=array([100]), \
         exprtype='sdss', \
         pixltype='cart', \
         regitype='mes5', \
         stdvlbhl=2./3600., \
         lgalcntr=202., \
         bgalcntr=2., \
         radispmrlbhl=5./3600., \
         maxmnormback=array([1e3]), \
         minmnormback=array([1e2]), \
         maxmgang=30./3600., \
         margsize=2./3600., \
         strgback=['unit'], \
         strgexpo='unit', \
         indxevttincl=indxevttincl, \
         indxenerincl=indxenerincl, \
         datatype='mock', \
         numbsidecart=100, \
         mockfdfnslop=array([1.9]), \
         mocknormback=ones((1, numbener)), \
        )
    
    
def cnfg_sdss_expr():

    init(psfntype='doubgaus', \
         trueinfo=False, \
         numbswep=1000000, \
         minmflux=ones(3) * 1e3, \
         maxmflux=ones(3) * 1e5, \
         initnumbpnts=array([10]), \
         exprtype='sdss', \
         datatype='inpt', \
         pixltype='cart', \
         regitype='mes5', \
         stdvlbhl=2./3600., \
         lgalcntr=202., \
         bgalcntr=2., \
         radispmrlbhl=0.5/3600., \
         stdvflux=0.05, \
         maxmnormback=array([1e3]), \
         minmnormback=array([1e2]), \
         margsize=2./3600., \
         maxmgang=30./3600., \
         strgexpr='sdssflux.fits', \
         strgexpo='sdssexpo.fits', \
         stdvback=1e-4, \
         indxevttincl=arange(1), \
         indxenerincl=arange(1), \
        )
    
    
if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        name = globals().copy()
        name.update(locals())
        numbargs = len(sys.argv) - 2
        if numbargs == 0:
            print 'Running PCAT configuration %s...' % sys.argv[1]
            name.get(sys.argv[1])()
        else:
            listargs = []
            for k in range(numbargs):
                listargs.append(sys.argv[k+2])
            print 'listargs'
            print listargs

            name.get(sys.argv[1])(listargs)
    else:

        pass
        #cnfg_ferm_info()
        
        #cnfg_ferm_psfn_mock('gausking')
        #cnfg_ferm_psfn_mock('doubking')
    
        #cnfg_ferm_psfn_expr('gausking')
        #cnfg_ferm_psfn_expr('doubking')
        
        #cnfg_ferm_expr_igal('fermflux_igal_cmp0_time0.fits', 'fermexpo_igal_cmp0_time0.fits')
        #cnfg_ferm_mock_igal()
        
        cnfg_ferm_expr_ngal('fermflux_cmp0_ngal.fits', 'fermexpo_cmp0_ngal.fits')
        #cnfg_ferm_expr_ngal('fermflux_cmp1_ngal.fits', 'fermexpo_cmp1_ngal.fits')
        #cnfg_ferm_expr_ngal('fermflux_cmp2_ngal.fits', 'fermexpo_cmp2_ngal.fits')
        #cnfg_ferm_expr_ngal('fermflux_cmp3_ngal.fits', 'fermexpo_cmp3_ngal.fits')
        
        #cnfg_ferm_post()
        #cnfg_ferm_mock_ngal()
        #cnfg_test()
        
        #cnfg_sdss_mock()
        #cnfg_sdss_expr()

