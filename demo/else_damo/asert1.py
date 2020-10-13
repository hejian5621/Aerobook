
from assertpy import assert_that

expect3_result="   铺层数据   库制作已完成!  "
actual_result="铺层数据库制作已完成!"



print("处理前：",expect3_result)

expect3_result4=expect3_result.strip()

print("处理后",expect3_result4)

# assert_that(expect3_result).is_equal_to(actual_result)