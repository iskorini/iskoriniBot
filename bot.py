import telepot
import sys
import time
import pprint
import os

class Jappo():
	def __init__(self, chat_id):
		self.__id = chat_id
		self.__location = ""
		self.__member = []
		self.__not_member = []
		self.__date = ""
		self.__closed = 0
	
	def setRistorante(self, nameLocation):
		self.__location = nameLocation
		print "dioculo"

	def closeJap(self):
		self.__closed = 1

	def add_member(self, name, member_id):
		if self.__closed == 0:
			if [name, member_id] not in self.__member:
				self.__member.append([name, member_id])
				if [name, member_id] in self.__not_member:
					self.__not_member.remove([name, member_id])
				return "ok"
			else:
				print "DEBUG: PARTECIPANTE RILEVATO"
				return "alreadymember"
		elif self.__closed == 1:
			return "closed"

	def remove_member(self, name, member_id):
		if self.__closed == 0:
			if [name, member_id] not in self.__not_member:
				self.__not_member.append([name, member_id])
				if [name, member_id] in self.__member:
					self.__member.remove([name, member_id])
				return "ok"
			else:
				print "DEBUG: PARTECIPANTE RILEVATO"
				return "alreadymember"
		elif self.__closed == 1:
			return "closed"

	def setDate(self, date):
		self.__date = date
		print "diomerda"
	def get_info(self):
		if len(self.__member)>0:
			members = reduce(lambda x, y: x+"\r\n"+y, map(lambda x:x[0], self.__member))
		else:
			members = "NESSUNO"
		if len(self.__not_member)>0:
			not_member = reduce(lambda x, y: x+"\r\n"+y, map(lambda x:x[0], self.__not_member))
		else:
			not_member = " "
		return "JAPPO ORGANIZZATO IL: "+self.__date+"\r\n"+"AL: "+self.__location+"\r\n"+"Partecipanti: "+str(len(self.__member))+"\r\n"+members+"\r\nNon partecipanti:\r\n"+not_member


