cd ../..
cd code/gh_server/app/src/piccolo_db
sleep 1
piccolo --diagnose
piccolo migrations forwards gh
cd ../..