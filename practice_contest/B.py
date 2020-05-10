# Contest No.: practice
# Problem No.: B
# Solver:      JEMINI
# Date:        20200509

import sys

def mergeSort(nums: str) -> str:
    if len(nums) < 2:
        return nums
    left = mergeSort(nums[:len(nums) // 2])
    right = mergeSort(nums[len(nums) // 2:])
    pLeft = 0
    pRight = 0
    ans = ""
    while pLeft < len(left) and pRight < len(right):
        print("?", left[pLeft], right[pRight])
        temp = input()
        if temp == "<":
            ans += left[pLeft]
            pLeft += 1
        else:
            ans += right[pRight]
            pRight += 1
    if pLeft == len(left):
        ans += right[pRight:]
    if pRight == len(right):
        ans += left[pLeft:]
    return ans

def main():
    n, q = map(int, input().split())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = None
    if n == 26:
        ans = mergeSort(alphabet)
        print("!", ans)
    else:
        def query(p: int, q: int) -> bool:
            print("?", alphabet[nums[p]], alphabet[nums[q]])
            temp = input()
            if temp == ">":
                return True
            else:
                return False

        nums = [0, 1, 2, 3, 4]
        if query(0, 1):
            nums[0], nums[1] = nums[1], nums[0]
        if query(2, 3):
            nums[2], nums[3] = nums[3], nums[2]
        if query(0, 2):
            nums[0], nums[2] = nums[2], nums[0]
            nums[1], nums[3] = nums[3], nums[1]
        # ACD
        if query(2, 4):
            if query(0, 4): # EACD
                if query(1, 2):
                    if query(1, 3):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[4], nums[0], nums[2], nums[3], nums[1]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[4], nums[0], nums[2], nums[1], nums[3]
                else:
                    nums[0], nums[1], nums[2], nums[3], nums[4] = nums[4], nums[0], nums[1], nums[2], nums[3]
            else:   # AECD
                if query(1, 2): # AEC(BD)
                    if query(1, 3):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[4], nums[2], nums[3], nums[1]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[4], nums[2], nums[1], nums[3]
                else:
                    if query(1, 4):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[4], nums[1], nums[2], nums[3]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[1], nums[4], nums[2], nums[3]
        else:
            if query(3, 4): # ACED
                if query(1, 4):
                    if query(1, 3):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[4], nums[3], nums[1]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[4], nums[1], nums[3]
                else:
                    if query(1, 2):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[1], nums[4], nums[3]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[1], nums[2], nums[4], nums[3]
            else:   # ACDE
                if query(1, 3):
                    if query(1, 4):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[3], nums[4], nums[1]
                    else:
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[3], nums[1], nums[4]
                else:
                    if query(1, 2):
                        nums[0], nums[1], nums[2], nums[3], nums[4] = nums[0], nums[2], nums[1], nums[3], nums[4]
                    else:
                        pass
        ans = "! "
        for i in nums:
            ans += alphabet[i]
        print(ans)

    return

if __name__ == "__main__":
    main()