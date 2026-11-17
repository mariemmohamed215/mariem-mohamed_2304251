@echo off
echo Loading Problem 1 (company) database...
mysql -u root -pRootAlaaSql2028 < problem1_DDL.sql
mysql -u root -pRootAlaaSql2028 < problem1_DML.sql

echo Loading Problem 2 (library 6-table) database...
mysql -u root -pRootAlaaSql2028 < problem2_DDL.sql
mysql -u root -pRootAlaaSql2028 < problem2_DML.sql

echo Starting Flask Website on http://127.0.0.1:5000 ...
cd website
pip install -r requirements.txt
python app.py