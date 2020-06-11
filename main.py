import discord
import asyncio
import random
import time
import source #arquivo criado empython na mesma pasta que este onde defino o TOKEN

client = discord.Client() #cria instância com o client, que é nossa ligação com o discord

@client.event
async def on_ready(): #função chamada quando o bot loga
    print('{} ONLINE'.format(client.user.name))
    print('ID:',client.user.id)
    print('URL: https://discord.com/oauth2/authorize?client_id={}&scope=bot'.format(client.user.id))


@client.event
async def on_message (message):
    if message.author == client.user: #previne o bot de chamar a si mesmo
        return


    if message.content.startswith('edhelp'):
        texto = open('help.txt')
        for i in range(random.randint(1,13)):
            linha = texto.readline()
            await message.channel.send(linha)

    if message.content.startswith('edchegou'): #quando o bot recebe uma mensagem
        await message.channel.send('Ednaldo Pereira Chegou!')
        valor = random.randint(1,10)
        if valor == 1:
            await message.channel.send('Para alegria do servidor.')
        if valor == 2:
            await message.channel.send('Para acabar com a tristeza dos corações tristes.')

    if message.content.startswith('ediga'): #repete o que o usuário diz
        fullmsg = (message.content)
        msg = fullmsg.split('ediga ')
        await message.channel.send(msg[1])

    if message.content.startswith('valenada'):
        await message.channel.send('Vale TUDO!')
    if message.content.startswith('valetudo'):
        await message.channel.send('Vale NADA!')

    if message.content.startswith('oi ednaldo'): #saúda seus fãs
        fullname = str(message.author)
        name = fullname.split('#')
        await message.channel.send('Olá, {}! Meu grande fã!'.format(name[0]))

    if message.content.startswith('edviado'): #xinga de volta
        await message.channel.send('viado é pato')
        time.sleep(0.6)
        await message.channel.send('pato é gay')
        time.sleep(0.6)
        await message.channel.send('teu cu rachado')
        time.sleep(0.8)
        valor = random.randint(1,6)
        if valor == 1:
            await message.channel.send('CHICO MELANCIA! 🍉')
        elif valor == 2:
            await message.channel.send('minha língua dento! 👅')
        elif valor == 3:
            await message.channel.send('minha cobra na toca! 🐍')
        elif valor == 4:
            await message.channel.send('e merda saindo! 💩')
        elif valor == 5:
            await message.channel.send('e as pomba entrando! :dove:')
        elif valor == 6:
            await message.channel.send('ESTÁ FALTANDO LENHA! :palm_tree:')
        #tem espaço pra mais a depender da criatividade

#Seta dados de RPG
    if message.content.startswith('ed20'): #seta a rolagem de um d20
        valor = random.randint(1,20)
        await message.channel.send(valor)
    if message.content.startswith('ed12'): #seta a rolagem de um d12
        valor = random.randint(1,12)
        await message.channel.send(valor)
    if message.content.startswith('ed10'): #seta a rolagem de um d10
        valor = random.randint(1,10)
        await message.channel.send(valor)
    if message.content.startswith('ed%'): #seta a rolagem de um d10
        valor = random.randint(1,10)
        await message.channel.send('{}%'.format(valor*10))
    if message.content.startswith('ed8'): #seta a rolagem de um d8
        valor = random.randint(1,8)
        await message.channel.send(valor)
    if message.content.startswith('ed6'): #seta a rolagem de um d6
        valor = random.randint(1,6)
        await message.channel.send(valor)
    if message.content.startswith('ed4'): #seta a rolagem de um d4
        valor = random.randint(1,4)
        await message.channel.send(valor)

# Seta o rolar de uma moeda e responde com emojis 'cara' ou 'coroa'
    if message.content.lower().startswith('edmoeda'):  # flipcoin
        escolha = random.randint(1, 2)
        if escolha == 1:
            await message.add_reaction('😀')  # imprime a reação no comentário ('cara')
        if escolha == 2:
            await message.add_reaction('👑')  # imprime a reação no comentário ('coroa')

#Retorna nomes de pokémons
    if message.content.startswith('edpokemon'):
        texto = open('pokemon.txt')
        for i in range(random.randint(1,148)):
            linha = texto.readline()
        await message.channel.send(linha)

#citações comunistas
    if message.content.lower().startswith('edcomunista'):
        await message.add_reaction('⚒')  # envia picareta(foice) e martelo como reação na mensagem
        texto = open('citacoes.txt')
        for i in range(random.randint(1,48)):
            linha = (texto.readline())
        await message.channel.send(linha)

#Reações com Emojis

    if message.content.lower().startswith('edcapitalista'):
        escolha = random.randint(1,2)
        if escolha == 1:
            await message.channel.send('🖕') #envia cotoco no chat
        else:
            await message.add_reaction('🖕') #envia cotoco como reação na mensagem

    if message.content.startswith('edpeida'):
        await message.channel.send('💨') #envia peido no chat

    if message.content.lower().startswith('edpython'):
        escolha = random.randint(1, 2)
        if escolha == 1:
            await message.channel.send('🐍')  # envia a cobra no chat
        else:
            await message.add_reaction('🐍')  # envia a cobra como reação na mensagem

#seta um jogo de adivinha semelhante à bola 8
    if message.content.startswith('edvinha'):
        escolha = random.randint(1,15)
        if escolha == 1:
            await message.channel.send('SIM')
        elif escolha == 2:
            await message.channel.send('NÃO')
        elif escolha == 3:
            await message.channel.send('Só depende de você')
        elif escolha == 4:
            await message.channel.send('Pare de pensar nisto!')
        elif escolha == 5:
            await message.channel.send('Pouco provável')
        elif escolha == 6:
            await message.channel.send('Depois da quarentena')
        elif escolha == 7:
            await message.channel.send('Pergunte a sua mãe')
        elif escolha == 8:
            await message.channel.send('Digite \"edmoeda\". Cara = sim, coroa = não')
        elif escolha == 9:
            await message.channel.send('Vai esperar sentado!')
        elif escolha == 10:
            await message.channel.send('Um dia')
        elif escolha == 11:
            await message.channel.send('Com toda a certeza!')
        elif escolha == 12:
            await message.channel.send('Peça pra Deus, que é certeza')
        elif escolha == 13:
            await message.channel.send('Ano que vem')
        elif escolha == 14:
            await message.channel.send('Pergune de novo, vou pensar melhor')
        elif escolha == 15:
            await message.channel.send('Não agora')
        # tem espaço pra mais a depender da criatividade


client.run(source.TOKEN)
#rodando o client com seu token