from pyautogui import press, keyUp, keyDown
from time import sleep
from sys import exit


amount = input('Amount: ')
timer = input('Time needed before going into discord (sec): ')

def main(amount, timer):
    sleep(float(timer))
    for i in range(1, int(amount)+1):
        press('up')
        press('up')
        keyDown('ctrl')
        keyDown('a')
        keyUp('ctrl')
        keyUp('a')
        press('backspace')
        press('enter')
        press('enter')
        print(f'Deleted Message #{i}')
        sleep(0.25)
    print(f'Successfully deleted {amount} messages!')


if __name__ == '__main__':
    try:
        int(amount)
        float(timer)
    except:
        print('Amount must be an integer!')
        print('Time needed must be a float!')
        exit()
    main(amount, timer)
