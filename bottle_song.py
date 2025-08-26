#!/usr/bin/env python3


def recite(start, take=1):
    verse = []
    NUMS = {0 : 'no', 1: 'One', 2 : 'Two', 3: 'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9: 'Nine', 10: 'Ten'}
    fin = {False: '', True: 's' }
    for ind in range(take):
        num = start - ind
        verse.append(f"{NUMS[num]} green bottle{fin[num != 1]} hanging on the wall,")
        verse.append(f"{NUMS[num]} green bottle{fin[num != 1]} hanging on the wall,")
        verse.append("And if one green bottle should accidentally fall,")
        verse.append(f"There'll be {NUMS[num - 1].lower()} green bottle{fin[(num - 1)!= 1]} hanging on the wall.")
        if ind != take -1:
            verse.append("")
    return verse