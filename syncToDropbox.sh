#!/bin/bash

# working directory
WDIR=/media/sf_Shared/Documents/Projects/HeywoodEngineering_BridgeMonitoring_2020/HES_toolbox/

# directory to backup
BDIR=/home/$USER/Dropbox/HES_RemoteMonitoring/Internal/reportDrafts/.

rsync -avz $WDIR/*draft.pdf $BDIR


