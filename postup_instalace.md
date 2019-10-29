INSTALACE A ZPROVOZNĚNÍ
=======================

GITHUB
------
- [ ] vytvoříme účet na GitHubu a založíme si repozitář pro soubory, spojené s aplikací. Repozitář může být i private, Heroku z toho umí deployovat, ale v tuhle chvíli stačí normální repozitář. 

	* [GitHub](https://github.com/)

	* [dokumentace a videonávody k GitHubu](https://guides.github.com/)

- [ ] všichni, kdo budou pracovat na aplikaci(resp. chtějí mít právo posílat o a/nebo upravovat soubory v repozitáři k aplikaci) musejí mít založený účet na GiHubu. 

- Repozitář s aplikací je ale pouze na **jednom** účtu a ostatní účastníci projektu jsou do něj přidání jako *collaborator*. 

- Repozitář si nejlépe **naklonujeme**:
	* na hlavní stránce daného repozitáře klikneme na `Clone or download`.
	* otevře se okýnko s odkazem, ten si skopírujeme.
	* ve Visual Studio Code klikneme na View a hned nahoře *Command Pallete* (lze také použít zkratku `Ctrl + Shift + P`).
	* do Command Pallete napíšeme `git: Clone` a odklepneme `Enterem`.
	* Vložíme zkopírovaný odkaz z GitHubu.
	* vybereme, kde chceme v počítači složku se soubory uložit (a kam se nám také budou ukládat naše změny) a potvrdíme. 
	* dole se otevře dialogové okno, kde odklepneme, zda chceme danou složku otevřít v tomto okně nebo v nově otevřeném.	

HEROKU
------

- [ ] vytvoříme účet na Heroku

	* [Heroku](https://dashboard.heroku.com)

	* [dokumentace k Heroku](https://devcenter.heroku.com/categories/reference)

- [ ] založíme aplikaci na Heroku 

	* tlačítko *new* vpravo nahoře -> *create new app* -> vyplnit jméno aplikace a region(Evropa), zbytek neřešíme.

- [ ] v *Deployment method* zvolíme **Connect to Github**, přihlásíme se na svůj GitHub účet, zvolíme příslušný repozitář a připojíme jej tlačítkem **Connect**

- [ ] v *Automatic Deploys* nastavíme `branch` (větev) v GitHubu, ze které chceme, aby se aplikace zveřejňovala na webu. V tuto chvíli doporučuji nechat branch nastavenou na defaultně danou `master` branch. Znamená to, že dokud nebudete mít vaše změny *pushnuté* do `masteru` na GitHubu, aplikace se nemění.

- na aplikaci se zpravidla podílí více lidí, ve vašem případě budete přinejmenším dvě. Je tedy třeba parťačku přidat jako spolupracovníka, tj. *collaboratora*. V hlavním menu klikneme na druhou záložku zprava s názvem *Acces*. Otevře se nám přehled všech lidí, kteří mají k naší aplikací nějaké přístupy. V tuhle chvíli tam vidíme jen sebe. 
- Klikneme na *Add collaborator*, otevře se nové okno, kam zadáme emailovou adresu parťačky. Po *Save changes* je tato emailová adresa přidána do přehledu lidí s přístupem a právy k aplikaci. 
- Pokud parťačka dosud nemá účet na heroku, musí si ho nejprve vytvořit. Není třeba nic hledat, na zadaný email je odeslána zpráva s pozvánkou ke spolupráci na aplikaci a linkem, který ji na založení účtu na heroku přesměruje. 
- pokud už parťačka účet na heroku má, tak přijde jen zpráva s pozvánkou ke spolupráci na příslušné aplikacemi a instrukcemi, jak se k ní dostane.   

- [ ] v hlavním menu klikneme na druhou odrážku zleva *Resources* a otevře se nám stránka, kde je možné nainstalovat potřebné rošíření heroku pro propojení s databází. My budeme pracovat s PostgreSQL, možností je však samozřejmě daleko více. 

 Podrobnější informace o možných rozšířeních najdete v dokumentaci. 

- [ ] najdeme rozšíření s názvem  *Heroku Postgres*, po kliknu na příslušnou dlaždici začneme s instalací klikem na *Install Heroku Postgres*. Pole *Add-on plan* neměníme a necháme nastavené *Hobby Dev-Free*. V poli *App to provision* on zvolíme aplikaci, ke které chceme rozšíření připojit. Volbu potvrdíme stiskem *Provision add-on*.

- [ ] Zpátky na stráce pod záložkou *Resources* a v sekci Add-ons vidíme rozšíření *Heroku Postgres*. Klikneme na něj a v novém okně se nám otevře stránka se souhrnnými údaji.


POSTGRESQL A PGADMIN
--------------------

- stáhneme PostgreSQL a nainstalujeme PgAdmin

	* [PostgreSQL](https://www.postgresql.org/)

	* [dokumentace k PostgreSQL](https://www.postgresql.org/docs/)


SOUBORY PRO DEPLOY APLIKACE NA WEB
----------------------------------

- requirements.txt
  obsah: `flask`
  	 `gunicorn`

- Procfile:
  obsah: `web: gunicorn pysoubor_s_aplikaci:jmeno_aplikace`


- python soubor, kde bude vytvořena flasková aplikace a aspoň jedna route
  obsah:
  ```
	from flask import Flask, render_template

	#vytvořila jsem novou aplikaci s názvem ivuška ve Flasku
	application = Flask('ivuska')


	@application.route('/')
	def show_index():
    		return render_template('title.html')
   ``` 

- html soubor, abychom měli co zobrazovat, v našem případě je to `title.html`:
  obsah: 
  ```  
	<!DOCTYPE html>
	<html lang="en">
	<head>
    <meta charset="UTF-8">
    <title>Title</title>

	</head>
	<body>
	Ahoj, já jsem tvoje aplikace  na webu!
	</body>
	</html>
  ```

Pak už stačí jen zadat do prohlížeče www.nazevmojiaplikace.herokuapp.com a měla Tvoje aplikace by Tě měla pozdravit z webových stránek :-)! 
