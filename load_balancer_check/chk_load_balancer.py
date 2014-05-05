#!/usr/bin/python

import urllib
import urllib2


serv_ip = []
serve_state = {}
choice_environments = {
        "1" : "dit",
        "2" : "prod",
        "3" : "stage",
        "4" : "sit",
        "5" : "test",
}        

def switch_modes(server, state, user, tpass):
    if state == "testing":
        theurl = "http://{ip}/rbproxy/changeToProdMode".format(ip=server)
    else:
        theurl = "http://{ip}rbproxy/changeToTestMode".format(ip=server)
    #urllib.urlopen("http://{ip}/rbproxy/changeToProdMode".format(ip=server))
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, theurl, user, tpass)
    
    authhandler = urllib2HTTPBasicAuthHandler(passman)

    opener = urllib2.build_opener(authhandler)

    urllib2.install_opener(opener)
    
    pagehandle = urllib2.urlopen(theurl)
    
def open_enviro(choice):
    """Takes an arguement for which enviornment file to open, opens the file and adds it to a list
    called serv_ip"""
    in_file = open(choice, 'r')
    serv_ip = in_file.readlines()
    serv_ip = [item.rstrip("\n") for item in serv_ip]
    in_file.close
    return serv_ip

def main():
    print("\n")
    print("\n")
    print("What environment do you want to check?"+ "\n")
    print("1. dit.rb.local")
    print("2. rbiprod.local")
    print("3. rbistg.local")
    print("4. sit.rb.local")
    print("5. test.rb.local" + "\n")

    choice = raw_input("Choice: ").strip()
    print "\n"

    if choice in choice_environments:
        serv_ip = open_enviro(choice_environments[choice])

    else:
        print "Please choose a correct environment."


    for entry in serv_ip:
        f =  urllib.urlopen("http://{domain}/rbproxy/ecvgroup".format(domain=entry))
        status = f.read()
    
        print "Server {domain} is in {status} mode".format(domain=entry, status=status)
        serve_state[entry] = status
        f.close


    print  "\n"
    print  "Would you like to change any server modes?"
    print  "\n"
    print  "1. Switch from testing"
    print  "2. Switch from production"
    print  "3. To exit"
    print  "\n"

    choice_switch = raw_input("Choice: ").strip()

    if choice_switch == "3":

        print "\nThanks for playing!!!"

    else:
        user = raw_input("Please enter the username")
        upass = raw_input("Please enter a password")


        for item in serve_state:
    
            if serve_state[item] == "testing":
               switch_modes(item, serve_state[item], user, upass)
       
            else:
               switch_modes(item, serve_state[item], user, upass)


if __name__ == "__main__":
    main()
