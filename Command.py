import CHaser
import MakeMap


class Command:
    """
    各種行動を起こします。
    """
    run = CHaser.Client()
    ready_OK = False
    mapCont = MakeMap.MakeMap()

    def __init__(self):
        global run
        global mapCont
        """Set instance"""

    def move(self, com, dir):
        """
        各種行動を起こします。
        Get_info忘れないで！
        """
        global run
        global ready_OK

        result = [0 for _ in range(9)]

        if not ready_OK:  # if didn't get_ready()
            self.get_ready()
            print("Warning!:You didn't get_ready().")

        if com == "put":
            if dir == 1:
                result = run.put_up()
            if dir == 7:
                result = run.put_down()
            if dir == 3:
                result = run.put_left()
            if dir == 5:
                result = run.put_right()

        if com == "walk":
            if dir == 1:
                result = run.walk_up()
                mapCont.mapY -= 1
            if dir == 7:
                result = run.walk_down()
                mapCont.mapY += 1
            if dir == 3:
                result = run.walk_left()
                mapCont.mapX -= 1
            if dir == 5:
                result = run.walk_right()
                mapCont.mapX += 1

        if com == "look":
            if dir == 1:
                result = run.look_up()
            if dir == 7:
                result = run.look_down()
            if dir == 3:
                result = run.look_left()
            if dir == 5:
                result = run.look_right()

        if com == "search":
            if dir == 1:
                result = run.search_up()
            if dir == 7:
                result = run.search_down()
            if dir == 3:
                result = run.search_left()
            if dir == 5:
                result = run.search_right()

        print(com + " " + str(dir))
        ready_OK = False

        return result

    @staticmethod
    def get_ready():
        """Lunch get_ready and return map."""
        global run
        global ready_OK

        ready_OK = True
        result = run.get_ready()
        mapCont.updata("G", 0, result)
        for ls in mapCont.map:
            print(ls)
        return result

    @staticmethod
    def get_map():
        """MAPはこちらからどうぞ"""
        return mapCont.map
