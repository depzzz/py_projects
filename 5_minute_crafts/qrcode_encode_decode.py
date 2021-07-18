import qrcode

data = 'if you come across this well then marry me cause no one fucking gives me attention uwu and the fact that you are here says something without you that you love me so from now on you are mine so shut up and kiss me and maybe idk well nothing else just kiss me and we can think about other pretty uwu stuff later when we hold hands and slow dance in the dark while ariana grande is playing in the background aaaaaaaaaaaaaaaaaaaaaaaaaaaaa i am horny'

img = qrcode.make(data)
img.save('/home/depsy/Deepanshu/Extra/Web/cs50w/python/environments/myqrcode.png')