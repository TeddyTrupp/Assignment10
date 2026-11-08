class QuestManager:
    def __init__(self, player):
        self.player = player

    def check_quests(self):
        print("\n--- QUEST LOG ---")
        main_step = self.player.quest_progress.get('main_quest', 0)
        print(f"Main Quest Step: {main_step}/3 (Defeat the Final Boss to win)")
        sq1 = 'Completed' if self.player.quest_progress.get('side_quest_1') else 'Active'
        sq2 = 'Completed' if self.player.quest_progress.get('side_quest_2') else 'Active'
        print(f"Side Quest 1 (Clear Goblins): {sq1}")
        print(f"Side Quest 2 (Gather Herbs): {sq2}")
