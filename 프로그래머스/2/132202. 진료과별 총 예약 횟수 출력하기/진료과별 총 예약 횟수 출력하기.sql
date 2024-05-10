-- 코드를 입력하세요
-- SELECT  *
select MCDP_CD AS 진료과코드, count(*) AS 5월예약건수
FROM APPOINTMENT
where APNT_YMD between '2022-05-01' and '2022-06-01'
 -- 예약취소가 안된거
GROUP BY MCDP_CD
order by count(*),MCDP_CD