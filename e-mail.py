import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('spyridoni164@gmail.com', '')
server.server('spyridoni164@gmail.com',
              'watervga2@gmail.com',
              'hello'              
)