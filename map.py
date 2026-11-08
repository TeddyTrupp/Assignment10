class GameMap:
    def __init__(self, map_name):
        self.map_name = map_name
        if map_name == 'town':
            self.grid = [
                ['#', '#', '#', '#', '#'],
                ['#', 'P', '.', 'N', '#'],
                ['#', '.', '#', '.', '#'],
                ['#', 'S', '.', 'E', '#'],
                ['#', '#', '#', '#', '#']
            ]
        else:
            self.grid = [
                ['#', '#', '#', '#', '#', '#'],
                ['#', 'P', '.', 'M', '.', '#'],
                ['#', '#', '#', '#', '.', '#'],
                ['#', 'M', '.', '.', 'B', '#'],
                ['#', '#', '#', '#', '#', '#']
            ]

    def display(self):
        print(f"\n--- MAP: {self.map_name.upper()} ---")
        for row in self.grid:
            print(" ".join(row))
