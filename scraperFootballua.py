import requests

from bs4 import BeautifulSoup

base = 'http://football.ua/club/'
init_request = requests.get('http://football.ua/club/27-roma.html')
soup = BeautifulSoup(init_request.content, 'html.parser')

# players raw data with all needed html
content = soup.find('article', {'class':'team-consist'})

#team link list
allLink=[]
#link id of each team
teamLinkId = []

#getting all team page links
def get_link():
	link_request = requests.get('http://football.ua/italy/table.html')
	link_soup = BeautifulSoup(link_request.content, 'html.parser')
	for i in link_soup.find_all('td', {'class':'team'}):
		for t in i.find_all('a'):
			allLink.append(t['href'])
	for i in allLink:
		l = base+i.split('/')[4]
		teamLinkId.append(l)
	return teamLinkId

#clubs dict
clubs = {}
#raw data with players accordingly their role
pos = []
#list with players names accordingly to their position
gkName=[]
dfName=[]
mfName=[]
fwName=[]
#list with all names
allName=[]
#list with all player numbers
allNum=[]
#list with all player nationality
allNat=[]
#list with all player birth date
allBirth=[]
#list with positions
posName = []
#main dict
teamRole = {}

#clear all lists
def clear_all_lists():
	#clubs dict
	clubs = {}
	#raw data with players accordingly their role
	pos = []
	#list with all names
	allName=[]
	#list with all player numbers
	allNum=[]
	#list with all player nationality
	allNat=[]
	#list with all player birth date
	allBirth=[]
	#list with positions
	posName = []
	#main dict
	teamRole = {}

#team positions
def get_posname():
	for h in base_content.find_all('h4',{'class':'consist-header'}):
		posName.append(h.get_text())

#get all player raw data
def get_players_rdata():
	global pos
	gk = base_content.find_all('table', {'class':'consist-table'})[0]
	df = base_content.find_all('table', {'class':'consist-table'})[1]
	mf = base_content.find_all('table', {'class':'consist-table'})[2]
	fw = base_content.find_all('table', {'class':'consist-table'})[3]
	pos = [gk, df, mf, fw]
	return pos

#get player name
def put_name():
	for p in pos:
		if p == gk:
			for pl in p.find_all('a', href=True):
				gkName.append(pl.get_text())
		elif p == df:
			for pl in p.find_all('a', href=True):
				dfName.append(pl.get_text())
		elif p == mf:
			for pl in p.find_all('a', href=True):
				mfName.append(pl.get_text())
		elif p == fw:
			for pl in p.find_all('a', href=True):
				fwName.append(pl.get_text())

#all numbers
def get_num():
	for p in pos:
		for n in p.find_all('td', {'class':'num'}):
			allNum.append(n.get_text())

#all names
def get_names():
	for p in pos:
		for n in p.find_all('a'):
			allName.append(n.get_text())

#all nationality
def get_nat():
	for p in pos:
		for n in p.find_all('img'):
			allNat.append(n['alt'])

#all birth dates
def get_birth():
	for p in pos:
		for n in p.find_all('td', {'class':'birth'}):
			allBirth.append(n.get_text())

def main():
	clear_all_lists()
	get_link()
	# for i in teamLinkId:
	# 	print(i)
	for l in teamLinkId:
		global base_content
		base_request = requests.get(l)
		base_soup = BeautifulSoup(base_request.content, 'html.parser')
		print(l)
		# players raw data with all needed html
		base_content = base_soup.find('article', {'class':'team-consist'})
		get_players_rdata()
		# print(pos)
		get_birth()
		get_num()
		get_names()
		get_nat()
		get_posname()
		clubs[base_soup.find('div', {'class':'info-intro'}).h1.text]={key: value for (key,value) in [(allName[i], {"birth":allBirth[i], "nat":allNat[i], "num":allNum[i]}) for i in range(0, len(allNum))]}
		print(base_soup.find('div', {'class':'info-intro'}).h1.text+' DONE')
		allName.clear()
		allBirth.clear()
		allNat.clear()
		allNum.clear()
	print(clubs)
main()
