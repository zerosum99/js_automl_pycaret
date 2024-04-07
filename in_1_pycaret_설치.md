# 가상환경 설치하기 


## 1. 아나콘다 가상환경 만들기 

conda create -n pycaret python=3.9 anaconda

## 1-1 아나콘다 가상환경 리스트 확인

conda env list

## 2. 가상환경 이동 
conda activate pycaret 


## 3. 가상환경에서 모듈 설치

pip install ipykernel
pip install jupyter

## 4.  install pycaret
pip install pycaret

## 4-1.  mac m1 install pycaret 설치 
conda install -c conda-forge pycaret

## 5. create notebook kernel connected with the conda environment
python -m ipykernel install --user --name yourenvname --display-name "display-name"

## 6. 알고리즘 모듈 추가 설치 

pip install lightgbm
pip install catboost
pip install xgboost

