#!/bin/python3
# генератор названий монстров и оружия для игр
import random
random.seed()
prefix = ('осьми', 'медве', 'псевдо', 'иноплане', 'мыше', 'чуче',
	'свино', 'грави', 'колды', 'мясо', 'верти', 'пуче', 'зеле',
	'мозго', 'зверо', 'перекати', 'змее', 'теле', 'колче', 'носо',
	'галлюци', 'электро', 'бензо', 'контро', 'долбо', 'дери', 'мульти',
	'космо', 'черве', 'нейро', 'био', 'нано', 'мега', 'турбо',
	'броне', 'буль', 'гидро', 'жиро', 'бормо')
suffix = ('зубка', 'сос', 'жуть', 'потам', 'завр', 'глот', 'жорка',
	'пёр', 'рубка', 'гузка', 'бойка', 'варка', 'выжималка',	'давка',
	'глазка', 'плюктор', 'жаба', 'пумпр', 'глаз', 'сосочка', 'мозг',
	'ёжик', 'грыз', 'хрюк', 'глюк', 'ножка', 'морда', 'рожа', 'хват',
	'пындра', 'бред', 'пуп', 'щуп', 'бобр', 'лёт', 'пырь', 'кабр',
	'пуз', 'морф', 'вик', 'мёт', 'пондер', 'лябр', 'бяка', 'шиш', 'луп',
	'мор', 'лярий', 'рыл', 'гад', 'блюдина', 'навт', 'френия')
#for i in range(5):
monster = random.choice(prefix) + random.choice(suffix)
print(monster)

prefix = ('свин', 'сов', 'слон', 'убив', 'сос', 'кошм', 'бормот',
	'плев', 'чуж', 'кальм', 'шиз')
suffix = ('ункул', 'урочка', 'уркл', 'оид', 'атор', 'унчик', 'уха',
	'улятор')
#for i in range(5):
monster = random.choice(prefix) + random.choice(suffix)
print(monster)

# Некоторые слова будут реально существующие - не обращайте внимание

# После того, как программа выдала Вам название монстра, попытайтесь его себе представить. Возможно, будет смешно.

# Я из принципа не генерирую матюги. Хотите матюги - делайте форк.
# Еще я из принципа не генерирую монстров семейства кошачьих, потому что я люблю кошек и не хочу над ними так издеваться.
