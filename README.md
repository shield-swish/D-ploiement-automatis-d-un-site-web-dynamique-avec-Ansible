# D-ploiement-automatis-d-un-site-web-dynamique-avec-Ansible

Introduction

Ce projet s’inscrit dans cette démarche, en mettant en œuvre une solution d’automatisation complète pour déployer une application web dynamique en utilisant Ansible. Le site est développé avec le framework Flask (Python), utilise une base de données SQLite, et est destiné à être déployé sur une machine virtuelle locale (VMware) ou cloud (Azure).


# Description de l’architecture

Le projet repose sur une architecture simple en 2 tiers :

-  Frontend & Backend : intégrés dans une application Flask, avec formulaire HTML, routes Python, et logique métier.
-  Base de données : locale, sous forme d’une base SQLite (messages.db), permettant de stocker les messages soumis via le formulaire.

Le déploiement est entièrement géré par Ansible, via :

Un fichier inventory.ini qui contient les adresses IP des machines cibles.

Un playbook Ansible qui :
-  Met à jour les paquets
-  Installe Apache, Python3, pip, Flask et ses extensions
-  Déploie l’application dans /var/www/monsite
-  Active et démarre le service Apache
-  Ouvre le port HTTP (80) si le pare-feu UFW est activé


# Exemple de fonctionnalité

Le site comprend :

-  Un formulaire HTML permettant de saisir nom, email, et message.
-  Une base de données SQLite qui stocke chaque soumission.
-  Une page affichant les messages enregistrés.

# Résultats obtenus

Une fois le playbook exécuté, le site est directement accessible via http://<adresse IP>:5000. L’utilisateur peut y soumettre un message, qui est automatiquement sauvegardé en base.
L’ensemble du processus est entièrement automatisé. Aucune intervention manuelle n’est requise sur la machine cible, ce qui garantit un déploiement homogène et rapide.


Ce projet a permis de démontrer l’intérêt d’utiliser Ansible pour automatiser un déploiement web. Grâce à une infrastructure claire et reproductible, il est possible de déployer un site Flask dynamique en quelques minutes sur n’importe quel hôte Linux. Ce travail pose les bases d’une approche plus industrielle du déploiement d'applications, facilement extensible à d'autres technologies et environnements cloud.


