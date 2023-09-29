# Guide pour utitiliser Word 2 PDF

**\*Cet outil est encore un prototype\***

### Étapes à suivre:

1. Finaliser l'article dans Word
2. [Baliser](#les-balises) les sections de l'article (étape très importante!)
3. Ouvrir Word 2 PDF
4. Chosir le fichier Word
5. Choisir le dossier où sera créé le fichier powerpoint
6. Choisir la taille de la police
7. Choisir la photo sur la première page\*
8. Appuyer sur go et attendre qu'une fenêtre de succès apparaisse

\* Attention, la source de la photo choisie sera automatiquement liée à la dernière source dans le document Word. Ignorer ce champ pour omettre la photo.

## Les balises
Les balises servent de repère pour que votre texe soit transférer de word sur powerpoint, avec la forme désirée. Veuiller insérer les balises toujours **au début d'une ligne avec un espace après**. Aucune balise n'est nécéssaire pour les paragraphes de texte.

### Table des balises
```text
id: [id]
@ [auteur]
% [Titre principal de l'article]
%% [Sous-titre principal de l'article]
# [Pays]
## [Sous-titre]
```
### Example:
```text
id: #00-23-2323

@ Micheal Faraday

% Veille sur l'intelligence artificielle

%% Immersion dans la matière grise des machines

## Qu’est-ce que l’intelligence artificielle?

L'intelligence artificielle est conceptualisée comme un domaine scientifique...

# Canada

## L'IA dans le domaine de la santé

Le cas de Deep Genomics⁷ au Canada est un exemple remarquable bla bla bla...
```
