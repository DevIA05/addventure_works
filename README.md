# addventure_works

## ETL

### Extract
Extraction (Extract) : Récupére les données dans un format brut (non structuré) à partir de différentes sources de données

    - bases de données
    - des fichiers
    - des services web, 
    - etc. 

### Transform
Transformation (Transform) : Rendre les données
- cohérentes, 
- nettoyées, 
- filtrées 
- adaptées aux besoins du système cible 

Les transformations peuvent inclure des opérations de:
- conversion de formats de données, 
- la normalisation des valeurs, 
- l'agrégation, 
- la fusion de données provenant de différentes sources, 
- etc.

### Load

Chargement (Load) : Envoie dans une infrastructure de stockage. 
- base de données, 
- un entrepôt de données, 
- ect, 

Le chargement peut impliquer la création de nouvelles tables, la mise à jour des données existantes ou l'ajout de nouvelles données à celles déjà présentes.

### Intéret
Garantir 
- l'intégrité, 
- la qualité
- la cohérence des données 


## OLTP
OLTP: Online Transaction Processing

Système de traitement des transactions en ligne.

Les transactions individuelles sont traitées en temps réel.

Prend en charge des opérations de transaction rapides et concurrencées:
- ajout, 
- la mise à jour, 
- la suppression

de données dans une base de données.

Exemple: 
- systèmes de gestion des commandes, 
- les systèmes de réservation, 
- les systèmes bancaires en ligne,
- ect.

## OLAP
OLAP: Online Analytical Processing 

Contrairement à l'OLTP, qui se concentre sur les transactions en temps réel, l'OLAP se concentre sur
- l'analyse
- la consultation 
des données pour prendre des décisions.

Exemple d'applications:
- analyses commerciales, 
- la planification financière, 
- l'analyse des ventes, 
- la segmentation client, 
- la prévision des performances, 
- etc. 

Exemple d'outils:
- Microsoft SQL Server Analysis Services
- Oracle OLAP 
- IBM Cognos

## DataWarehouse
Entrepôt de données

Infrastructure qui stocke et gère de grandes quantités de **données provenant de différentes sources**.

## Data Lake
Lac de données 

Infrastructure qui permet de stocker de grandes quantités de **données brutes et non structurées**. 

S'adapter à 
- différents types de données
- à des volumes croissants

offre:
- flexibilité pour stocker et 
- gérer de nouvelles sources de données au fur et à mesure.

## Data Mart

Contient une petite partie des données que l'entreprise stocke dans un système de stockage plus important. 

**Les données sont centré sur un seul domaine, sujet ou fonction**.

Exemple:
- les ventes, 
- le marketing 
- la finance 


## DataMesh

Se focalise sur la gestion des données

Améliore:
- l'interopérabilité, 
- la collaboration 
- la gouvernance des données 

au sein d'une organisation. 

**Met l'accent sur la création d'écosystèmes de données interconnectés** plutôt que sur des silos de données centralisés.