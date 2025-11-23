import random
import time

class MovieGame:
    def __init__(self):
        self.var1 = []
        self.var2 = "*"
        self.var3 = 0
        self.var4 = 0
        self.var5 = 0
        self.var6 = 0
        self.var7 = 0
        self.var8 = ""
        self.var9 = 1.0

    def clear_screen(self):
        print("\n" * 19)

    def print_banner(self):
        print("=" * 47)
        print("||                                           ||")
        print("||       MOVIE GUESS THINGY (??)             ||")
        print("||                                           ||")
        print("=" * 47)

    def get_difficulty_setting(self):
        print("\nDifficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")

        dd = ""
        while dd == "":
            inp = input("Pick difficulty: ").strip()
            if inp == "1":
                self.var8 = "EASY"
                self.var9 = 1.0
                dd = 0.1
            elif inp == "2":
                self.var8 = "MEDIUM"
                self.var9 = 1.5
                dd = 0.3
            elif inp == "3":
                self.var8 = "HARD"
                self.var9 = 2.0
                dd = 0.5
            else:
                print("?? try again")
        return dd

    def setup_game(self):
        self.print_banner()
        time.sleep(0.4)

        ok = False
        while not ok:
            t = input("\nMovies separated by commas: ")
            lst = [x.strip() for x in t.split(",") if x.strip()]
            if len(lst) > 0:
                self.var1 = lst
                ok = True
            else:
                print("enter something dude")

        ph = input("placeholder (default '*'): ").strip()
        if len(ph) > 0:
            self.var2 = ph[0]
        else:
            self.var2 = "*"

        time.sleep(0.7)

    def obfuscate_title(self, varA, varB):
        a = list(varA)
        idxs = []
        for ii, cc in enumerate(a):
            if cc.isalpha():
                idxs.append(ii)
        if not idxs:
            return varA

        maybe = int(len(idxs) * varB)
        if maybe < 1:
            maybe = 1
        pick = random.sample(idxs, maybe)
        for p in pick:
            a[p] = self.var2
        return "".join(a)

    def reveal_hint(self, xx, yy):
        aa = list(xx)
        bb = list(yy)
        hidden = []
        for i2, c2 in enumerate(aa):
            if c2 == self.var2:
                hidden.append(i2)
        if not hidden:
            return xx
        pos = random.choice(hidden)
        aa[pos] = bb[pos]
        return "".join(aa)

    def show_stats(self):
        print("\n--------------")
        print(" FINISHED ")
        print("--------------")
        print("SCORE:", int(self.var3))
        print("ROUNDS:", self.var4)
        print("CORRECT:", f"{self.var5}/{self.var4}")
        print("BEST:", self.var7)
        print("--------------")

    def play_round(self, hide):
        self.var4 += 1
        tmp_x = random.choice(self.var1)
        weirdString = self.obfuscate_title(tmp_x, hide)
        tries = 0
        maxTry = 3

        print(f"\n>>> ROUND {self.var4} <<<")
        time.sleep(0.2)

        flag = True
        while flag:
            print("\nMovie:", weirdString)
            print("tries left:", maxTry - tries)
            print("HINT or QUIT")

            user = input("guess: ").strip()

            if user.upper() == "QUIT":
                return False

            if user.upper() == "HINT":
                if self.var3 >= 5:
                    self.var3 -= 5
                    weirdString = self.reveal_hint(weirdString, tmp_x)
                    print("hint ok")
                else:
                    print("no points")
                continue

            if user.lower() == tmp_x.lower():
                b1 = 100
                b2 = (maxTry - tries) * 20
                total = (b1 + b2) * self.var9

                self.var3 += total
                self.var5 += 1
                self.var6 += 1

                if self.var6 > self.var7:
                    self.var7 = self.var6

                print("\nYes:", tmp_x)
                print("Earned:", int(total))
                print("streak:", self.var6)
                flag = False

            else:
                tries += 1
                self.var6 = 0
                print("wrong")
                if tries >= maxTry:
                    print("\nno tries left")
                    print("movie was:", tmp_x)
                    flag = False

        return True

    def start(self):
        self.setup_game()
        h = self.get_difficulty_setting()

        go = True
        while go:
            res = self.play_round(h)
            if not res:
                break

            ans = ""
            while ans not in ("y","n"):
                ans = input("\nagain? (y/n): ").lower().strip()
                if ans == "n":
                    go = False
                elif ans == "y":
                    pass
                else:
                    print("y or n ??")

        self.show_stats()
        print("\nok done\n")

if __name__ == "__main__":
    game = MovieGame()
    game.start()
