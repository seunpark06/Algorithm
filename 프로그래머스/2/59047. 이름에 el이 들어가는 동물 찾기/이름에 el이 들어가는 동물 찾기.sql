-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
from ANIMAL_INS 
where name like '%el%'
and animal_type = 'Dog'
order by name