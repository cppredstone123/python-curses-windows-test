import curses
from curses import wrapper

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def scroll(y, x, text, scrollRate = 40):
    for i in range(0, len(text)):
        stdscr.addstr(y, x + i, text[i])
        stdscr.refresh()
        curses.napms(int(1000 / scrollRate))

def main(stdscr):
    maxY, maxX = stdscr.getmaxyx()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "Greetings! (Press any key to continue...)")
    stdscr.getkey()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "Thank you very much for volunteering your time to run this test.")
    stdscr.getkey()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "Part 1/3: Formatting")
    stdscr.addstr(1, 0, "This text should be flashing.", curses.A_BLINK)
    stdscr.addstr(2, 0, "This text should be bold.", curses.A_BOLD)
    stdscr.addstr(3, 0, "This text should be at half brightness", curses.A_DIM)
    stdscr.addstr(4, 0, "This text should be highlighted.", curses.A_STANDOUT)
    stdscr.addstr(5, 0, "This text should be underlined.", curses.A_UNDERLINE)
    stdscr.addstr(6, 0, "No idea what this one does, but it does something, apparently.", curses.A_REVERSE)
    stdscr.getch()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "Part 2/3: Standard Colors")
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        stdscr.addstr(2, 0, "If you see this, it means that NCurses can use color. Yay!", curses.color_pair(1)) #TODO Add color here
        stdscr.refresh()
    else:
        stdscr.addstr(2, 0, "If you see this, it means NCurses can't use color. Boo.")
    stdscr.getkey()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "Part 3/3: Dynamic Colors")
    if curses.can_change_color():
        scroll(1, 0, "If you are reading this, it means that by some miracle, your terminal supports custom colors. Huzzah!")
    else:
        scroll(1, 0, "If you are reading this, it means that your terminal does not support custom colors. No biggie.")
    stdscr.getch()
    
    stdscr.clear()
    stdscr.refresh()
    scroll(0, 0, "This concludes the NCurses compatability test. Thank you very much for your time.")
    stdscr.getch()
    
    stdscr.clear()
    stdscr.refresh()
    
    

wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
