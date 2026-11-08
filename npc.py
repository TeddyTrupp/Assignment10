NPCS = {
    "Elder": "Welcome traveler! Defeat the Dark Overlord to save our village.",
    "Merchant": "Care to buy some potions or better gear?",
    "Guard": "Watch out for monsters wandering near the forest boundary.",
    "Hermit": "I know secret spells, but you must prove your worth.",
    "Innkeeper": "Rest here to restore your strength, adventurer."
}

def talk_to_npc(npc_name):
    dialogue = NPCS.get(npc_name, "Hello there.")
    print(f"\n{npc_name} says: \"{dialogue}\"")
