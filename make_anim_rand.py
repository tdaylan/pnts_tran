from __init__ import *
from util import *

rtag = sys.argv[1]
strgplot = sys.argv[2]
if len(sys.argv) == 3:
    indxframloww = 0
else:
    indxframloww = int(numbfram * float(sys.argv[3]))
pathimag = os.environ["PCAT_DATA_PATH"] + '/imag/%s/post/fram/' % rtag
listpathfram = array(fnmatch.filter(os.listdir(pathimag), '*%s*.pdf' % strgplot))
cmnd = 'convert -density 200x200 '
numbfram = len(listpathfram)
indxfram = arange(indxframloww, numbfram)
indxframrand = choice(indxfram, size=numbfram, replace=False).astype(int)
for pathfram in listpathfram[indxframrand]:
    cmnd += '%s/%s ' % (pathimag, pathfram)
    print '%s/%s ' % (pathimag, pathfram)
cmnd += '%s/%s.gif' % (pathimag, strgplot)
os.system(cmnd)

