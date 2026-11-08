IGNOREZ botexample.py, IL EST LA POUR SI JE VEUT TESTER DE FAIRE UN BOT QUI REPONDS QUE A DES COMMANDES

Commandes a executer avant de lancer

    sudo apt install python3-full
    python3 -m venv ./.venv
    source ./.venv/bin/activate
    pip install -U discord.py
    pip install -U python-dotenv

attention parfois le premier essait peut echouer, juste reessayer apres un moment

pour faire un bot faut aller a https://discord.com/developers/applications, cliquer sur new application, puis aller dans bot, cliquer sur reset token et le mettre dans le .env, (enable les 3 intents sinon ce bot marche pas prcq il utilise intents all), aller dans OAuth2 dans scopes cliquer sur bot et dans bot permissions sur administrator, puis copier le lien dans le browser pour introduire le bot dans le server (en le selectionnant dans le dropdown)
