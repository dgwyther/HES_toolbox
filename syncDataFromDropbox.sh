#!/bin/bash

# todays date
date_today=$(date '+%Y%m%d')

# working directory
WDIR=/media/sf_Shared/Documents/Projects/HeywoodEngineering_BridgeMonitoring_2020/SampleData/

# from-directory to collect
FROMDIR=/home/$USER/Dropbox/HES_RemoteMonitoring/Sites/

# CCB Northbound
cp -p $WDIR/HE604_RV50_CCB_NB_SensorStats.dat $WDIR/HE604_RV50_CCB_NB_SensorStats.$date_today.dat
rsync -avz $FROMDIR/2020_CCB_NB_VW/Data/HE604_RV50_CCB_NB_SensorStats.dat $WDIR/HE604_RV50_CCB_NB_SensorStats.dat

# CCB Southbound
cp -p $WDIR/HE602_3680_RV50_CCB_SB_SensorStats.dat $WDIR/HE602_3680_RV50_CCB_SB_SensorStats.$date_today.dat
rsync -avz $FROMDIR/2020_CCB_SB/Data/HE602_3680_RV50_CCB_SB_SensorStats.dat $WDIR/HE602_3680_RV50_CCB_SB_SensorStats.dat



