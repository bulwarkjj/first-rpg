from low_level_baddies.goblins import FootGoblins
from create_hero import Hero

kevin = FootGoblins()
matt = Hero()

print(kevin.__dict__)
print(matt.__dict__)

while kevin.health > 0:
	if kevin.health == 1 and kevin.aggression < 8:
		print("Kevin ran away!!!")
		break
	elif matt.strength > kevin.strength:
		if "shield" in kevin.equip:
			kevin.health -= 0.5
			print("hit, but kevin shield block half the damage")
		else:
			kevin.health -= 1
			print("direct hit")

if kevin.health == 0:
	print("Kevin Died")