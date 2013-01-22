#!/usr/bin/python

import random;
import time;

random.seed()

def clients(phenny, input):
	phenny.say('There are several IRC clients for all operating systems. For Windows, we recommend hexchat (Free X-Chat Successor, http://hexchat.org). For Unix/Linux consider X-Chat (GUI) or irssi (console), both available in your repository. For Mac try XChat Aqua (http://xchataqua.github.com/)')
clients.rule = r'^clients\?'

def dnsleaks(phenny, input):
        phenny.say('A DNS leak means that you are using a fixed nameserver (like the one from your provider) which may compromise your anonymity. Read about it here: http://www.dnsleaktest.com/what-is-a-dns-leak.php')
        phenny.say('You can test this on this website: http://www.dnsleaktest.com/ - to prevent DNS leaks when using TOR, read the following: https://trac. torproject.org/projects/tor/wiki/doc/PreventingDnsLeaksInTor')
dnsleaks.rule = r'^dnsleaks\?'

def freevpn(phenny, input):
	phenny.say('Personally I would not trust any free VPN for the simple reason that if a VPN provider has no product for sale, chances are that they are selling YOU.')
freevpn.rule = r'^freevpn\?'

def hacking(phenny, input):
	phenny.say('Becoming a hacker is nothing to be achieved overnight. The typical skillset of a hacker is build on years of coding experience in various languages, plus a good deal of network knowledge. For an outline on how to get there, I recommend the following read: http://www.catb.org/esr/faqs/hacker-howto.html')
hacking.rule = r'^hacking\?'

def i2p(phenny, input):
	phenny.say('I2P is an anonymous network, exposing a simple layer that applications can use to anonymously and securely send messages to each other http://www.i2p2.de/intro.html - http://www.i2p2.de/faq.html')
i2p.rule = r'^i2p\?'

def irch(phenny, input):
	phenny.say('IRC is Internet Relay Chat - which is where you are chatting right now. More precisely you are on irc.voxanon.net which runs inspircd (http://www.irc-wiki.org/InspIRCd). If you need general IRC help, ask in channel. For recommended IRC clients, type clients?. For network specific help /join #help')
irch.rule = r'^irc\?'

def python(phenny, input):
	phenny.say('I recommend: http://learnpythonthehardway.org/. A good very comprehensive book on this is O\'Reilly Programming Python. Download the 4th edition here: http://www.par-anoia.net/assessment/books/coding/Programming_Python_-_OReilly_4th_Ed.pdf')
python.rule = r'^python\?'
python.priority = 'medium'

def tor(phenny, input):
	phenny.say('Tor is a network of virtual tunnels that allows people and groups to improve their anonymity and security on the Internet. Read more here: https://www.torproject.org/about/overview.html.en and here https://www.torproject.org/docs/documentation.html.en')
tor.rule = r'^tor\?'

def vm(phenny, input):
	phenny.say('Virtual machines allow you to run one operating system emulated within another operating system. Your primary OS can be Windows 7 64-bit, for example, but with enough memory and processing power, you can run Ubuntu and OS X side-by-side within it. More information: http://lifehacker.com/5714966/five-best-virtual-machine-applications')
vm.rule = r'^vm\?'

def vpn(phenny, input):
    phenny.say('Currently I can recommend two privacy vpn providers, '+ input.nick +': Perfect Privacy (http://perfect-privacy.com) and ovpn (http://ovpn.to)')
vpn.rule = r'^vpn\?'
vpn.priority = 'medium'


#topics


def topics(phenny, input):
    phenny.say('Currently I can advise about the following topics: clients, freevpn, dnsleaks, hacking, i2p, irc, python, vm, vpn and tor. Use "topic?" to get specific info on a topic.')
topics.rule = r'^topics\?'


#generic stuff

def Logbot(phenny, input):
	time.sleep(2)
	lanswer = random.choice(('lol logbots <3', 'I pity those who worry about logbots.', input.nick+', you\'re a logbot.'))
	phenny.say(lanswer)
Logbot.rule = r'.*logbot.*'

def feds(phenny, input):
	time.sleep(2)
	fanswer = random.choice(('I am a Fed! And so is my wife!', 'I don\'t care about Feds.', 'lolfeds :D', 'To apply as Fed join #feds today!'))
	phenny.say(fanswer)
feds.rule = r'(?i)(.*\bfeds\b.*|.*\bfed\b.*)'

def tyler(phenny, input):
	time.sleep(2)
	tanswer = random.choice(('OMG TYLER TYLER TYLER TYLEEEEER! *flips out*', 'Tyler... isn\'t that something like RefRef?'))
	phenny.say(tanswer)
tyler.rule = r'(?i)(.*\btyler\b.*)'

def niceday(phenny, input):
	time.sleep(1)
	rand = random.randint(1,5)
	if rand == 1:
		phenny.say(input.nick+': A nice day to you, too, Sir.')
niceday.rule = r'(?i)(fuck you)'


#events

def join_shh(phenny, input):
	time.sleep(1)
	randm = random.randint(1,35)
	if (randm == 1):
		phenny.say('Ehh, but don\'t tell ' + input.nick + '!')
join_shh.event = 'JOIN'
join_shh.rule = r'.*'

#chatter

def chatter(phenny, input):
	chan = input.sender
	if (chan.lower() == '#opnewblood'):
		randm = random.randint(1,1500)
		if (randm == 1):
			phenny.say('We should simply kidnap and kill him and run him through a woodchipper.')
		elif randm == 2:
			phenny.say('I am a serious bad ass right now and I\'m not sure you realize that.')
		elif randm == 3:
			phenny.say('I am only one removed from the President of the United States!')
chatter.event = 'PRIVMSG'
chatter.rule = r'.*'

#punishment

def troutpatro(phenny, input):
	phenny.write(['kick',input.sender,input.nick,'Trout slaps are incredibly lame. [Troutpatrol]'])
#	phenny.say('!kick '+ input.nick + ' Trout slaps are incredibly lame. [Troutpatrol]')
troutpatro.rule = r'.*slaps.*(trout|fishbot)'
