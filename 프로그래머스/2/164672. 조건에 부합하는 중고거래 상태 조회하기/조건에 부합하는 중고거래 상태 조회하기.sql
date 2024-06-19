-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, decode(STATUS, 'SALE', '판매중', 'RESERVED', '예약중', 'DONE', '거래완료') as status
from USED_GOODS_BOARD 
where to_char(CREATED_DATE, 'yyyy-mm-dd') = '2022-10-05'
order by board_id desc