-- 코드를 작성해주세요
select count(*) as fish_count, fni.fish_name
from FISH_INFO fi join FISH_NAME_INFO fni
on fi.fish_type = fni.fish_type
group by fish_name
order by 1 desc

