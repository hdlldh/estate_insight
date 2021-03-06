WORK_DIR=$HOME/Workspace/estate_insight
cd $WORK_DIR
mkdir -p $WORK_DIR"/data"
mkdir -p $WORK_DIR"/logs"
DATA_FILE=$WORK_DIR"/data/data_$(date +"%Y-%m-%d").csv"
rm -f $DATA_FILE
LOG_FILE=$WORK_DIR"/logs/info_$(date +"%Y-%m-%d").log"
rm -f $LOG_FILE
scrapy crawl redfin_estate \
	--output=$DATA_FILE \
	--loglevel=INFO \
	--logfile=$LOG_FILE

