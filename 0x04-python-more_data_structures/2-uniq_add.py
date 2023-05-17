#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return 0
    else:
        new_list = []
        ans = 0

        for num in my_list:
            comp = 0

            for x in new_list:
                if num == x:
                    comp = 1
                else:
                    pass
            if comp == 1:
                pass
            else:
                new_list.append(num)
                ans += num

        return ans
