#coding: utf-8

import csv
import json
import requests

entetes = {
	"User-Agent":"Philippe Léger",
	"From":"philippe.asselinleger@gmail.com"
}

fichier = "coursems.csv"
fichier2 = "posts.csv"

#Le fichier équivaut à ma première base de données faite à la main et qui rescense les agents et candidats politiques de toutes les allégances politiques confondues. Il serait mise à jour, mais pour l'instant, il correspond à tous les candidats ou agents politiques ayant 1000 «likes» ou plus sur le compte public. L'API de FB ne tient pas compte des pages privées, comme celle de Gabriel Nadeau-Dubois, suivi par environ 27 000 personnes. C'est une de mes limites de mon script.
#Le fichier 2 est le « fichier d'arrivé ». Il est le résultat de mon script.

f1 = open(fichier)

lignes = csv.reader(f1)

next(lignes)

#Il s'agit ici d'ouvrir mon fichier et le lire « une ligne après l'autre ».

jeton = "EAACEdEose0cBAMy1ZCApBYZB9c4bUOol7ZB9ix75bj2itZAMZC4u1BGsv2FveVSPZAbZBiXp8VgXg7GYEOXKp3up4RLCEuYZBUZAQEcisQktRxOuqgnGYdWueZCy1TzrULIySSqMqCtkZBogjrBwxReWSLYBWZALUhPz29NNpE5lLI1ZBHFfQuqPDYRIAIOjv8u1vL0K3YPQ2QI6oCwZDZD"

#Ici, mon jeton n'est pas définif, il changera constamment. L'API de FB est valide pendant une heure et demi selon mes estimations (lorsque je faisais mes modifications dans le document fichier 2)

for ligne in lignes:
	nombre = ligne[2]
	# url = "https://www.facebook.com/{}/".format(nombre)
	# print(url)
	# la boucle « for ligne in lignes (2) » me permet d'aller chercher mon élément 2 dans fichier de départ. On veut le deuxième élément du fichier, donc l'ID des personnes identifiés. Il me permet d'aller chercher les informations sur chacun(e) des utilisateurs politiques au Québec.

	url = "https://graph.facebook.com/v3.0/{}/posts?fields=reactions.summary(true)%2Ccomments.summary(true)%2Cmessage%2Ccreated_time%2Cshares%2Cstatus_type%2Clink%2Cdescription%2Cname&limit=100&access_token={}".format(nombre, jeton)
	req = requests.get(url, headers=entetes)
	contenu = req.json()
	#Ici, je suis venu prendre le «c url » donné par Facebook pour recueillir les réactions et les commentaires des personnes choisies. Le tout est suivi d'un « summary(true) », qui correspond à une formule que vous m'avez donné en classe.
	# print(contenu["posts"]["data"])

	# if data["id"] 
	
	for data in contenu["data"]:
		try : 
			partage = data["shares"]["count"]

		except :
			partage = 0

		#Étant donné que les autres infos nécessaires n'apparaissent pas dans la page source de la page, nous devons aller les chercher différement. Le nombre de partages est par contre donné sous le shares et le count de la page. 
		#Je me suis assuré de rajouter un except pour ne pas que mon script arrête de rouler lorsque le résultat est « blank ».

		try :
			reactions = data["reactions"]["summary"]["total_count"]

		except :
			reactions = 0

		#Un peu dans la même logique : je vais chercher dans mon dictionnaire le « reactions », ensuite le « summary » et le « total count » pour calculer mon nombre de réactions. Comme dans une poupée russe.

		try :
			comments = data["comments"]["summary"]["total_count"]

		except :
			comments = 0


		#Même principe pour mon nombre de commentaires. 


		try :
			messages = data["message"]

		except :
			messages = "?"


		#Même principe, mais dans un autre dictionnaire, pour savoir la teneur de la publication.


		try :
			date = data["created_time"]

		except : 
			date = "?"

		#On veut ici la date de création.

		try :
			typestatut = data["status_type"]

		except : 
			typestatut = "?"

		#On veut ici mon type de statut

		try :
			lien = data["link"]

		except : 
			lien = "?"

			#On veut ici le lien vers la publication.

		try :
			description = data["description"]

		except : 
			description = "?"

		#On veut ici le lien vers la description de la publication. Elle apparait rarement selon mon script.

		try :
			name = data["name"]

		except : 
			name = "?"

		#idem

		engagement = reactions + comments + partage
		post = [ligne[1], data["id"], reactions, comments, partage, engagement, messages, date, typestatut, lien, description, name]

		#Étant donné que nous considérons l'engagement d'une publication par la somme des réactions, des commentaires et des partages, j'ai rajouté cette partie à mon script. C'est par cette variable que je pourrais voir l'emprunte forte ou faible de mes personnes choisies.
		#La variable post est une ligne de mon fichier csv final. Je mets en ordre ce que je veux dans mon fichier. Remarquez que j'ai utilisé des éléments de mon premier fichier comme le nom et l'id.

		print(post)

		f2 = open(fichier2, "a")
		monique = csv.writer(f2)
		monique.writerow(post)

		#Dernière étapte qui me permet de me créer un nouveau fichier avec toutes les informations que j'ai besoin. Il correspond à mon fichier 2. 

		# print(reactions)

		# print(partage)

	# ajouter = nom de la page

		# somme = data["id"]


 	


		# ?fields=reactions.summary(true),comments.summary(true)
		# 122369341291136?fields=posts
		# 11392874217?fields=posts
		# 11392874217_10156825039704218?fields=reactions.summary(true),comments.summary(true)

		# .format(somme)






