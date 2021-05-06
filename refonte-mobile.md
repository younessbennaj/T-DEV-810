# Refonte mobile 

# Refonte de la topbar 

Consultez bien le LDS pour voir toutes les variantes de composants, l'idée est qu'au scroll on puisse fixer la barre de recherche à la navbar (voir sur Internet si besoin avec les mots-clés suivants : on scroll fixed navbar, on scroll sticky navbar



### Story

Refondre la top bar pour afficher les informations différemment

## Approche technique 

### Ancien composant 

```<LayoutHeaderWrapper> ...```: src/components/Layouts/SpaceLayout/SpaceLayout.tsx (:230)

### Refondre les éléments présent dans la topbar 

Actuellement la topbar est constitué de plusieurs éléments: 

+ Le boutton pour toggle le drawer 
+ Le titre de la page courrante 
+ Le boutton montant de la cagnotte de l'utilisateur 
+ Le boutton pour accéder au panier de l'utilisateur 
+ L'avatar de l'utilisateur avec une petite flèche pour toggle le menu du profil 

Les nouveaux éléments qu'on souhaite y retrouver: 

+ La bouton montant de la cagnotte de l'utilisateur (tout à gauche) 
+ Le boutton pour accéder au panier de l'utilisateur (à droite)
+ Le boutton avatar de l'utilisateur 

### Le bouton avatar 

Contrairement à ce qui est fait actuellement dans l'application, on ne veut plus l'apparition d'un dropdown au clique sur ce boutton. On veut maintenant rediriger directement l'utilisateur vers la page /espace-salarie/mon-profil. 

### Le layout de la topbar 

```
<Row justify='end' style={{padding:'12px 24px'}}>
  <Col style={{marginRight: 'auto'}}>Amount</Col>
  <Col style={{marginRight: '24px'}}>Cart</Col>
  <Col>Avatar</Col>
</Row>
```

### Différence topbar mobile et desktop

+ Boutton montant cagnotte à droit sur desktop et à gauche sur mobile

```
<Col style={{marginRight: responsiveContext.isSmallScreen ? 'auto' : '24px'}}>Amount</Col>
```

+ Le boutton avatar fonctionne différement sur mobile (simple boutton qui redirige vers la page profile) et sur desktop (dropdown menu)

``` 
{responsiveContext.isSmallScreen ? 
	(
		<DropdownStyled overlay={dropdownMenu}>
			... content here
		</DropdownStyled>
	)
	:
	(
		<Link to={PROFILE_PATH_HERE}>
		<Avatar
        src={user.avatar.url && user.avatar.url}
        style={{
        	backgroundColor: user.color
          ? user.color
          : themeColors.GREY_7,
        }}
      	>
      		{`${upperFirst(user.firstName.charAt(0))}${upperFirst(
	       	user.lastName.charAt(0)
          )}`}
       </Avatar>
       </Link>
	)
}
```

# Refonte de la topbar - Sticky Search Bar 

1) Refonte design pour la barre de recherche

2) Créer le style à activé pour l'effet "sticky" 

3) Ajouter la logique pour déclencher le style "sticky" au scroll

## Le composant 

```<LeeshopSearchBox />```: Le composant qui affiche la barre de recherche algolia ainsi que son wrapper styled. 

```<PageLeeshop />```: Le container qui affiche entre autre la barre de recherche et son wrapper. 

## Conditionnal rendering 

Sur mobile et sur desktop il faudrait afficher deux barres différentes: 

+ Sur mobile 

## Rendre la barre sticky

### le style

Ici on va reposer la logique sur une condition ```isSticky``` qui doit passer à true lorsqu'on déclenche l'évenement sticky change:

```
<RowStyled
	spacing={16}
   	style={{ padding: '0px 16px' }}
   isSticky={true}
>
```

On va ensuite créer un composant wrapper ```SearchBoxStickyWrapper``` qui va contenir le style et la logique pour rendre le container sticky

L'idée ça va être de détecter l'intersection entre mon SearchBoxStickyWrapper

***La cible***: C'est notre élément qui va s'intersecter avec une autre (dans notre cas le SearchBoxStickyWrapper)

***La racine***: element prédéfini avec lequel notre élement cible va s'intersecter

### Feedbacks

+ Fixer la ligne de pixel 
+ Faire un hook pour Truc

## Refonte bottom bar 

### Fichier à modifier

```
SpaceLayout.tsx
```

### Objectif

Objectif créer un nouveau composant ```<BottomBar />``` pour remplacer l'actuel Drawer/sidebar dans la navigation de l'app. 

⚠️ La difficulté est d'ajuster la taille des IconButton en fonction du nombre de module disponible dans l'app 

### Layout 

On va partir du model de donnée ```sidebarOptions``` qui existe dans ```spaceLayoutWithData.tsx``` pour créer notre bottombar.

On va à partir de ce tableau créer notre propre tableau depourvu de la hiérarchie menu/subMenu puisque dans la bottombar cette notion disparait. L'idée est de créer le model suivant: 

```
const bottomBarOptions = [
	{
		icon: JSX.Element,
		key: string
		redirection: string, 
		title: string
	}
]
```

```
set bottomBarOptions to sidebarOptions.map: option => [...option.subMenu]
```


* ```icon```: L'icon à afficher dans le boutton de navigation 
* ```key```: Pour le map()
* ```redirection```: Le path vers lequel redirigé l'utilisateur 
* ```title```: Le titre du boutton

On va donc nommer la ```<TabBar />``` le composant généraliste qui va composer la BottomBar et ```<TabBarItem />``` le composant qui décrit un lien de navigation dans la BottomBar.

### TabBar

```
<TabBar items={bottomBarOptions}/>
```

#### Layout 

```
<Row>
	bottomBarOptions.map(option => {
		<Col>
			<TabBarItem ...propTabBarItem />
		<Col>
	})
<Row>
```

### TabBarItem 

```
// "items.map(item => ...)" here
<TabBarItem icon={item.icon} key={item.key} redirection={redirection} title={item.title}  />
```

### Props 

+ ```icon```: L'icon à afficher dans le boutton de navigation 
+ ```key```: Pour le map()
+ ```redirection```: Le path vers lequel redirigé l'utilisateur 
+ ```title```: Le titre du boutton 

#### Layout

```
<Link to={redirection}>
	<Flex direction="column" justify="center">
		{icon}
		<Text>
			{title}
		</Text>
	<Flex>
<Link>
```

### Ajuster la taille des TabBarItems 

1) Récupérer la taille de ```bottomBarOptions``` => ```ratio``` 
2) Définir des règles de fontSize pour ```icon``` et ```title``` en fonction de ```ratio```

```
<TabBar items={bottomBarOptions} ratio={bottomBarOptions.length}/>
```

```
// "items.map(item => ...)" here
<TabBarItem icon={item.icon} key={item.key} redirection={redirection} title={item.title} ratio={ratio}  />
```

### Savoir quand le tab item est actif ?

```
<TabBarItem isActive={true}  />
```

Pour savoir si il est actif: 

+ Son redirection est égal au chemin dans l'url 







