import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('swapnilpatil46117@gmail.com', 'xvfxeadltnyzbfxj')
server.sendmail('swapnilpatil46117@gmail.com', 'devapukale929@gmail.com', 'Mail send from python.')
