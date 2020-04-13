# Projet

Le modeste objectif de ce projet est de dérouler l'exemple fourni par le créateur de la librairie gensim à l'adresse ci-contre (https://radimrehurek.com/gensim/wiki.html).

# Installation de l'environnement (Windows)

1. Mise en place du virtualenv : `python -m venv venv`
2. Activation du virtualenv : `source venv\Scripts\activate.bat`
3. Installation des modules : `pip install -r requirements.txt`

# Installation

1. We first set the virtual env : `python -m venv venv`
2. Activate it : `source venv/bin/activate`
3. Install some modules (gensim included) : `pip install -r requirements.txt`

# Let's do this tutorial !

1. First we have to download the raw material (a.k.a wikipedia dump) : `./download_wikipedia.sh`
   
   If everything goes smoothly, the dump will be available in `DATA/OUT`. Congrats ! You're the happy owner of 16 compressed Gigs of humankind wisdom (as well as many other things).
	
2. Extract dictionnary and corpus from wikipedia dump : `python -m gensim.scripts.make_wiki DATA/IN/enwiki-latest-pages-articles.xml.bz2 DATA/OUT/wiki`
