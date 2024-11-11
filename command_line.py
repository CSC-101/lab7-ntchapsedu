import sys
import keyboard

def comm_input()->list or None:
    nums = sys.argv
    nums.pop(0)
    count = 0
    for i in nums:
        try:
            count += float(i)
        except ValueError:
            break
    print(count)
if __name__ == '__main__':
    print(sys.argv)
    comm_input()

