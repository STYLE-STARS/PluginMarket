from tooldelta import plugins, Plugin, Utils, Print

@plugins.add_plugin
class LargeFill(Plugin):
    name = "大范围填充"
    author = "System"
    version = (0, 0, 1)

    def on_def(self):
        self.gx: float | None = None
        self.gy: float | None = None
        self.gz: float | None = None
        self.ex: float | None = None
        self.ey: float | None = None
        self.ez: float | None = None
        self.frame.add_console_cmd_trigger(
            ["lfset"], "[x] [y] [z]", "设置大范围填充起点", self.on_setpos_start
        )
        self.frame.add_console_cmd_trigger(
            ["lfsend"], "[x] [y] [z]", "设置大范围填充起点", self.on_setpos_end
        )
        self.frame.add_console_cmd_trigger(
            ["lfill"], None, "设置大范围填充起点", self.on_fill
        )
        # lfset 400 -60 400
        # lfsend 500 -40 500
        # lfill diamond_ore

    def on_setpos_start(self, args: list[str]):
        try:
            x, y, z = (int(i) for i in args)
        except Exception:
            Print.print_err("菜单参数错误")
            return
        self.gx = x
        self.gy = y
        self.gz = z
        Print.print_suc(f"起点坐标设置为: {self.gx}, {self.gy}, {self.gz}")

    def on_setpos_end(self, args: list[str]):
        try:
            x, y, z = (int(i) for i in args)
        except Exception:
            Print.print_err("菜单参数错误")
            return
        self.ex = x
        self.ey = y
        self.ez = z
        Print.print_suc(f"终点坐标设置为: {self.ex}, {self.ey}, {self.ez}")

    def on_fill(self, args: list[str]):
        if len(args) != 1:
            Print.print_err("参数错误")
            return
        self.thread_fill(args[0])

    @Utils.thread_func("大范围填充")
    def thread_fill(self, fillblock_id: str):
        pos_start = self.getpos_start()
        if pos_start is None:
            Print.print_err("还未设置起点, 使用 lfset 设置")
            return
        _sx, _sy, _sz = pos_start
        pos_end = self.getpos_end()
        if pos_end is None:
            Print.print_err("还未设置终点, 使用 lfsend 设置")
            return
        _ex, _ey, _ez = pos_end
        sx, ex = self.cmp(_sx, _ex)
        sy, ey = self.cmp(_sy, _ey)
        sz, ez = self.cmp(_sz, _ez)
        nowx = sx
        nowy = sy
        nowz = sz
        while nowz < ez:
            while nowx < ex:
                while nowy < ey:
                    Print.print_inf(f"大范围填充: 正在填充 {nowx}, {nowy}, {nowz} 区域     ", need_log=False, end="\r")
                    self.game_ctrl.sendcmd_with_resp(f"tp @a[name={self.game_ctrl.bot_name}] {nowx} {nowy} {nowz}")
                    self.game_ctrl.sendcmd_with_resp(f"fill {nowx} {nowy} {nowz} {min(nowx + 31, ex)} {min(nowy + 31, ey)} {min(nowz + 31, ez)} {fillblock_id}")
                    Print.print_inf(f"大范围填充: 已填充 {nowx}, {nowy}, {nowz} 区域     ", need_log=False, end="\r")
                    nowy += 32
                nowy = sy
                nowx += 32
            nowx = sx
            nowz += 32
        Print.print_suc(f"大范围填充已完成: ({sx}, {sy}, {sz}) -> ({ex}, {ey}, {ez})")

    def getpos_start(self):
        if self.gx is None or self.gy is None or self.gz is None:
            return None
        return int(self.gx), int(self.gy), int(self.gz)

    def getpos_end(self):
        if self.ex is None or self.ey is None or self.ez is None:
            return None
        return int(self.ex), int(self.ey), int(self.ez)

    @staticmethod
    def cmp(a: int, b: int):
        return (a, b) if a < b else (b, a)
