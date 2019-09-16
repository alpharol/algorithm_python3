select Email
from leetcode_0182
group by Email
having count(Email)>=2;
