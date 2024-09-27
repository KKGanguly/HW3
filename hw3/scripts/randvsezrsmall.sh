mkdir -p output/randvsezr/less_than_6
rm -f output/randvsezr/less_than_6/*
python3 hw3.py -t data/less_than_6/SS-B.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-B.csv & 
python3 hw3.py -t data/less_than_6/wc+wc-3d-c4-obj1.csv -e randvsezr  | tee output/randvsezr/less_than_6/wc+wc-3d-c4-obj1.csv & 
python3 hw3.py -t data/less_than_6/wc+sol-3d-c4-obj1.csv -e randvsezr  | tee output/randvsezr/less_than_6/wc+sol-3d-c4-obj1.csv & 
python3 hw3.py -t data/less_than_6/SS-D.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-D.csv & 
python3 hw3.py -t data/less_than_6/SS-F.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-F.csv & 
python3 hw3.py -t data/less_than_6/SS-E.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-E.csv & 
python3 hw3.py -t data/less_than_6/wc+rs-3d-c4-obj1.csv -e randvsezr  | tee output/randvsezr/less_than_6/wc+rs-3d-c4-obj1.csv & 
python3 hw3.py -t data/less_than_6/SS-A.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-A.csv & 
python3 hw3.py -t data/less_than_6/SS-C.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-C.csv & 
python3 hw3.py -t data/less_than_6/SS-G.csv -e randvsezr  | tee output/randvsezr/less_than_6/SS-G.csv & 
