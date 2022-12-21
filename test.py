# Function to level up the character and add points to their stats and skills
def level_up(stat, skill):
  global strength, dexterity, vigor, intelligence, wisdom, mana, charisma
  global health, magic
  global acrobatics, animal_handling, arcana, archery, athletics, crafting
  global deception, enchantment, faith, insight, intimidation, investigation
  global medicine, nature, perception, performance, persuasion, sleight_of_hand
  global stealth, survival

  # Add 5 points to the chosen stat
  if stat == "strength":
    strength += 5
  elif stat == "dexterity":
    dexterity += 5
  elif stat == "vigor":
    vigor += 5
  elif stat == "intelligence":
    intelligence += 5
  elif stat == "wisdom":
    wisdom += 5
  elif stat == "mana":
    mana += 5
  elif stat == "charisma":
    charisma += 5

  # Add 10 points to the chosen skill
  if skill == "acrobatics":
    acrobatics += 10
  elif skill == "animal_handling":
    animal_handling += 10
  elif skill == "arcana":
    arcana += 10
  elif skill == "archery":
    archery += 10
  elif skill == "athletics":
    athletics += 10
  elif skill == "crafting":
    crafting += 10
  elif skill == "deception":
    deception += 10
  elif skill == "enchantment":
    enchantment += 10
  elif skill == "faith":
    faith += 10
  elif skill == "insight":
    insight += 10
  elif skill == "intimidation":
    intimidation += 10
  elif skill == "investigation":
    investigation += 10
  elif skill == "medicine":
    medicine += 10
  elif skill == "nature":
    nature += 10
  elif skill == "perception":
    perception += 10
  elif skill == "performance":
    performance += 10
  elif skill == "persuasion":
    persuasion += 10
  elif skill == "sleight_of_hand":
    sleight_of_hand += 10
  elif skill == "stealth":
    stealth += 10
  elif skill == "survival":
    survival += 10

# Level up the character's strength and persuasion skill twice
level_up("strength", "persuasion")
level_up("strength", "persuasion")

# Print out the character's stats
print("Attributes:")
print("Strength:", strength)
print("Dexterity:", dexterity)
print("Vigor:", vigor)
print("Intelligence:", intelligence)
print("Wisdom:", wisdom)
print("Mana:", mana)
print("Charisma:", charisma)

print("Stats:")
print("Health:", health)
print("Magic:", magic)

print("Skills:")
print("Acrobatics:", acrobatics)
print("Animal Handling:", animal_handling)
print("Arcana:", arcana)
print("Archery:", archery)
print("Athletics:", athletics)
print("Crafting:", crafting)
print("Deception:", deception)
print("Enchantment:", enchantment)
print("Faith:", faith)
print("Insight:", insight)
print("Intimidation:", intimidation)
print("Investigation:", investigation)
print("Medicine:", medicine)
print("Nature:", nature)
print("Perception:", perception)
print("Performance:", performance)
print("Persuasion:", persuasion)
print("Sleight of Hand:", sleight_of_hand)
print("Stealth:", stealth)
print("Survival:", survival)
