#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return 0

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	pass

def average(values: list) -> list:
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme_totale=0
	for v in range (len(values)):
		somme_totale+= values[v]
		v+=1
		pass # La variable v contient une valeur de la liste.

	return (somme_totale/v)
def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	valeur_restante = value
	ones = 0
	twos = 0
	fives = 0
	tens = 0
	twenties = 0
	while valeur_restante != 0:
		if valeur_restante >= 20:
			twenties = value//20
			valeur_restante = value - twenties*20
			#print(value, " value")
			pass
		elif valeur_restante >= 10:
			tens = valeur_restante //10
			valeur_restante = valeur_restante - tens*10
			pass
		elif valeur_restante >= 5:
			fives = valeur_restante//5
			valeur_restante = valeur_restante - fives*5
			pass
		elif valeur_restante >= 2:
			twos = valeur_restante//2

			valeur_restante = valeur_restante - twos*2
			print(valeur_restante, " valeur restante 2")
			pass
		elif valeur_restante >= 1 :
			ones = 1
			valeur_restante=0
			pass

	return (twenties, " billets de 20$, ", tens, " billets de 10$ ", fives, " billets de 5$ ", twos, " pieces de 2$ ", ones, " piece de 1$ dollar");

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
