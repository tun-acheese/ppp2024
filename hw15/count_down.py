import time
def main():
    # x = int(input())
    count = 5

    while True:
        # print(f"카운트 다운...{count}", end="/r")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print("Bomb")