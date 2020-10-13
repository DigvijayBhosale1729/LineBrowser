import optparse

def inputfn():
    usage = "usage: python3 browser.py [options] argument use -h for help"
    parser=optparse.OptionParser(usage=usage)
    parser.add_option('-u', dest='website', type='string', help='Specify url of website you want to browse')
    parser.add_option('-t', dest='itype', type='int', help='Specify the type of identifier you want to use to search 1 for ID, 2 for Link Text, 3 for Name, 4 for Tag Name, 5 for Xpath')
    parser.add_option('-i', dest='identifier', type='string', help='Specify the identifier you want to use for searching')
    parser.add_option('-m', dest='uinput', type='string', help='Specify the text you want to input into the search field')
    parser.add_option('-c', dest='clicker', type='string', help='Specify link text you want to click after searching')
    (options, args)=parser.parse_args()
    website=options.website
    identifier=options.identifier
    uinput=options.uinput
    itype=options.itype
    clicker=options.clicker
    data = [None, None, None, None, None]
    data[0] = website
    if identifier==None or uinput==None or itype==None :
        return (data)
    data[1]=identifier
    data[2]=uinput
    data[3]=itype
    if clicker==None:
        data[4]==0
    data[4]=clicker
    return(data)