class MyBot(telepot.Bot):

	def __init__(self, *args, **kwargs):
		super(MyBot, self).__init__(*args, **kwargs)
		self._answerer = telepot.helper.Answerer(self)
		self._jappo = dict()


	def hai_detto(self, message, chat_id,  name):
		hai_detto = "ahahahah "+name+" ha detto "
		if 'fica' in message:
			self.sendMessage(chat_id,hai_detto+"fica")
		elif 'fallo' in message:
			self.sendMessage(chat_id,  hai_detto+"fallo")
		elif 'ano' in message:
			self.sendMessage(chat_id, hai_detto+"ano")
		elif 'pene' in message:
			self.sendMessage(chat_id, hai_detto+"pene")
		elif 'figa' in message: 
			self.sendMessage(chat_id, hai_detto+"figa")
		elif 'fighe' in message:
			self.sendMessage(chat_id, hai_detto+"fighe")
		elif 'peni' in message:
			self.sendMessage(chat_id, hai_detto+"peni")
		elif 'ani' in message:
			self.sendMessage(chat_id, hai_detto+"ani")
		elif 'falli' in message:
			self.sendMessage(chat_id, hai_detto+"falli")
		elif 'anale' in message:
			self.sendMessage(chat_id, hai_detto+"anale")
		elif 'anal' in message:
			self.sendMessage(chat_id, hai_detto+"anal")
		elif 'sborra' in message:
			self.sendMessage(chat_id, hai_detto+"sborra")
		elif 'ahah' in message:
			self.sendMessage(chat_id, "cazzo ridi che ti avvolgo in una stagnola di panico e dolore")
		elif 'pluto' in message:
			self.sendMessage(chat_id, "Cosa dice una trota ad un cassonetto? IL CREDITO BANCARIO!")

	def jappo(self, chat_id):
		self._jappo['chat_id'] = Jappo(str(chat_id))
		jp = self._jappo['chat_id']
		show_keyboard = {'keyboard': [['Partecipo','Non partecipo']]}
		self.sendMessage(chat_id, "ORGANIZZIAMO UN JAPPO", reply_markup = show_keyboard)

	def organizzato(self, chat_id):
		try:
			self._jappo['chat_id'].closeJap()
			hide_keyboard = {'hide_keyboard': True}
			self.sendMessage(chat_id, 'JAPPO ORGANIZZATO', reply_markup=hide_keyboard)
		except Exception as e:
			self.sendMessage(chat_id, 'COSA CAZZO CHIUDI CHE NON HAI ORGANIZZATO NIENTE')
	
	def addMember(self, chat_id, name, member_id):
		try:
			result = self._jappo['chat_id'].add_member(name, member_id)
			if result == 'ok':
				self.sendMessage(chat_id, name+" partecipa")
			elif result == 'alreadymember':
				self.sendMessage(chat_id, name+" ho capito che partecipi, vuoi farmi incazzare?")
			elif result == 'closed':
				self.sendMessage(chat_id, "COSA CAZZO VUOI PARTECIPARE CHE NESSUNO HA ORGANIZZATO NIENTE")
		except Exception, e:
			self.sendMessage(chat_id, 'COSA CAZZO VUOI PARTECIPARE CHE NESSUNO HA ORGANIZZATO NIENTE')

	def removeMember(self, chat_id, name, member_id):
		try:
			result = self._jappo['chat_id'].remove_member(name, member_id)
			if result == 'ok':
				self.sendMessage(chat_id, name+" non partecipa")
			elif result == 'alreadymember':
				self.sendMessage(chat_id, name+" ho capito che non partecipi, vuoi farmi incazzare?")
			elif result == 'closed':
				self.sendMessage(chat_id, "COSA CAZZO VUOI PARTECIPARE CHE NESSUNO HA ORGANIZZATO NULLA")
		except Exception, e:
			self.sendMessage(chat_id, 'COSA CAZZO VUOI PARTECIPARE CHE NESSUNO HA ORGANIZZATO NULLA')

	def get_info(self, chat_id):
		try:
			jp_info = self._jappo['chat_id'].get_info()
			self.sendMessage(chat_id, jp_info)
		except Exception as e:
			print e
			self.sendMessage(chat_id, 'COSA CAZZO VUOI INFORMAZIONI CHE NESSUNO HA ORGANIZZATO NULLA')

	def set_date(self, chat_id, message):
		print "cazzoculo"
		try:
			self._jappo['chat_id'].setDate(message[11:])
		except Exception, e:
			self.sendMessage(chat_id, 'COSA CAZZO DATEGGI CHE NESSUNO HA ORGANIZZATO NULLA')

	def set_ristorante(self, chat_id, message):
		print "merda"
		try:
			self._jappo['chat_id'].setRistorante(message[12:])
		except Exception, e:
			self.sendMessage(chat_id, 'COSA CAZZO METTI IL RISTORANTE CHE NESSUNO HA ORGANIZZATO NULLA')

	def handle(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)
		message = msg['text'].lower()
		name = msg['from']['first_name']
		member_id = msg['from']['id']
		chat_id = msg['chat']['id']
		print name+": "+message+" in chat->"+str(chat_id)
		#parte jappo
		if '/jappo' in message:
			self.jappo(chat_id)
		elif '/organizzato' in message:
			self.organizzato(chat_id)
		elif '/partecipanti' in message:
			self.get_info(chat_id)
		elif 'non partecipo' in message:
			self.removeMember(chat_id, name, member_id)
		elif 'partecipo' in message:
			self.addMember(chat_id, name, member_id)
		elif '/datajappo' in message:
			self.set_date(chat_id, message)
		elif '/ristorante' in message:
			self.set_ristorante(chat_id, message)
		#messaggi di merda
		self.hai_detto(message, chat_id, name)
	


if __name__ == '__main__':
	
	bot = MyBot('')
	bot.message_loop()
	print("ready")
	while 1:
		time.sleep(10)