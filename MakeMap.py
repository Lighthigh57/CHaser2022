class MakeMap:
    """
    Map生成します。
    self.Mapという名前のリストを使ってる。
    """

    """座標"""

    def __init__(self) -> None:

        self.map = [[9 for _ in range(20)] for _ in range(20)]
        """保存したマップ"""

        self.mapX = 0
        """今のX座標（仮定）"""

        self.mapY = 0
        """今のY座標（仮定）"""

    def updata(self, com, dir, get):

        print("UpdateData実行")

        if str(com) == "G":
            print("GetReadyのデータで更新")
            if self.mapX - 1 < 0:
                print("Xのデータを修正")
                for y in range(20):
                    for i in range(-1 * self.mapX + 1):
                        self.map[y].insert(0, 9)

                for y in range(20):
                    for i in range(-1 * self.mapX + 1):
                        del self.map[y][18]
                self.mapX = -1 * self.mapX + 1

            if self.mapY - 1 < 0:
                print("Yのデータを修正")
                for i in range(-1 * self.mapY + 1):
                    self.map.insert(0, [9 for _ in range(20)])

                for i in range(-1 * self.mapY + 1):
                    del self.map[20]
                self.mapY = -1 * self.mapY + 1

            print("get_ready()で更新中...")
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.map[self.mapY + i][self.mapX + j] = get[i * 3 + j]

        elif str(com) == "S":
            print("Searchのデータで更新")
            if dir == "U":
                if self.mapY - 9 < 0:
                    print("Yのデータを修正")
                    for i in range(-1 * self.mapY + 9):
                        self.map.insert(0, [9 for _ in range(20)])

                    for i in range(-1 * self.mapY + 9):
                        del self.map[20]
                    self.mapY = -1 * self.mapY + 9

                print("Searchの上の情報で更新中...")
                for i in range(9):
                    self.map[self.mapY - 1 - i][self.mapX] = get[i]

            if dir == "D":
                print("Searchの下の情報で更新中...")
                for i in range(9):
                    self.map[self.mapY + 1 + i][self.mapX] = get[i]

            if dir == "L":
                if self.mapX - 9 < 0:
                    print("Xのデータを修正")
                    for y in range(20):
                        for j in range(-1 * self.mapX + 9):
                            self.map[y].insert(0, 9)

                    for y in range(20):
                        for j in range(-1 * self.mapX + 9):
                            del self.map[y][18]
                    self.mapX = -1 * self.mapX + 9

                print("Searchの左の情報で更新中...")
                x = self.mapX - 1
                y = self.mapY
                for i in range(9):
                    self.map[y][x] = get[i]
                    x -= 1

            if dir == "R":
                print("Searchの右の情報で更新中...")
                for i in range(9):
                    self.map[self.mapY][self.mapX + 1 + i] = get[i]

        elif str(com) == "L":
            print("Lookのデータで更新")
            if dir == "U":
                if self.mapX - 3 > 0:
                    print("Xのデータを修正")
                    for y in range(20):
                        for i in range(-1 * self.mapX + 3):
                            self.map[y].insert(0, 9)

                    for y in range(20):
                        for i in range(-1 * self.mapX + 3):
                            del self.map[y][18]
                    self.mapX = -1 * self.mapX + 3

                if self.mapY - 1 > 0:
                    for i in range(-1 * self.mapY + 1):
                        self.map.insert(0, [9 for _ in range(20)])

                    for i in range(-1 * self.mapY + 1):
                        del self.map[20]
                    self.mapY = -1 * self.mapY + 1

                print("Lookの上のデータで更新中...")
                y = self.mapY - 3
                for i in range(3):
                    x = self.mapX - 1
                    for j in range(3):
                        self.map[y][x] = get[i * j]
                        x += 1
                    y += 1

            if dir == "D":
                print("Lookの下のデータで更新中...")
                y = self.mapY + 3
                for i in range(3):
                    x = self.mapX - 1
                    for j in range(3):
                        self.map[y][x] = get[i * j]
                        x += 1
                    y += 1

            if dir == "L":
                if self.mapX - 3 > 0:
                    print("Xのデータを修正")
                    for y in range(20):
                        for i in range(-1 * self.mapX + 3):
                            self.map[y].insert(0, 9)

                    for y in range(20):
                        for i in range(-1 * self.mapX + 3):
                            del self.map[y][18]

                    self.mapX = -1 * self.mapX + 3

                if self.mapY - 1 > 0:
                    for i in range(-1 * self.mapY + 1):
                        self.map.insert(0, [9 for _ in range(20)])

                    for i in range(-1 * self.mapY + 1):
                        del self.map[20]
                    self.mapY = -1 * self.mapY + 1

                print("Lookの左のデータで更新中...")
                y = self.mapY - 1
                for i in range(3):
                    x = self.mapX - 3
                    for j in range(3):
                        self.map[y][x] = get[i * j]
                        x += 1
                    y += 1

            if dir == "R":
                print("Lookの右のデータで更新中...")
                x = self.mapX + 3
                y = self.mapY - 1
                for i in range(3):
                    for j in range(3):
                        self.map[y][x] = get[i * j]
                        x += 1
                    x = self.mapX - 3
                    y += 1
        print(self.mapX, self.mapY)
        print("更新完了")
